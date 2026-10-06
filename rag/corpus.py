"""Du PDF au passage.

Les supports de cours sont des diapositives : chaque page porte une idée et
très peu de texte. Le découpage suit donc la page — c'est aussi ce qui permet
de citer une source précise (« fichier, page 12 »).
"""
import logging
import re
import warnings
from pathlib import Path

from pypdf import PdfReader

warnings.filterwarnings("ignore")
logging.getLogger("pypdf").setLevel(logging.CRITICAL)

LONGUEUR_MIN = 80  # en dessous, une page est un titre ou une image : inutile
LONGUEUR_MAX = 1200


def _nettoyer(texte: str) -> str:
    texte = texte.replace("\x00", " ")
    texte = re.sub(r"[ \t]+", " ", texte)
    texte = re.sub(r"\n\s*\n+", "\n", texte)
    return texte.strip()


def _decouper(texte: str) -> list[str]:
    """Quelques pages sont très longues (texte dense, code) : on les coupe
    par lignes entières pour garder des passages de taille comparable."""
    if len(texte) <= LONGUEUR_MAX:
        return [texte]
    morceaux, courant = [], ""
    for ligne in texte.split("\n"):
        if courant and len(courant) + len(ligne) + 1 > LONGUEUR_MAX:
            morceaux.append(courant)
            courant = ligne
        else:
            courant = f"{courant}\n{ligne}" if courant else ligne
    if len(courant) >= LONGUEUR_MIN:
        morceaux.append(courant)
    return morceaux


def fichiers_du_corpus(config: dict) -> list[Path]:
    dossier = Path(config["dossier_corpus"])
    exclure = [m.lower() for m in config.get("exclure", [])]
    exclure_exact = set(config.get("exclure_exact", []))
    retenus = []
    for chemin in sorted(dossier.rglob("*.pdf")):
        relatif = chemin.relative_to(dossier)
        nom = chemin.name.lower()
        # Un fichier posé à la racine du dossier et listé ici est un doublon.
        if len(relatif.parts) == 1 and chemin.name in exclure_exact:
            continue
        if any(motif in nom for motif in exclure):
            continue
        retenus.append(chemin)
    return retenus


def extraire_passages(config: dict) -> list[dict]:
    dossier = Path(config["dossier_corpus"])
    passages = []
    for chemin in fichiers_du_corpus(config):
        relatif = chemin.relative_to(dossier)
        cours = relatif.parts[0] if len(relatif.parts) > 1 else "Divers"
        try:
            lecteur = PdfReader(str(chemin))
        except Exception as erreur:  # PDF illisible : on le signale, on continue
            print(f"  ! illisible : {relatif} ({erreur})")
            continue
        for numero, page in enumerate(lecteur.pages, start=1):
            texte = _nettoyer(page.extract_text() or "")
            if len(texte) < LONGUEUR_MIN:
                continue
            for morceau in _decouper(texte):
                passages.append(
                    {
                        "id": len(passages),
                        "cours": cours,
                        "fichier": str(relatif),
                        "page": numero,
                        "texte": morceau,
                    }
                )
    return passages
