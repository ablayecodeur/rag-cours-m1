"""L'index : un tableau NumPy de vecteurs normalisés et la liste des passages.

Pas de base vectorielle : à un millier de passages, un produit matriciel
répond en quelques millisecondes, et chaque étape reste lisible."""
import json

import numpy as np

from . import config, ollama

TAILLE_LOT = 32


def construire(conf: dict, passages: list[dict]) -> None:
    vecteurs = []
    for debut in range(0, len(passages), TAILLE_LOT):
        lot = passages[debut : debut + TAILLE_LOT]
        vecteurs.extend(ollama.vectoriser(conf["modele_embeddings"], [p["texte"] for p in lot]))
        print(f"  {min(debut + TAILLE_LOT, len(passages))}/{len(passages)} passages", end="\r")
    print()
    matrice = np.asarray(vecteurs, dtype=np.float32)
    matrice /= np.linalg.norm(matrice, axis=1, keepdims=True)
    config.DONNEES.mkdir(exist_ok=True)
    np.save(config.FICHIER_VECTEURS, matrice)
    with open(config.FICHIER_PASSAGES, "w", encoding="utf-8") as sortie:
        for passage in passages:
            sortie.write(json.dumps(passage, ensure_ascii=False) + "\n")


def charger() -> tuple[np.ndarray, list[dict]]:
    matrice = np.load(config.FICHIER_VECTEURS)
    with open(config.FICHIER_PASSAGES, encoding="utf-8") as entree:
        passages = [json.loads(ligne) for ligne in entree]
    return matrice, passages


def chercher(conf: dict, matrice: np.ndarray, passages: list[dict], question: str) -> list[dict]:
    """Les k passages les plus proches de la question (similarité cosinus)."""
    vecteur = np.asarray(ollama.vectoriser(conf["modele_embeddings"], [question])[0], dtype=np.float32)
    vecteur /= np.linalg.norm(vecteur)
    scores = matrice @ vecteur
    meilleurs = np.argsort(-scores)[: conf["passages_par_question"]]
    return [{**passages[i], "score": float(scores[i])} for i in meilleurs]
