export type KpiSnapshot = {
    total_trades: number;
    wins: number;
    losses: number;
    win_rate: number;
    expectancy_r: number;
    profit_factor: number;
    max_drawdown_pct: number;
    sharpe_ratio: number;
    avg_rr_realized: number;
    total_r: number;
    final_equity: number;
    cagr: number;
};

export type LiveTrade = {
    signal_id: string;
    timestamp: string;
    direction: string;
    entry: number;
    stop: number;
    tp: number;
    outcome: string;
    pnl_r: number;
    pnl_usd: number;
    exit_price?: number;
    exit_timestamp?: string;
};

export type ProgressState = {
    day: number;
    total: number;
    pct: number;
};

export type BootstrapLiveData = {
    iterations: number;
    net_profit_95_ci: [number, number];
    max_drawdown_95_ci_pct: [number, number];
    net_profit_samples: number[];
    max_drawdown_samples: number[];
};

export type CompletedResult = {
    sim_id: string;
    symbol: string;
    strategy: string;
    status: string;
    kpis: KpiSnapshot;
    trading_days: number;
    total_trades: number;
    bootstrap?: {
        iterations: number;
        net_profit_95_ci: [number, number];
        max_drawdown_95_ci_pct: [number, number];
    } | null;
    report_url?: string | null;
};

export type EquityPoint = {
    label: string;
    equity: number;
};

export type RegimeDist = {
    mean_ret: number;
    std_ret: number;
    annualized_vol_pct: number;
    annualized_ret_pct: number;
    sharpe: number;
    count: number;
    label: string;
    color: string;
};

export type RegimeData = {
    regime_sequence: { date: string; state: number; vol: number; ret: number }[];
    state_colors: Record<string, string>;
    state_labels: Record<string, string>;
    distributions: Record<string, RegimeDist>;
    transition_matrix: number[][];
    current_label: string;
    next_probs: Record<string, number>;
};

export type IvContract = {
    strike: number;
    moneyness_pct: number;
    type: string;
    iv: number;
    iv_pct: number;
    market_price: number;
    bid: number;
    ask: number;
    volume: number;
    open_interest: number;
};

export type IvExpiration = {
    exp_date: string;
    dte: number;
    atm_iv: number | null;
    smile: IvContract[];
};

export type IvSmileData = {
    symbol: string;
    spot: number;
    rf: number;
    as_of: string;
    expirations: IvExpiration[];
};

export type IVOptionContext = {
    available: boolean;
    error?: string;
    signal_mode?: string;
    direction_bias?: "LONG" | "SHORT" | "FLAT";
    exp_date?: string;
    dte?: number;
    strike?: number;
    moneyness_pct?: number | null;
    atm_iv_pct?: number | null;
    atm_call_iv_pct?: number | null;
    atm_put_iv_pct?: number | null;
    skew_pct?: number | null;
    call_price?: number | null;
    put_price?: number | null;
    iv_realized_spread_pct?: number | null;
    iv_realized_ratio?: number | null;
    source?: string;
    as_of?: string;
};

export type IVCurrentSignal = {
    date: string;
    close: number;
    iv_rank: number;
    regime: string;
    momentum_pct: number;
    direction: "LONG" | "SHORT" | "FLAT";
    proxy_direction?: "LONG" | "SHORT" | "FLAT";
    signal_source?: string;
    daily_vol_pct?: number;
    realized_vol_ann_pct?: number;
    option_context?: IVOptionContext;
};

export type ArchVolPoint = {
    date: string;
    sigma_pct: number;      // daily conditional vol %
    sigma_ann_pct: number;  // annualised conditional vol %
    ret_pct: number;        // log-return %
};

export type ArchVolData = {
    symbol: string;
    n_obs: number;
    model: string;
    params: {
        mu: number;
        omega: string;
        alpha: number;
        beta: number;
        persistence: number;
    };
    fit: { log_likelihood: number; aic: number; bic: number };
    long_run_vol_ann_pct: number;
    current_sigma_ann_pct: number;
    forecast: { h1_ann_pct: number; h5_ann_pct: number; h21_ann_pct: number };
    var_daily: { var_95_pct: number; var_99_pct: number };
    arch_lm_test: { stat: number; p_value: number; adequate: boolean | null };
    conditional_vol: ArchVolPoint[];
};

export type KalmanFilterPoint = {
    date: string;
    observed: number;
    predicted: number;
    filtered: number;
    innovation: number;
    innovation_z: number;
    gain: number;
    variance: number;
    lower_1sigma: number;
    upper_1sigma: number;
    mean_gap_pct: number | null;
};

export type KalmanFilterData = {
    symbol: string;
    n_obs: number;
    model: string;
    ou_interpretation: boolean;
    calibration: {
        alpha: number;
        beta: number;
        residual_std: number;
        process_noise_q: number;
        measurement_noise_r: number;
        measurement_noise_mult: number;
        stationary: boolean;
        long_run_mean: number | null;
        half_life_days: number | null;
    };
    diagnostics: {
        rmse_filtered_vs_observed: number;
        mean_abs_innovation: number;
        avg_gain: number;
        last_gain: number;
        last_innovation_z: number;
        smoothness_ratio: number;
    };
    current_state: {
        observed: number;
        predicted: number;
        filtered: number;
        innovation: number;
        innovation_z: number;
        gain: number;
        variance: number;
        lower_1sigma: number;
        upper_1sigma: number;
        spread_pct: number;
        pull_signal: "UP" | "DOWN" | "NEUTRAL";
        mean_gap_pct: number | null;
    };
    series: KalmanFilterPoint[];
};
