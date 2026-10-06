# Résultats de l'évaluation

Modèle de génération : `Qwen2.5-7B-Instruct-abliterated-GGUF:latest` · embeddings : `bge-m3` · 1202 passages · 4 passages par question · seuil 0.5

| Mode | Bonne page retrouvée | Questions de cours répondues | Pièges refusés |
|---|---|---|---|
| naif | 7/8 | 8/8 | 0/6 |
| strict | 7/8 | 8/8 | 6/6 |

## À quoi sert la phase package de Maven ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.605 · premier passage : Generation d'application d'entreprise, page 8 · bonne page retrouvée : oui

> La phase package de Maven sert à créer un package de l'application, généralement sous forme de fichier `.jar`, `.war` ou `.ear`. Ce package contient les classes compilées, les ressources nécessaires et les dépendances, prêt pour le déploiement.

**strict** — réponse · meilleur score 0.605 · premier passage : Generation d'application d'entreprise, page 8 · bonne page retrouvée : oui

> La phase package de Maven sert à créer un package (un fichier « .jar », « .war », « .ear »). [1]

## Quelle est la différence entre la fragmentation horizontale et la fragmentation verticale dans une base de données répartie ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.642 · premier passage : Base de donnee repartis, page 29 · bonne page retrouvée : non

> La fragmentation horizontale et la fragmentation verticale sont deux types de fragmentation utilisés dans les bases de données réparties, chacune ayant des approches et des impacts différents :
> 
> 1. Fragmentation horizontale :
>    - Divise la table en sous-ensembles (fragments) basés sur une clé de partition.
>    - Chaque fragment contient des enregistrements entiers.
>    - Optimise les requêtes qui filtre sur la clé de partition.
>    - Exemple : partitionner une table de ventes par année ou par région.
> 
> 2. Fragmentation verticale :
>    - Divise la table en sous-ensembles en séparant les attributs en fragments.
>    - Chaque fragment contient une partie des attributs de la table.
>    - Optimise les requêtes qui utilisent uniquement certains attributs.
>    - Exemple : séparer les attributs de détails de commande et de détails de produit dans une table de commande.
> 
> La fragmentation verticale est généralement utilisée pour réduire la taille des enregistrements et optimiser les requêtes, tandis que la fragmentation horizontale est utilisée pour répartir les données de manière plus é

**strict** — réponse · meilleur score 0.642 · premier passage : Base de donnee repartis, page 29 · bonne page retrouvée : non

> La fragmentation horizontale consiste à diviser une table en plusieurs parties horizontales, c'est-à-dire en plusieurs sous-tables contenant des ensembles de lignes. En revanche, la fragmentation verticale divise une table en plusieurs parties verticales, c'est-à-dire en plusieurs sous-tables contenant des ensembles d'attributs. [2] [4]

## Quels sont les inconvénients de l'approche base de données répartie ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.658 · premier passage : Base de donnee repartis, page 7 · bonne page retrouvée : oui

> Les inconvénients de l'approche base de données répartie mentionnés dans l'extrait sont :
> 
> - Administration complexe
> - Complexité de mise en œuvre 
> - Distribution du contrôle
> - Surcharge (l'échange de messages augmente le temps de calcul)
> 
> Ces points soulignent les défis opérationnels et techniques liés à la gestion et au déploiement d'une base de données répartie.

**strict** — réponse · meilleur score 0.658 · premier passage : Base de donnee repartis, page 7 · bonne page retrouvée : oui

> Les inconvénients de l'approche base de données répartie incluent une administration complexe, une complexité de mise en œuvre, une distribution du contrôle et une surcharge due à l'échange de messages qui augmente le temps de calcul [1].

## Qu'est-ce qu'une API REST ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.776 · premier passage : Technologies cloud, page 48 · bonne page retrouvée : oui

> Une API REST (Representational State Transfer) est un type d'architecture d'API qui fournit un certain nombre de normes à respecter pour faciliter la communication entre applications. Elle permet l'interaction entre différentes applications et est une interface entre le client et le serveur pour récupérer des données. Elle utilise des URL couplées à des requêtes HTTP.

**strict** — réponse · meilleur score 0.776 · premier passage : Technologies cloud, page 48 · bonne page retrouvée : oui

> Une API REST est un type d'architecture d'API qui fournit un certain nombre de normes et de conventions à respecter pour faciliter la communication entre applications. Les APIs qui respectent le standard REST sont appelées API REST ou API RESTful [1]. Une API est une interface permettant l'interaction entre différentes applications [2].

## Quelles sont les deux collections les plus utilisées en Dart ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.568 · premier passage : Dvplt d'applications mobiles, page 18 · bonne page retrouvée : oui

> En Dart, les deux collections les plus utilisées sont les Listes et les Maps. Les Listes sont des collections où chaque élément est associé à un index, tandis que les Maps fonctionnent sur un ensemble clé/valeur.

**strict** — réponse · meilleur score 0.568 · premier passage : Dvplt d'applications mobiles, page 18 · bonne page retrouvée : oui

> Les deux collections les plus utilisées en Dart sont les Listes et les Maps. [1]

## Qu'est-ce qu'une fonction fléchée en Dart ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.639 · premier passage : Dvplt d'applications mobiles, page 31 · bonne page retrouvée : oui

> Une fonction fléchée en Dart, également appelée fonction Lambda, est une fonction courte et concise. Elle ressemble aux fonctions classiques mais utilise une syntaxe plus courte où les accolades sont remplacées par `⇒`. Elle ne contient pas de mot-clé `return` et retourne automatiquement la valeur de l'expression.

**strict** — réponse · meilleur score 0.639 · premier passage : Dvplt d'applications mobiles, page 31 · bonne page retrouvée : oui

> Une fonction fléchée en Dart est similaire aux fonctions classiques mais utilise une syntaxe plus courte. Elle ne contient pas le mot-clé return et utilise =⇒ à la place des accolades. [1]

## Quel document sort de l'étude préalable d'un projet, et qui le valide ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.651 · premier passage : Divers, page 8 · bonne page retrouvée : oui

> Un document appelé "Note de cadrage (Rapport d'étude préalable)" sort de l'étude préalable d'un projet. Ce document est validé par le comité de pilotage.

**strict** — réponse · meilleur score 0.651 · premier passage : Divers, page 8 · bonne page retrouvée : oui

> Un document appelé "Note de cadrage (Rapport d'étude préalable)" sort de l'étude préalable d'un projet. Ce document est validé par le comité de pilotage [1].

## Par quoi commence un schéma XML ?

Type : dans-les-cours

**naif** — réponse · meilleur score 0.733 · premier passage : xml, page 6 · bonne page retrouvée : oui

> Un schéma XML commence par un prologue qui indique la version et l'encodage du document, suivie d'un élément racine `xsd:schema`. Par exemple :
> 
> ```xml
> <?xml version="1.0" encoding="ISO-8859-1"?>
> <xsd:schema xmlns:xsd="http://www.w3.org/2000/10/XMLSchema">
>     <!-- Déclarations d'éléments, d'attributs et de types ici -->
> </xsd:schema>
> ```
> 
> Cet élément racine `xsd:schema` fait référence à la recommandation du W3C pour le langage de définition de schéma XML (XSD).

**strict** — réponse · meilleur score 0.733 · premier passage : xml, page 6 · bonne page retrouvée : oui

> Un schéma XML commence par un prologue, et a un élément racine. [1]

## Comment déployer une application avec Docker Compose ?

Type : piege-hors-cours

**naif** — réponse · meilleur score 0.541 · premier passage : Divers, page 29

> Le déploiement d'une application avec Docker Compose consiste à utiliser un fichier `docker-compose.yml` pour définir et exécuter les conteneurs Docker nécessaires à l'application. Voici les étapes principales :
> 
> 1. Créer un fichier `docker-compose.yml` pour définir les services et leurs configurations.
> 2. Exécuter la commande `docker-compose up` pour démarrer les conteneurs définis dans le fichier.
> 
> Cela permet un déploiement fluide et contrôlé de l'application dans un environnement Docker.

**strict** — refus · meilleur score 0.541 · premier passage : Divers, page 29

> Je ne trouve pas cela dans les cours fournis.

## Qu'est-ce qu'un Operator dans Kubernetes ?

Type : piege-hors-cours

**naif** — réponse · meilleur score 0.504 · premier passage : secure, page 36

> Les extraits de cours fournis ne contiennent pas d'informations directes sur les opérateurs dans Kubernetes. Cependant, en se basant sur le contexte et la terminologie utilisée en informatique et en particulier en gestion d'infrastructure cloud, un opérateur dans Kubernetes est un type de ressource de gestion personnalisée qui permet de gérer des applications complexes en les décomposant en étapes simples et répétables. Il s'agit d'un concept introduit par Kubernetes pour faciliter la gestion et l'automatisation des applications et des processus de vie cycle dans un cluster Kubernetes.

**strict** — refus · meilleur score 0.504 · premier passage : secure, page 36

> Je ne trouve pas cela dans les cours fournis.

## Comment fonctionne le protocole MQTT ?

Type : piege-hors-cours

**naif** — réponse · meilleur score 0.484 · premier passage : secure, page 35

> Le protocole MQTT (Message Queuing Telemetry Transport) est un protocole de messagerie asynchrone basé sur le modèle pub/sub. Il est conçu pour des applications de bas bande passante et de faible latence, comme la surveillance des objets connectés (IoT).
> 
> Voici comment il fonctionne de manière concise :
> 
> 1. **Architecture Pub/Sub** : Les clients MQTT se connectent à un serveur de messagerie (broker) et peuvent s'abonner à des sujets (topics) ou publier des messages sur des sujets.
> 
> 2. **Connexion** : Le client MQTT établit une connexion sécurisée (optionnellement TLS/SSL) avec le broker MQTT.
> 
> 3. **Publication et Abonnement** : Les clients peuvent publier des messages sur des sujets et s'abonner à des sujets pour recevoir des messages.
> 
> 4. **Qualité de Service** : MQTT offre trois niveaux de qualité de service (QoS) pour garantir la livraison des messages :
>    - QoS 0 : Livraison non garantie (uniquement en mode pub/sub).
>    - QoS 1 : Livraison garantie (confirmation de livraison).
>    -

**strict** — refus · meilleur score 0.484 · premier passage : secure, page 35

> Je ne trouve pas cela dans les cours fournis.

## Quelle est la différence entre REST et GraphQL ?

Type : piege-proche

**naif** — réponse · meilleur score 0.575 · premier passage : Technologies cloud, page 48

> REST (Representational State Transfer) et GraphQL sont deux approches différentes pour interagir avec des services web, mais ils ont des différences notables :
> 
> 1. **REST** :
>    - Fournit une architecture basée sur des ressources.
>    - Utilise des méthodes HTTP standard (GET, POST, PUT, DELETE) pour interagir avec des ressources.
>    - Les données sont généralement structurées en JSON et retournées dans des entités distinctes.
>    - Les requêtes REST sont souvent plus granulaires et peuvent être combinées pour obtenir des informations complètes.
> 
> 2. **GraphQL** :
>    - Permet de demander exactement les données dont on a besoin.
>    - Utilise une seule requête pour obtenir toutes les données nécessaires, ce qui peut réduire le nombre de requêtes HTTP.
>    - Offre plus de flexibilité car les clients peuvent spécifier exactement les champs qu'ils souhaitent recevoir.
>    - Les données sont retournées sous forme d'un seul objet JSON.
> 
> En résumé, REST est plus orienté vers une architecture de ressources et des requêtes granulaires, tandis que GraphQL offre plus de flexibilité et

**strict** — refus · meilleur score 0.575 · premier passage : Technologies cloud, page 48

> Je ne trouve pas cela dans les cours fournis.

## À quoi sert la phase optimize de Maven ?

Type : piege-proche

**naif** — réponse · meilleur score 0.513 · premier passage : Introduction a l'IA, page 14

> La phase optimize de Maven n'est pas explicitement mentionnée dans les extraits fournis. Cependant, en analysant les phases disponibles, on peut voir que la phase "verify" est destinée à lancer des tests pour vérifier la validité du package. Cette phase pourrait être considérée comme une phase d'optimisation indirecte, car elle vise à s'assurer que le package est valide et fonctionnel avant son déploiement.

**strict** — refus · meilleur score 0.513 · premier passage : Introduction a l'IA, page 14

> Je ne trouve pas cela dans les cours fournis.

## Quel est le prix d'une licence Oracle 19c ?

Type : piege-proche

**naif** — réponse · meilleur score 0.579 · premier passage : Administration de base de donnee, page 8

> L'information sur le prix d'une licence Oracle 19c n'est pas fournie dans les extraits de cours fournis. Ces extraits de cours se concentrent plutôt sur les fonctionnalités et l'historique d'Oracle 19c, et ne contiennent pas de détails sur les coûts de licence. Pour obtenir cette information, il faudrait consulter la documentation officielle d'Oracle ou contacter leur service commercial.

**strict** — refus · meilleur score 0.579 · premier passage : Administration de base de donnee, page 8

> Je ne trouve pas cela dans les cours fournis.
