"""Scan OpenBB SDK for all endpoints that support chart=True."""
from openbb import obb
import inspect


def scan_router(obj, prefix=""):
    results = []
    for name in sorted(dir(obj)):
        if name.startswith("_"):
            continue
        attr = getattr(obj, name, None)
        if attr is None:
            continue
        full_path = f"{prefix}.{name}" if prefix else name

        if callable(attr):
            try:
                sig = inspect.signature(attr)
            except (ValueError, TypeError):
                continue
            if "chart" in sig.parameters:
                params = []
                for pname, p in sig.parameters.items():
                    if pname in ("chart", "provider", "extra_params", "kwargs"):
                        continue
                    if p.default is inspect.Parameter.empty:
                        params.append(pname)
                    else:
                        params.append(f"{pname}={p.default!r}")
                results.append((full_path, params))
        else:
            if isinstance(attr, (str, int, float, bool, list, dict, type(None))):
                continue
            try:
                results.extend(scan_router(attr, full_path))
            except Exception:
                pass
    return results


if __name__ == "__main__":
    chart_cmds = scan_router(obb)
    chart_cmds.sort(key=lambda x: x[0])

    print(f"=== {len(chart_cmds)} COMANDOS OpenBB CON chart=True ===\n")
    
    # Group by category
    categories = {}
    for cmd, params in chart_cmds:
        cat = cmd.split(".")[0] if "." in cmd else "root"
        categories.setdefault(cat, []).append((cmd, params))

    for cat in sorted(categories):
        print(f"--- {cat.upper()} ---")
        for cmd, params in categories[cat]:
            p_str = ", ".join(params)
            print(f"  obb.{cmd}({p_str}, chart=True)")
        print()
