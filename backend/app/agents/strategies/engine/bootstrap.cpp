// bootstrap.cpp
// Compile with: g++ -O3 -shared -o bootstrap.dll bootstrap.cpp
#include <vector>
#include <random>
#include <algorithm>
#include <numeric>

extern "C" {

    // Structure to hold the return results
    struct BootstrapResult {
        double net_profit_2_5;
        double net_profit_97_5;
        double max_dd_2_5;
        double max_dd_97_5;
    };

    // Main function to run bootstrap
    // pnl_array: array of PnL values from trades
    // num_trades: size of pnl_array
    // initial_equity: starting balance
    // iterations: number of bootstrap samples (e.g. 10000)
    // result_out: pointer to struct to receive results
    __declspec(dllexport) void run_bootstrap(
        const double* pnl_array, 
        int num_trades, 
        double initial_equity, 
        int iterations, 
        BootstrapResult* result_out,
        double* out_net_profits,
        double* out_max_drawdowns
    ) {
        if (num_trades == 0 || iterations == 0) {
            result_out->net_profit_2_5 = 0.0;
            result_out->net_profit_97_5 = 0.0;
            result_out->max_dd_2_5 = 0.0;
            result_out->max_dd_97_5 = 0.0;
            return;
        }

        std::vector<double> net_profits(iterations);
        std::vector<double> max_drawdowns(iterations);

        // Random number generation setup
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, num_trades - 1);

        for (int i = 0; i < iterations; ++i) {
            double current_equity = initial_equity;
            double peak_equity = initial_equity;
            double max_dd = 0.0;

            for (int j = 0; j < num_trades; ++j) {
                // Randomly sample with replacement
                int idx = dis(gen);
                double pnl = pnl_array[idx];
                
                current_equity += pnl;

                if (current_equity > peak_equity) {
                    peak_equity = current_equity;
                }

                double dd_pct = (peak_equity - current_equity) / peak_equity;
                if (dd_pct > max_dd) {
                    max_dd = dd_pct;
                }
            }

            net_profits[i] = current_equity - initial_equity;
            max_drawdowns[i] = max_dd * 100.0; // Drawdown in %
        }

        // Sort to find percentiles
        std::sort(net_profits.begin(), net_profits.end());
        std::sort(max_drawdowns.begin(), max_drawdowns.end());

        int idx_2_5 = static_cast<int>(iterations * 0.025);
        int idx_97_5 = static_cast<int>(iterations * 0.975);

        // Bounds check
        if (idx_2_5 >= iterations) idx_2_5 = iterations - 1;
        if (idx_97_5 >= iterations) idx_97_5 = iterations - 1;

        result_out->net_profit_2_5 = net_profits[idx_2_5];
        result_out->net_profit_97_5 = net_profits[idx_97_5];
        
        result_out->max_dd_2_5 = max_drawdowns[idx_2_5];
        result_out->max_dd_97_5 = max_drawdowns[idx_97_5];

        if (out_net_profits != nullptr) {
            std::copy(net_profits.begin(), net_profits.end(), out_net_profits);
        }
        if (out_max_drawdowns != nullptr) {
            std::copy(max_drawdowns.begin(), max_drawdowns.end(), out_max_drawdowns);
        }
    }
}

