# RAG sur mes cours

Un assistant qui répond à des questions à partir de mes supports de cours de
Master Systèmes d'Information, et qui cite la page d'où vient chaque réponse.
Tout tourne en local avec [Ollama](https://ollama.com) : aucun document n'est
envoyé à un service extérieur.

Le projet existe en deux versions, pour pouvoir les comparer sur les mêmes
questions :

- **naïve** : on donne au modèle les passages trouvés et on lui demande de
  répondre ;
- **stricte** : si aucun passage n'est assez proche de la question, le modèle
  n'est pas appelé ; sinon il doit s'en tenir aux extraits et les citer.

> Le corpus n'est pas dans ce dépôt. Les supports de cours appartiennent à mes
> enseignants : ils restent sur ma machine, ainsi que l'index qui en dérive
> (dossier `donnees/`, ignoré par Git).

## Comment ça marche

| Étape | Fichier | Ce qui se passe |
|---|---|---|
| Découper | `rag/corpus.py` | Les cours sont des diapositives : une page devient un passage, ce qui permet de citer « tel cours, page 12 » |
| Vectoriser | `rag/index.py` | Chaque passage devient un vecteur, avec le modèle d'embeddings `bge-m3` |
| Chercher | `rag/index.py` | Similarité cosinus : les 4 passages les plus proches de la question |
| Répondre | `rag/repondre.py` | Un modèle de langage local répond à partir de ces passages |

Il n'y a pas de base vectorielle. L'index est un tableau NumPy : sur mes
1 202 passages, une recherche prend moins d'une milliseconde, et chaque étape
reste lisible.

## Résultats de l'évaluation

Évaluation du 6 octobre 2026 : 37 PDF, 1 202 passages, 14 questions
(`evaluation/questions.json`), dont 8 dont la réponse est dans les cours et
6 pièges dont la réponse n'y figure pas.

| Version | Bonne page retrouvée | Questions de cours répondues | Pièges écartés |
|---|---|---|---|
| naïve | 7/8 | 8/8 | 1/6 |
| stricte | 7/8 | 8/8 | 6/6 |

Ce que la lecture des réponses montre (`evaluation/resultats.md`) :

- **La version naïve a répondu à 5 pièges sur 6.** Trois fois sans prévenir
  (Docker Compose, MQTT, GraphQL), deux fois après avoir écrit que ce n'était
  pas dans les extraits. Ces sujets n'apparaissent dans aucun passage : le
  modèle a répondu de mémoire.
- **Le seuil de pertinence n'a arrêté qu'un piège sur six.** Les pièges
  obtiennent entre 0,48 et 0,58 de similarité, les questions de cours entre
  0,57 et 0,78 : les deux plages se chevauchent. Les cinq autres refus de la
  version stricte viennent de la consigne donnée au modèle.

Le tableau de `evaluation/resultats.md` affiche « 0/6 » pièges refusés pour la
version naïve : le script ne compte que la phrase de refus exacte. Une des six
réponses décline bien la question, avec d'autres mots, d'où le « 1/6 »
ci-dessus.

## Limites

- 14 questions seulement, écrites par moi : c'est un premier test, pas une
  mesure.
- Un seul modèle de génération a été évalué : une variante communautaire
  « abliterated » de Qwen 2.5 7B (GGUF), qui était déjà sur ma machine. Les
  résultats ne valent que pour ce montage ; `config.exemple.json` propose le
  modèle officiel `qwen2.5:7b`.
- L'exactitude des réponses données hors des cours n'a pas été vérifiée.
- Sans carte graphique, une réponse prend une à deux minutes.
- Pas d'interface : tout se fait en ligne de commande.

## Rejouer chez soi

Il faut Python 3.12, Ollama, et un dossier de PDF à interroger.

```bash
ollama pull bge-m3
ollama pull qwen2.5:7b

python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

cp config.exemple.json config.local.json   # puis indiquer le dossier des PDF

.venv/bin/python indexer.py                             # 1. découper et vectoriser
.venv/bin/python demander.py "Qu'est-ce qu'une API REST ?"          # 2. version stricte
.venv/bin/python demander.py "Qu'est-ce qu'une API REST ?" --naif   #    version naïve
.venv/bin/python evaluer.py                             # 3. comparer les deux versions
```

Les questions de `evaluation/questions.json` portent sur mes cours : pour un
autre corpus, il faut écrire les siennes, pièges compris.
