"""Étape 3 — pose les mêmes questions aux deux versions et compare.

Trois familles de questions (evaluation/questions.json) :
- « dans-les-cours » : la réponse existe, on connaît la page ;
- « piege-hors-cours » : le sujet n'apparaît nulle part dans le corpus ;
- « piege-proche » : le sujet est voisin d'un cours, mais la réponse n'y est
  pas (ou la question repose sur une fausse prémisse).

Usage : python evaluer.py            # tout
        python evaluer.py strict     # un seul mode
Écrit le détail dans donnees/ (local) et un résumé publiable dans
evaluation/resultats.md."""
import json
import sys
from pathlib import Path

from rag import config, index, repondre

modes = sys.argv[1:] or ["naif", "strict"]
conf = config.charger()
matrice, passages = index.charger()
questions = json.loads(Path("evaluation/questions.json").read_text(encoding="utf-8"))

detail = []
for q in questions:
    for mode in modes:
        r = repondre.repondre(conf, matrice, passages, q["question"], mode)
        attendue = q.get("source")
        r["id"], r["type"] = q["id"], q["type"]
        r["source_retrouvee"] = (
            any(attendue["fichier"] in s["fichier"] and s["page"] == attendue["page"] for s in r["sources"])
            if attendue
            else None
        )
        detail.append(r)
        print(f"[{mode:6s}] {q['id']:22s} score {r['meilleur_score']:.3f} refus={r['refus']!s:5s} {r['duree_s']:5.1f}s")

config.DONNEES.mkdir(exist_ok=True)
(config.DONNEES / "resultats-detail.json").write_text(json.dumps(detail, ensure_ascii=False, indent=2), encoding="utf-8")


def bilan(mode: str) -> dict:
    lignes = [r for r in detail if r["mode"] == mode]
    cours = [r for r in lignes if r["type"] == "dans-les-cours"]
    pieges = [r for r in lignes if r["type"] != "dans-les-cours"]
    return {
        "source": sum(bool(r["source_retrouvee"]) for r in cours),
        "repondu": sum(not r["refus"] for r in cours),
        "cours": len(cours),
        "refus": sum(r["refus"] for r in pieges),
        "pieges": len(pieges),
    }


# Le résumé publiable ne cite que le nom du cours et la page, jamais le nom
# des fichiers (ils portent parfois celui de l'enseignant).
sortie = ["# Résultats de l'évaluation", ""]
sortie += [f"Modèle de génération : `{conf['modele_generation'].split('/')[-1]}` · embeddings : `{conf['modele_embeddings']}` · "
           f"{len(passages)} passages · {conf['passages_par_question']} passages par question · seuil {conf['seuil_pertinence']}", ""]
sortie += ["| Mode | Bonne page retrouvée | Questions de cours répondues | Pièges refusés |", "|---|---|---|---|"]
for mode in modes:
    b = bilan(mode)
    sortie.append(f"| {mode} | {b['source']}/{b['cours']} | {b['repondu']}/{b['cours']} | {b['refus']}/{b['pieges']} |")
sortie.append("")
for q in questions:
    sortie += [f"## {q['question']}", "", f"Type : {q['type']}", ""]
    for r in (r for r in detail if r["id"] == q["id"]):
        premiere = r["sources"][0]
        etat = "refus" if r["refus"] else "réponse"
        sortie += [
            f"**{r['mode']}** — {etat} · meilleur score {r['meilleur_score']} · "
            f"premier passage : {premiere['cours']}, page {premiere['page']}"
            + ("" if r["source_retrouvee"] is None else f" · bonne page retrouvée : {'oui' if r['source_retrouvee'] else 'non'}"),
            "",
            "> " + r["reponse"].replace("\n", "\n> "),
            "",
        ]
Path("evaluation/resultats.md").write_text("\n".join(sortie), encoding="utf-8")
print("\nRésumé : evaluation/resultats.md")
