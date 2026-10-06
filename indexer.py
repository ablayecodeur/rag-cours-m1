"""Étape 1 — lit les PDF du corpus, les découpe et calcule les vecteurs.
Usage : python indexer.py"""
from rag import config, corpus, index

conf = config.charger()
print("Lecture des PDF…")
passages = corpus.extraire_passages(conf)
print(f"{len(corpus.fichiers_du_corpus(conf))} fichiers, {len(passages)} passages")
print(f"Calcul des vecteurs avec {conf['modele_embeddings']}…")
index.construire(conf, passages)
print(f"Index écrit dans {config.DONNEES}")
