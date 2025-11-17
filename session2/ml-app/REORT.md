Rapport du Projet DevOps
Ce document décrit les étapes suivies pour compléter l'assignment DevOps, de l'exécution locale à la mise en place d'un pipeline CI/CD avec GitHub Actions et Docker. 

Tâche 2 : Exécution de l'application localement
L'objectif de cette tâche était de configurer l'environnement de développement local et de vérifier que l'application de Machine Learning fonctionne comme prévu avant de l'automatiser. 

1. Préparation de l'environnement
Pour garantir un environnement de travail propre et isolé, j'ai suivi les étapes suivantes :


Création d'un environnement virtuel : J'ai créé un environnement virtuel dédié au projet en utilisant une version spécifique de Python (Python 3.11) pour éviter les conflits de dépendances. 

Bash

python3.11 -m venv .venv

Activation de l'environnement : J'ai ensuite activé cet environnement. 

Bash

source .venv/bin/activate

Installation des dépendances : Une fois l'environnement activé, j'ai installé toutes les bibliothèques requises (telles que scikit-learn, pandas, etc.) listées dans le fichier requirements.txt. 

Bash

pip install -r requirements.txt
2. Exécution des scripts de l'application
J'ai exécuté les deux scripts principaux de l'application pour confirmer son bon fonctionnement :

A. Entraînement du modèle (src/train.py) 

J'ai d'abord lancé le script d'entraînement. Ce script effectue les actions suivantes :

Charge le jeu de données "Iris".

Divise les données en ensembles d'entraînement et de test.

Entraîne un modèle de régression logistique.

Affiche un rapport de classification et une précision (Accuracy).

Sauvegarde le modèle entraîné dans models/iris_classifier.pk.

Sauvegarde les graphiques d'évaluation (confusion_matrix.png, feature_importance.png).

Preuve d'exécution (Entraînement) : La capture d'écran ci-dessous montre la sortie du terminal après l'exécution de python src/train.py. On y voit le rapport de classification (Accuracy de 0.9667) et les messages confirmant la sauvegarde du modèle et des graphiques.

B. Exécution des prédictions (src/predict.py)

Pour m'assurer que le modèle sauvegardé était fonctionnel, j'ai exécuté le script de prédiction. Ce script charge le fichier .pk et l'utilise pour prédire la classe de trois exemples de fleurs Iris.

Preuve d'exécution (Prédiction) : Cette capture d'écran montre la sortie de python src/predict.py. Le modèle est chargé avec succès et fournit des prédictions correctes (setosa, virginica, versicolor) pour les trois exemples, validant ainsi l'ensemble du processus local.

(Fin de la section pour la Tâche 2)

Vous pouvez maintenant continuer avec la Tâche 3 (Tests unitaires). Vous pouvez ajouter une nouvelle section à ce fichier dès que vous l'aurez terminée.