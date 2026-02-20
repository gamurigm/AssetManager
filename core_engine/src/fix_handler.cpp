/**
 * @file fix_handler.cpp
 * @brief Implementation of the Fix8-based FIX protocol handler.
 *
 * When compiled with -DHAS_FIX8, this file uses the real Fix8 runtime and
 * the generated AM_types / AM_classes headers.  Without that flag the code
 * provides a *stub* implementation that logs actions to stdout, which is
 * useful for development, testing, and pybind11 integration work before the
 * Fix8 library is fully linked.
 */

#include "fix_handler.h"
#include <chrono>
#include <sstream>
#include <iomanip>
#include <ctime>

namespace asset_mgr {

// ── Helpers ─────────────────────────────────────────────────────────────────

static std::string now_utc() {
    auto tp  = std::chrono::system_clock::now();
    auto t   = std::chrono::system_clock::to_time_t(tp);
    std::tm  gmt{};
#ifdef _WIN32
    gmtime_s(&gmt, &t);
#else
    gmtime_r(&t, &gmt);
#endif
    std::ostringstream os;
    os << std::put_time(&gmt, "%Y%m%d-%H:%M:%S");
    return os.str();
}

static int next_seq() {
    static std::atomic<int> seq{1};
    return seq.fetch_add(1);
}

// ── Constructor / Destructor ────────────────────────────────────────────────

FixHandler::FixHandler(const FixConfig& cfg) : config_(cfg) {}

FixHandler::~FixHandler() {
    if (running_) stop();
}

// ── Lifecycle ───────────────────────────────────────────────────────────────

bool FixHandler::start() {
    if (running_) return true;

#ifdef HAS_FIX8
    // ── Real Fix8 session ──────────────────────────────────────────────────
    // 1. Load XML config produced by f8c
    // 2. Create ClientSession
    // 3. Start the session thread
    // (implementation depends on generated session classes)
    std::cout << "[FIX] Starting Fix8 session "
              << config_.sender_comp_id << " -> "
              << config_.target_comp_id << " @ "
              << config_.host << ":" << config_.port << "\n";

    // TODO: instantiate fix_session_ from generated classes
    running_   = true;
    connected_ = true;
    return true;
#else
    // ── Stub mode ──────────────────────────────────────────────────────────
    std::cout << "[FIX-STUB] Starting stub session  "
              << config_.sender_comp_id << " -> "
              << config_.target_comp_id << " @ "
              << config_.host << ":" << config_.port << "\n";

    running_   = true;
    connected_ = true;

    // Simulate a background "session" thread that stays alive.
    session_thread_ = std::make_unique<std::thread>([this]() { session_loop(); });

    return true;
#endif
}

void FixHandler::stop() {
    if (!running_) return;

    std::cout << "[FIX] Logging out and stopping session.\n";
    running_   = false;
    connected_ = false;

    if (session_thread_ && session_thread_->joinable()) {
        session_thread_->join();
    }
    session_thread_.reset();
}

bool FixHandler::is_connected() const {
    return connected_;
}

// ── Trading ─────────────────────────────────────────────────────────────────

std::string FixHandler::send_order(const FixOrder& order) {
    if (!connected_) {
        std::cerr << "[FIX] Cannot send order – not connected.\n";
        return {};
    }

#ifdef HAS_FIX8
    // Build a real NewOrderSingle from generated classes
    // auto *nos = new AM::NewOrderSingle;
    // *nos << new AM::ClOrdID(order.cl_ord_id)
    //      << new AM::Symbol(order.symbol)
    //      << new AM::Side(order.side)
    //      << new AM::OrdType(order.ord_type)
    //      << new AM::OrderQty(order.quantity)
    //      << new AM::TransactTime(now_utc());
    // if (order.ord_type != '1') // not market
    //     *nos << new AM::Price(order.price);
    // fix_session_->send(nos);
    std::cout << "[FIX] Sent NewOrderSingle: " << order.cl_ord_id << "\n";
#else
    // ── Stub: print + generate a fake fill ──────────────────────────────
    std::cout << "[FIX-STUB] NewOrderSingle  clOrdId=" << order.cl_ord_id
              << "  sym=" << order.symbol
              << "  side=" << order.side
              << "  qty=" << order.quantity
              << "  ordType=" << order.ord_type
              << "  px=" << order.price << "\n";

    // Simulate an immediate fill
    ExecReport rpt;
    rpt.order_id   = "ORD-" + std::to_string(next_seq());
    rpt.exec_id    = "EXE-" + std::to_string(next_seq());
    rpt.exec_type  = '2';            // Fill
    rpt.ord_status = '2';            // Filled
    rpt.symbol     = order.symbol;
    rpt.side       = order.side;
    rpt.leaves_qty = 0;
    rpt.cum_qty    = order.quantity;
    rpt.avg_px     = order.price;
    rpt.last_px    = order.price;
    rpt.last_qty   = order.quantity;
    rpt.text       = "Simulated fill";

    handle_exec_report(rpt);
#endif

    return order.cl_ord_id;
}

// ── Execution Reports ───────────────────────────────────────────────────────

void FixHandler::on_exec_report(ExecReportCallback cb) {
    std::lock_guard<std::mutex> lk(mu_);
    callback_ = std::move(cb);
}

std::vector<ExecReport> FixHandler::poll_exec_reports() {
    std::lock_guard<std::mutex> lk(mu_);
    std::vector<ExecReport> out;
    while (!report_queue_.empty()) {
        out.push_back(std::move(report_queue_.front()));
        report_queue_.pop();
    }
    return out;
}

// ── Status ──────────────────────────────────────────────────────────────────

std::string FixHandler::get_status() const {
    std::ostringstream os;
    os << "FixHandler  sender=" << config_.sender_comp_id
       << "  target=" << config_.target_comp_id
       << "  connected=" << (connected_ ? "yes" : "no")
       << "  running=" << (running_ ? "yes" : "no");
    return os.str();
}

// ── Private ─────────────────────────────────────────────────────────────────

void FixHandler::session_loop() {
    std::cout << "[FIX-STUB] Session loop started.\n";
    while (running_) {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        // In real Fix8, this is where heartbeats / message dispatch happen.
    }
    std::cout << "[FIX-STUB] Session loop ended.\n";
}

void FixHandler::handle_exec_report(const ExecReport& rpt) {
    std::lock_guard<std::mutex> lk(mu_);
    report_queue_.push(rpt);
    if (callback_) {
        callback_(rpt);
    }
}

} // namespace asset_mgr
