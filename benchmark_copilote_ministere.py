#!/usr/bin/env python3
import time, json, subprocess, sys

POCS = [
    ("fairdispatch", "POC_FairDispatch_Sante.py"),
    ("rollback", "POC_EquityRollback.py"),
]

results = {}

for name, script in POCS:
    start = time.time()
    try:
        proc = subprocess.run(["python3", script], capture_output=True, timeout=30)
        duration = time.time() - start
        results[name] = {
            "exit_code": proc.returncode,
            "stdout": proc.stdout.decode("utf-8", errors="ignore")[:300],
            "stderr": proc.stderr.decode("utf-8", errors="ignore")[:300],
            "time_s": round(duration, 3)
        }
    except Exception as e:
        results[name] = {"error": str(e)}

results["summary"] = {
    "success": sum(1 for r in results.values() if isinstance(r, dict) and r.get("exit_code") == 0),
    "total": len(POCS)
}

with open("benchmark_report.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Benchmark terminé — voir benchmark_report.json")
