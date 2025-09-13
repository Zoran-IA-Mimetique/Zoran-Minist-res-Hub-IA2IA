# AUDIT_NOTE.md

## Incohérences observées
1) Pas de tests automatisés/CI intégrée
2) README module‑spécifique manquant pour certains POC
3) Versioning non standard (RELEASE_LIST non SemVer)
4) Sécurité déclarée (Merkle, kill‑switch) non démontrée

## Plan de remédiation
- Ajouter `ci_benchmark_ministere.yml` (GitHub Actions) — déplacez en .github/workflows/
- Rédiger des mini‑README par POC
- Normaliser `CHANGELOG.md` (SemVer) + tags Git
- POC Merkle & kill‑switch humain (journal + bouton)

## KPI de succès
- 1 tag/release / mois
- 1 benchmark vert / commit
- 1 audit externe / trimestre
