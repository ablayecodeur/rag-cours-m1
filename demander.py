"""Étape 2 — pose une question aux cours.
Usage : python demander.py "Qu'est-ce qu'une API REST ?" [--naif]"""
import sys

from rag import config, index, repondre

arguments = [a for a in sys.argv[1:] if not a.startswith("--")]
if not arguments:
    raise SystemExit(__doc__)
mode = "naif" if "--naif" in sys.argv else "strict"
conf = config.charger()
matrice, passages = index.charger()
r = repondre.repondre(conf, matrice, passages, arguments[0], mode)
print(f"\n{r['reponse']}\n")
print(f"Mode : {r['mode']} · meilleur score : {r['meilleur_score']} · {r['duree_s']} s")
for n, s in enumerate(r["sources"], start=1):
    print(f"  [{n}] {s['fichier']}, page {s['page']} (score {s['score']})")
