"""Run the minimal Deep Agent from the command line."""

from __future__ import annotations

import argparse
import sys

from app.agents.deep_agent import invoke_deep_agent


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the AssetManager Deep Agent")
    parser.add_argument("request", nargs="+", help="The request to send to the agent")
    args = parser.parse_args()
    try:
        print(invoke_deep_agent(" ".join(args.request)))
    except ValueError as exc:
        parser.error(str(exc))
    except Exception as exc:
        # SDK error strings may contain provider details; never print secrets.
        print(f"Deep Agent failed ({type(exc).__name__}). Check model, endpoint and credentials.", file=sys.stderr)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
