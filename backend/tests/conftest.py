"""Keep the default suite deterministic and free of manual live diagnostics.

The ignored files are executable smoke/diagnostic scripts with no pytest test
functions, or optional native/live checks. They remain runnable explicitly.
"""

collect_ignore = [
    "test_ai_strategy.py",
    "test_bootstrap.py",
    "test_bootstrap_crash.py",
    "test_bootstrap_scale.py",
    "test_bybit.py",
    "test_chat.py",
    "test_cv_real.py",
    "test_db_lock.py",
    "test_deepseek.py",
    "test_finazon.py",
    "test_glm.py",
    "test_intraday.py",
    "test_kb.py",
    "test_market_data.py",
    "test_multi_range.py",
    "test_openbb_agent.py",
    "test_orb_diagnostics.py",
    "test_orchestrator.py",
    "test_pfaff_logic.py",
    "test_report.py",
    "test_search.py",
    "test_sessions.py",
    "test_signals.py",
    "test_stable.py",
    "test_wma_rust.py",
    "test_yahoo.py",
    "test_yf.py",
]
