#pragma once
#include <vector>
#include <string>

struct Order {
    std::string id;
    std::string symbol;
    double price;
    int quantity;
    bool is_buy;
};

class OrderMatchingEngine {
public:
    OrderMatchingEngine();
    void add_order(const Order& order);
    std::vector<Order> get_order_book(const std::string& symbol);
private:
    // Basic storage for now
    std::vector<Order> orders;
};
