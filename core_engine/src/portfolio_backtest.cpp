#include "portfolio_backtest.h"

#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <unordered_map>

namespace {

std::map<std::string, std::unordered_map<std::string, double>> build_price_grid(
    const std::vector<PortfolioPriceBar>& prices
) {
    std::map<std::string, std::unordered_map<std::string, double>> grid;
    for (const auto& bar : prices) {
        grid[bar.date][bar.symbol] = bar.close;
    }
    return grid;
}

bool has_all_symbols(
    const std::unordered_map<std::string, double>& row,
    const std::vector<PortfolioTarget>& targets
) {
    for (const auto& target : targets) {
        if (row.find(target.symbol) == row.end()) {
            return false;
        }
    }
    return true;
}

double compute_equity(
    double cash,
    const std::vector<PortfolioTarget>& targets,
    const std::unordered_map<std::string, double>& row,
    const std::unordered_map<std::string, double>& quantities
) {
    double equity = cash;
    for (const auto& target : targets) {
        const auto qty_it = quantities.find(target.symbol);
        const auto px_it = row.find(target.symbol);
        if (qty_it == quantities.end() || px_it == row.end()) {
            continue;
        }
        equity += qty_it->second * px_it->second * target.factor;
    }
    return equity;
}

void rebalance_to_targets(
    const std::string& date,
    double total_equity,
    const std::vector<PortfolioTarget>& targets,
    const std::unordered_map<std::string, double>& row,
    double fee_rate,
    double& cash,
    std::unordered_map<std::string, double>& quantities,
    std::vector<PortfolioTrade>& trades
) {
    for (const auto& target : targets) {
        const auto px_it = row.find(target.symbol);
        if (px_it == row.end() || px_it->second <= 0.0 || target.factor <= 0.0) {
            continue;
        }

        const double price = px_it->second;
        const double current_qty = quantities[target.symbol];
        const double current_value = current_qty * price * target.factor;
        const double target_value = total_equity * target.weight;
        const double diff_value = target_value - current_value;

        if (std::abs(diff_value) < 1e-9) {
            continue;
        }

        if (diff_value > 0.0) {
            const double quantity = diff_value / (price * target.factor * (1.0 + fee_rate));
            if (quantity <= 0.0) {
                continue;
            }
            const double notional = quantity * price * target.factor;
            const double fee = notional * fee_rate;
            quantities[target.symbol] = current_qty + quantity;
            cash -= (notional + fee);
            trades.push_back({date, target.symbol, quantity, price, true, notional, fee});
        } else {
            double quantity = std::abs(diff_value) / (price * target.factor);
            quantity = std::min(quantity, current_qty);
            if (quantity <= 0.0) {
                continue;
            }
            const double notional = quantity * price * target.factor;
            const double fee = notional * fee_rate;
            quantities[target.symbol] = current_qty - quantity;
            cash += (notional - fee);
            trades.push_back({date, target.symbol, quantity, price, false, notional, fee});
        }
    }
}

}  // namespace

PortfolioBacktestEngine::PortfolioBacktestEngine() = default;

PortfolioBacktestResult PortfolioBacktestEngine::run_weighted(
    double initial_cash,
    const std::vector<PortfolioTarget>& targets,
    const std::vector<PortfolioPriceBar>& prices,
    int rebalance_interval_days,
    double fee_bps
) const {
    PortfolioBacktestResult result{};
    result.final_equity = initial_cash;
    result.final_cash = initial_cash;

    if (initial_cash <= 0.0 || targets.empty() || prices.empty()) {
        return result;
    }

    const auto grid = build_price_grid(prices);
    std::unordered_map<std::string, double> quantities;
    for (const auto& target : targets) {
        quantities[target.symbol] = 0.0;
    }

    const double fee_rate = fee_bps / 10000.0;
    double cash = initial_cash;
    int elapsed_days = 0;
    bool invested = false;

    for (const auto& date_row : grid) {
        const auto& date = date_row.first;
        const auto& row = date_row.second;
        if (!has_all_symbols(row, targets)) {
            continue;
        }

        const bool should_rebalance = !invested || (rebalance_interval_days > 0 && elapsed_days > 0 && (elapsed_days % rebalance_interval_days) == 0);
        if (should_rebalance) {
            const double equity_before = compute_equity(cash, targets, row, quantities);
            rebalance_to_targets(date, equity_before, targets, row, fee_rate, cash, quantities, result.trades);
            invested = true;
        }

        const double equity = compute_equity(cash, targets, row, quantities);
        result.equity_curve.push_back({date, equity, cash});
        result.final_equity = equity;
        result.final_cash = cash;
        elapsed_days += 1;
    }

    return result;
}