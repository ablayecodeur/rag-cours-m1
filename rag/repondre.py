"""De la question à la réponse, en deux versions.

- « naif » : la première version, celle qu'on écrit en suivant un tutoriel.
  Elle donne toujours les passages trouvés au modèle et lui demande de
  répondre.
- « strict » : la version corrigée. Si aucun passage n'est assez proche de
  la question, le modèle n'est même pas appelé ; sinon il doit s'en tenir
  aux extraits et les citer.

Les deux existent pour pouvoir les comparer sur les mêmes questions."""
import time

from . import index, ollama

REFUS = "Je ne trouve pas cela dans les cours fournis."

SYSTEME_NAIF = (
    "Tu es un assistant pour un étudiant en Master Systèmes d'Information. "
    "Réponds à la question en français, de façon concise, en t'aidant des "
    "extraits de cours ci-dessous.\n\n{contexte}"
)

SYSTEME_STRICT = (
    "Tu es un assistant pour un étudiant en Master Systèmes d'Information. "
    "Tu réponds UNIQUEMENT à partir des extraits de cours ci-dessous.\n"
    "Règles :\n"
    "1. Si les extraits ne contiennent pas la réponse, réponds exactement : "
    f"« {REFUS} » et rien d'autre.\n"
    "2. N'ajoute aucune information qui ne figure pas dans les extraits, même "
    "si tu la connais.\n"
    "3. Après chaque affirmation, cite l'extrait utilisé entre crochets, par "
    "exemple [1].\n"
    "4. Réponds en français, en quatre phrases au plus.\n\n{contexte}"
)


def _contexte(passages: list[dict]) -> str:
    return "\n\n".join(
        f"[{n}] ({p['cours']}, page {p['page']})\n{p['texte']}" for n, p in enumerate(passages, start=1)
    )


def repondre(conf: dict, matrice, passages, question: str, mode: str = "strict") -> dict:
    debut = time.time()
    trouves = index.chercher(conf, matrice, passages, question)
    meilleur = trouves[0]["score"]
    resultat = {
        "mode": mode,
        "question": question,
        "meilleur_score": round(meilleur, 3),
        "sources": [
            {"cours": p["cours"], "fichier": p["fichier"], "page": p["page"], "score": round(p["score"], 3)}
            for p in trouves
        ],
    }
    if mode == "strict" and meilleur < conf["seuil_pertinence"]:
        # Aucun passage assez proche : on refuse sans appeler le modèle. Un
        # modèle à qui l'on ne demande rien ne peut rien inventer.
        resultat.update(reponse=REFUS, refus=True, modele_appele=False)
    else:
        systeme = (SYSTEME_STRICT if mode == "strict" else SYSTEME_NAIF).format(contexte=_contexte(trouves))
        texte = ollama.generer(conf["modele_generation"], systeme, question)
        resultat.update(reponse=texte, refus=REFUS.rstrip(".").lower() in texte.lower(), modele_appele=True)
    resultat["duree_s"] = round(time.time() - debut, 1)
    return resultat
