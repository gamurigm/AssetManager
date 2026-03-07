#pragma once

#include <string>
#include <vector>

struct PortfolioTarget {
    std::string symbol;
    double weight;
    double factor;
};

struct PortfolioPriceBar {
    std::string date;
    std::string symbol;
    double close;
};

struct PortfolioTrade {
    std::string date;
    std::string symbol;
    double quantity;
    double price;
    bool is_buy;
    double notional;
    double fee;
};

struct PortfolioEquityPoint {
    std::string date;
    double equity;
    double cash;
};

struct PortfolioBacktestResult {
    double final_equity;
    double final_cash;
    std::vector<PortfolioTrade> trades;
    std::vector<PortfolioEquityPoint> equity_curve;
};

class PortfolioBacktestEngine {
public:
    PortfolioBacktestEngine();

    PortfolioBacktestResult run_weighted(
        double initial_cash,
        const std::vector<PortfolioTarget>& targets,
        const std::vector<PortfolioPriceBar>& prices,
        int rebalance_interval_days,
        double fee_bps
    ) const;
};