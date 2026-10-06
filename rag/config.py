"""Chargement de la configuration locale (jamais committée)."""
import json
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DONNEES = RACINE / "donnees"
FICHIER_PASSAGES = DONNEES / "passages.jsonl"
FICHIER_VECTEURS = DONNEES / "vecteurs.npy"


def charger() -> dict:
    chemin = RACINE / "config.local.json"
    if not chemin.exists():
        raise SystemExit(
            "config.local.json introuvable : copiez config.exemple.json et adaptez-le."
        )
    return json.loads(chemin.read_text(encoding="utf-8"))
