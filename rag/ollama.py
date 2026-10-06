"""Client minimal pour Ollama (modèles locaux, aucune clé, aucun envoi de
données à l'extérieur) — bibliothèque standard uniquement."""
import json
import urllib.request

URL = "http://localhost:11434"


def _post(chemin: str, corps: dict, delai: int = 600) -> dict:
    requete = urllib.request.Request(
        URL + chemin,
        data=json.dumps(corps).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(requete, timeout=delai) as reponse:
        return json.loads(reponse.read())


def vectoriser(modele: str, textes: list[str]) -> list[list[float]]:
    return _post("/api/embed", {"model": modele, "input": textes})["embeddings"]


def generer(modele: str, systeme: str, question: str, max_tokens: int = 260) -> str:
    reponse = _post(
        "/api/chat",
        {
            "model": modele,
            "stream": False,
            "messages": [
                {"role": "system", "content": systeme},
                {"role": "user", "content": question},
            ],
            # Température 0 : la même question donne la même réponse, ce qui
            # rend l'évaluation rejouable.
            "options": {"temperature": 0, "num_predict": max_tokens, "seed": 7},
        },
    )
    return reponse["message"]["content"].strip()
