#include "order_matching.h"

OrderMatchingEngine::OrderMatchingEngine() {}

void OrderMatchingEngine::add_order(const Order& order) {
    orders.push_back(order);
}

std::vector<Order> OrderMatchingEngine::get_order_book(const std::string& symbol) {
    std::vector<Order> result;
    for (const auto& o : orders) {
        if (o.symbol == symbol) {
            result.push_back(o);
        }
    }
    return result;
}
