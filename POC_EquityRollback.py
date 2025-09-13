#!/usr/bin/env python3
# POC_EquityRollback.py — déclenche ΔM11.3 si l'équité tombe sous 0.85

import json, os

THRESHOLD = 0.85

def check_and_trigger(fairness_index):
    if fairness_index < THRESHOLD:
        print("⚠️  Fairness < 0.85 → trigger ΔM11.3 rollback")
        # Ici on simule : écriture d'un "signal" pour l'orchestrateur
        with open("deltaM11_3_signal.json", "w") as f:
            json.dump({"rollback": True, "reason": "fairness_below_threshold", "value": fairness_index}, f, indent=2)
    else:
        print("✅ Fairness OK")

if __name__ == "__main__":
    # Exemple : lire un rapport ou recevoir une valeur
    fairness = float(os.environ.get("FAIRNESS", "0.82"))
    check_and_trigger(fairness)
