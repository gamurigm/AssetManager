#include <iostream>
#include <string>
#include <boost/asio.hpp>

using boost::asio::ip::udp;

class MarketDataFeed {
public:
    MarketDataFeed(short port) : socket_(io_service_, udp::endpoint(udp::v4(), port)) {
        start_receive();
    }

    void run() {
        io_service_.run();
    }

private:
    void start_receive() {
        socket_.async_receive_from(
            boost::asio::buffer(recv_buffer_), remote_endpoint_,
            [this](boost::system::error_code ec, std::size_t bytes_recvd) {
                if (!ec && bytes_recvd > 0) {
                    process_message(std::string(recv_buffer_.data(), bytes_recvd));
                }
                start_receive();
            });
    }

    void process_message(const std::string& message) {
        // Logic to parse message and update order book or notify python
        std::cout << "Received market data: " << message << std::endl;
    }

    boost::asio::io_service io_service_;
    udp::socket socket_;
    udp::endpoint remote_endpoint_;
    std::array<char, 1024> recv_buffer_;
};
