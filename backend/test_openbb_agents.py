import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_tests():
    print("--- 1. Testing Agent Modularity ---")
    try:
        from app.agents.team.specialists import (
            quant_analyst, fundamental_analyst, 
            macro_analyst, risk_manager, trader, strategy_analyst as strat
        )
        
        agents = {
            "Quant Analyst": quant_analyst,
            "Fundamental Analyst": fundamental_analyst,
            "Macro Analyst": macro_analyst,
            "Risk Manager": risk_manager,
            "Trader": trader,
            "Strategy Analyst": strat
        }
        
        all_ok = True
        for name, agent in agents.items():
            if "OPENBB PLATFORM API" in agent.role:
                print(f"[OK] {name}: Loaded modular Markdown role + OpenBB Reference.")
            else:
                print(f"[ERROR] {name}: Did not load OpenBB Reference.")
                all_ok = False
                
            tool_names = list(agent.agent._function_tools.keys()) if hasattr(agent.agent, '_function_tools') else []
            print(f"     Tools configured: {len(tool_names)} tools")
            
            # Check if openbb specific tools are added
            if "execute_openbb_terminal_command" in tool_names:
                print(f"     [OK] Has terminal bridge tool.")
            else:
                print(f"     [WARN] No terminal bridge.")
                
        if all_ok:
            print("[SUCCESS] All 6 specialist agents are correctly modularized and configured!")
            
    except Exception as e:
        print(f"[ERROR] Failed to instantiate team: {e}")

    print("\n--- 2. Testing API Endpoints Integration Tools ---")
    try:
        from app.agents.team.specialists import (
            discover_openbb_endpoints, get_openbb_endpoint_details,
            query_openbb_api, query_openbb_api_post
        )
        print("[OK] OpenBB API dynamic routing tools imported successfully.")
    except Exception as e:
        print(f"[ERROR] Tool import failed: {e}")

if __name__ == "__main__":
    run_tests()
