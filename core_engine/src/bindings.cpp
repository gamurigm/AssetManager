#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "order_matching.h"
#include "market_feed.h"

namespace py = pybind11;

PYBIND11_MODULE(core_engine, m) {
    py::class_<Order>(m, "Order")
        .def(py::init<std::string, std::string, double, int, bool>())
        .def_readwrite("id", &Order::id)
        .def_readwrite("symbol", &Order::symbol)
        .def_readwrite("price", &Order::price)
        .def_readwrite("quantity", &Order::quantity)
        .def_readwrite("is_buy", &Order::is_buy);

    py::class_<OrderMatchingEngine>(m, "OrderMatchingEngine")
        .def(py::init<>())
        .def("add_order", &OrderMatchingEngine::add_order)
        .def("get_order_book", &OrderMatchingEngine::get_order_book);

    py::class_<MarketDataFeed>(m, "MarketDataFeed")
        .def(py::init<short>())
        .def("run", &MarketDataFeed::run);
}
