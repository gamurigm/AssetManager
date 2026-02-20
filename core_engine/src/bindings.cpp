#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include "order_matching.h"
#include "market_feed.h"
#include "fix_handler.h"

namespace py = pybind11;

PYBIND11_MODULE(core_engine, m) {

    // ── Order Matching ──────────────────────────────────────────────────────
    py::class_<Order>(m, "Order")
        .def(py::init<std::string, std::string, double, int, bool>())
        .def_readwrite("id",       &Order::id)
        .def_readwrite("symbol",   &Order::symbol)
        .def_readwrite("price",    &Order::price)
        .def_readwrite("quantity", &Order::quantity)
        .def_readwrite("is_buy",   &Order::is_buy);

    py::class_<OrderMatchingEngine>(m, "OrderMatchingEngine")
        .def(py::init<>())
        .def("add_order",      &OrderMatchingEngine::add_order)
        .def("get_order_book", &OrderMatchingEngine::get_order_book);

    // ── Market Data Feed ────────────────────────────────────────────────────
    py::class_<MarketDataFeed>(m, "MarketDataFeed")
        .def(py::init<short>())
        .def("run", &MarketDataFeed::run);

    // ── FIX Protocol Handler (Fix8) ─────────────────────────────────────────
    using namespace asset_mgr;

    py::class_<FixConfig>(m, "FixConfig")
        .def(py::init<>())
        .def_readwrite("sender_comp_id",     &FixConfig::sender_comp_id)
        .def_readwrite("target_comp_id",     &FixConfig::target_comp_id)
        .def_readwrite("host",               &FixConfig::host)
        .def_readwrite("port",               &FixConfig::port)
        .def_readwrite("heartbeat_interval", &FixConfig::heartbeat_interval);

    py::class_<FixOrder>(m, "FixOrder")
        .def(py::init<>())
        .def_readwrite("cl_ord_id", &FixOrder::cl_ord_id)
        .def_readwrite("symbol",    &FixOrder::symbol)
        .def_readwrite("side",      &FixOrder::side)
        .def_readwrite("ord_type",  &FixOrder::ord_type)
        .def_readwrite("quantity",  &FixOrder::quantity)
        .def_readwrite("price",     &FixOrder::price);

    py::class_<ExecReport>(m, "ExecReport")
        .def(py::init<>())
        .def_readonly("order_id",   &ExecReport::order_id)
        .def_readonly("exec_id",    &ExecReport::exec_id)
        .def_readonly("exec_type",  &ExecReport::exec_type)
        .def_readonly("ord_status", &ExecReport::ord_status)
        .def_readonly("symbol",     &ExecReport::symbol)
        .def_readonly("side",       &ExecReport::side)
        .def_readonly("leaves_qty", &ExecReport::leaves_qty)
        .def_readonly("cum_qty",    &ExecReport::cum_qty)
        .def_readonly("avg_px",     &ExecReport::avg_px)
        .def_readonly("last_px",    &ExecReport::last_px)
        .def_readonly("last_qty",   &ExecReport::last_qty)
        .def_readonly("text",       &ExecReport::text);

    py::class_<FixHandler>(m, "FixHandler")
        .def(py::init<const FixConfig&>(), py::arg("config") = FixConfig{})
        .def("start",              &FixHandler::start,
             "Start the FIX session (Logon)")
        .def("stop",               &FixHandler::stop,
             "Stop the FIX session (Logout)")
        .def("is_connected",       &FixHandler::is_connected,
             "Check if the session is currently logged on")
        .def("send_order",         &FixHandler::send_order,
             py::arg("order"),
             "Send a NewOrderSingle and return the ClOrdID")
        .def("poll_exec_reports",  &FixHandler::poll_exec_reports,
             "Return all queued ExecutionReports")
        .def("get_status",         &FixHandler::get_status,
             "Return a human-readable status string");
}
