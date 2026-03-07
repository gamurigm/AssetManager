#include "../include/portfolio_backtest.h"

#include <algorithm>
#include <array>
#include <cerrno>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <regex>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

#ifdef _WIN32
#include <winsock2.h>
#include <ws2tcpip.h>
#else
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#endif

namespace {

using SocketHandle =
#ifdef _WIN32
    SOCKET;
#else
    int;
#endif

#ifdef _WIN32
constexpr SocketHandle kInvalidSocket = INVALID_SOCKET;
#else
constexpr SocketHandle kInvalidSocket = -1;
#endif

std::string escape_json(const std::string& value) {
    std::string escaped;
    escaped.reserve(value.size());
    for (const char ch : value) {
        switch (ch) {
            case '\\': escaped += "\\\\"; break;
            case '"': escaped += "\\\""; break;
            case '\n': escaped += "\\n"; break;
            case '\r': escaped += "\\r"; break;
            case '\t': escaped += "\\t"; break;
            default: escaped += ch; break;
        }
    }
    return escaped;
}

void close_socket(SocketHandle socket_handle) {
#ifdef _WIN32
    closesocket(socket_handle);
#else
    close(socket_handle);
#endif
}

bool send_all(SocketHandle socket_handle, const std::string& payload) {
    size_t total_sent = 0;
    while (total_sent < payload.size()) {
#ifdef _WIN32
        const int sent = send(socket_handle, payload.data() + total_sent, static_cast<int>(payload.size() - total_sent), 0);
#else
        const ssize_t sent = send(socket_handle, payload.data() + total_sent, payload.size() - total_sent, 0);
#endif
        if (sent <= 0) {
            return false;
        }
        total_sent += static_cast<size_t>(sent);
    }
    return true;
}

size_t parse_content_length(const std::string& headers) {
    const std::regex pattern(R"(Content-Length:\s*(\d+))", std::regex::icase);
    std::smatch match;
    if (std::regex_search(headers, match, pattern)) {
        return static_cast<size_t>(std::stoull(match[1].str()));
    }
    return 0;
}

std::string receive_http_request(SocketHandle socket_handle) {
    std::string request;
    std::array<char, 8192> buffer{};

    size_t header_end = std::string::npos;
    size_t expected_body_length = 0;

    for (;;) {
#ifdef _WIN32
        const int received = recv(socket_handle, buffer.data(), static_cast<int>(buffer.size()), 0);
#else
        const ssize_t received = recv(socket_handle, buffer.data(), buffer.size(), 0);
#endif
        if (received <= 0) {
            break;
        }

        request.append(buffer.data(), static_cast<size_t>(received));
        if (header_end == std::string::npos) {
            header_end = request.find("\r\n\r\n");
            if (header_end != std::string::npos) {
                expected_body_length = parse_content_length(request.substr(0, header_end));
            }
        }

        if (header_end != std::string::npos) {
            const size_t body_size = request.size() - (header_end + 4);
            if (body_size >= expected_body_length) {
                break;
            }
        }
    }

    return request;
}

std::string request_body(const std::string& request) {
    const auto header_end = request.find("\r\n\r\n");
    if (header_end == std::string::npos) {
        return {};
    }
    return request.substr(header_end + 4);
}

std::pair<std::string, std::string> request_line_parts(const std::string& request) {
    const auto line_end = request.find("\r\n");
    const std::string line = request.substr(0, line_end);
    std::istringstream stream(line);
    std::string method;
    std::string path;
    stream >> method >> path;
    return {method, path};
}

double extract_number(const std::string& body, const std::string& key, double fallback = 0.0) {
    const std::regex pattern("\\\"" + key + "\\\"\\s*:\\s*([-+0-9.eE]+)");
    std::smatch match;
    if (std::regex_search(body, match, pattern)) {
        return std::stod(match[1].str());
    }
    return fallback;
}

std::vector<PortfolioTarget> extract_targets(const std::string& body) {
    std::vector<PortfolioTarget> targets;
    const std::regex pattern(R"rgx("symbol"\s*:\s*"([^"]+)"\s*,\s*"weight"\s*:\s*([-+0-9.eE]+)\s*,\s*"factor"\s*:\s*([-+0-9.eE]+))rgx");

    for (std::sregex_iterator it(body.begin(), body.end(), pattern), end; it != end; ++it) {
        PortfolioTarget target{};
        target.symbol = (*it)[1].str();
        target.weight = std::stod((*it)[2].str());
        target.factor = std::stod((*it)[3].str());
        if (!target.symbol.empty() && target.weight > 0.0 && target.factor > 0.0) {
            targets.push_back(target);
        }
    }

    return targets;
}

std::vector<PortfolioPriceBar> extract_prices(const std::string& body) {
    std::vector<PortfolioPriceBar> prices;
    const std::regex pattern(R"rgx("date"\s*:\s*"([^"]+)"\s*,\s*"symbol"\s*:\s*"([^"]+)"\s*,\s*"close"\s*:\s*([-+0-9.eE]+))rgx");

    for (std::sregex_iterator it(body.begin(), body.end(), pattern), end; it != end; ++it) {
        PortfolioPriceBar price_bar{};
        price_bar.date = (*it)[1].str();
        price_bar.symbol = (*it)[2].str();
        price_bar.close = std::stod((*it)[3].str());
        if (!price_bar.date.empty() && !price_bar.symbol.empty() && price_bar.close > 0.0) {
            prices.push_back(price_bar);
        }
    }

    return prices;
}

PortfolioBacktestResult run_backtest_from_body(const std::string& body) {
    PortfolioBacktestEngine engine;
    const auto targets = extract_targets(body);
    const auto prices = extract_prices(body);
    return engine.run_weighted(
        extract_number(body, "initial_cash", 0.0),
        targets,
        prices,
        static_cast<int>(extract_number(body, "rebalance_interval_days", 0.0)),
        extract_number(body, "fee_bps", 0.0)
    );
}

std::string build_health_payload() {
    return R"({"status":"ok","service":"portfolio_cpp_service","version":"1.0.0"})";
}

std::string build_backtest_payload(const PortfolioBacktestResult& result) {
    std::ostringstream payload;
    payload << "{"
            << "\"service\":\"portfolio_cpp_service\"," 
            << "\"engine\":\"cpp-remote\"," 
            << "\"final_equity\":" << result.final_equity << ","
            << "\"final_cash\":" << result.final_cash << ","
            << "\"trades\":[";

    for (size_t index = 0; index < result.trades.size(); ++index) {
        const auto& trade = result.trades[index];
        if (index > 0) {
            payload << ",";
        }
        payload << "{"
                << "\"date\":\"" << escape_json(trade.date) << "\"," 
                << "\"symbol\":\"" << escape_json(trade.symbol) << "\"," 
                << "\"side\":\"" << (trade.is_buy ? "BUY" : "SELL") << "\"," 
                << "\"quantity\":" << trade.quantity << ","
                << "\"price\":" << trade.price << ","
                << "\"notional\":" << trade.notional << ","
                << "\"fee\":" << trade.fee
                << "}";
    }

    payload << "],\"equity_curve\":[";
    for (size_t index = 0; index < result.equity_curve.size(); ++index) {
        const auto& point = result.equity_curve[index];
        if (index > 0) {
            payload << ",";
        }
        payload << "{"
                << "\"date\":\"" << escape_json(point.date) << "\"," 
                << "\"equity\":" << point.equity << ","
                << "\"cash\":" << point.cash
                << "}";
    }

    payload << "]}";
    return payload.str();
}

std::string make_http_response(const std::string& status, const std::string& body) {
    std::ostringstream response;
    response << "HTTP/1.1 " << status << "\r\n"
             << "Content-Type: application/json\r\n"
             << "Server: portfolio_cpp_service\r\n"
             << "Connection: close\r\n"
             << "Content-Length: " << body.size() << "\r\n\r\n"
             << body;
    return response.str();
}

void handle_session(SocketHandle socket_handle) {
    const std::string request = receive_http_request(socket_handle);
    if (request.empty()) {
        close_socket(socket_handle);
        return;
    }

    const auto request_line = request_line_parts(request);
    const std::string& method = request_line.first;
    const std::string& path = request_line.second;
    std::string response;

    try {
        if (method == "GET" && path == "/health") {
            response = make_http_response("200 OK", build_health_payload());
        } else if (method == "POST" && path == "/portfolio/backtest") {
            response = make_http_response("200 OK", build_backtest_payload(run_backtest_from_body(request_body(request))));
        } else {
            response = make_http_response("404 Not Found", R"({"error":"Route not found"})");
        }
    } catch (const std::exception& exc) {
        response = make_http_response(
            "422 Unprocessable Entity",
            std::string("{\"error\":\"") + escape_json(exc.what()) + "\"}"
        );
    }

    send_all(socket_handle, response);
    close_socket(socket_handle);
}

unsigned short resolve_port(int argc, char* argv[]) {
    if (argc > 1) {
        return static_cast<unsigned short>(std::stoi(argv[1]));
    }

#ifdef _WIN32
    char* env_port = nullptr;
    size_t env_length = 0;
    if (_dupenv_s(&env_port, &env_length, "PORTFOLIO_CPP_SERVICE_PORT") == 0 && env_port && *env_port) {
        const unsigned short port = static_cast<unsigned short>(std::stoi(env_port));
        std::free(env_port);
        return port;
    }
    std::free(env_port);
#else
    const char* env_port = std::getenv("PORTFOLIO_CPP_SERVICE_PORT");
    if (env_port && *env_port) {
        return static_cast<unsigned short>(std::stoi(env_port));
    }
#endif

    return 9092;
}

}  // namespace

int main(int argc, char* argv[]) {
    try {
        const auto port = resolve_port(argc, argv);

#ifdef _WIN32
        WSADATA data{};
        if (WSAStartup(MAKEWORD(2, 2), &data) != 0) {
            throw std::runtime_error("WSAStartup failed");
        }
#endif

        const SocketHandle listener = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        if (listener == kInvalidSocket) {
            throw std::runtime_error("Unable to create listening socket");
        }

        int reuse = 1;
#ifdef _WIN32
        setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, reinterpret_cast<const char*>(&reuse), sizeof(reuse));
#else
        setsockopt(listener, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(reuse));
#endif

        sockaddr_in address{};
        address.sin_family = AF_INET;
        address.sin_addr.s_addr = htonl(INADDR_ANY);
        address.sin_port = htons(port);

        if (bind(listener, reinterpret_cast<sockaddr*>(&address), sizeof(address)) != 0) {
            close_socket(listener);
            throw std::runtime_error("Unable to bind listening socket");
        }
        if (listen(listener, SOMAXCONN) != 0) {
            close_socket(listener);
            throw std::runtime_error("Unable to listen on socket");
        }

        std::cout << "[portfolio_cpp_service] Listening on http://0.0.0.0:" << port << std::endl;

        for (;;) {
            sockaddr_in client{};
#ifdef _WIN32
            int client_length = sizeof(client);
#else
            socklen_t client_length = sizeof(client);
#endif
            const SocketHandle client_socket = accept(listener, reinterpret_cast<sockaddr*>(&client), &client_length);
            if (client_socket == kInvalidSocket) {
                continue;
            }
            std::thread(&handle_session, client_socket).detach();
        }
    } catch (const std::exception& exc) {
        std::cerr << "[portfolio_cpp_service] Fatal error: " << exc.what() << std::endl;
        return 1;
    }

    return 0;
}