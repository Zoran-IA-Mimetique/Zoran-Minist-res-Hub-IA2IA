# TEST_PLAN.md

- Lancer `python3 POC_FairDispatch_Sante.py` → vérifier sortie & indice d'équité
- Lancer `FAIRNESS=0.80 python3 POC_EquityRollback.py` → ΔM11.3 signal JSON
- Lancer `python3 benchmark_copilote_ministere.py` → `benchmark_report.json`
- (Option CI) déplacer `ci_benchmark_ministere.yml` en `.github/workflows/`
