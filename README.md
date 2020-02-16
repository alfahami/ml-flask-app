# Stack Overflow Survey 2019 et Machine Learning flask Web app

## Analyse des resultats du Stack Overflow Survey 2019

<p align="justify">
Avec près de 90 000 réponses provenant de plus de 170 pays et territoires dépendants, le sondage Stack Overflow Annual Developer Survey continue d'être le sondage le plus complet jamais réalisée auprès des développeurs de logiciels. Le sondage couvre des aspects tels que la satisfaction professionnelle et la recherche d'emploi dans les langages de programmation...etc

Dans ce projet, les résultats du sondage seront utilisés pour répondre aux questions suivantes pour les aspirants scientifiques des données (data scientists):
</p>
  * Quel est le langage de programmation de votre choix?
  * Quel est le salaire des développeurs?
  * Quel est le framework de choix numéro un pour les développeurs?

### Resumé des résultats
<p align="justify">
Après avoir analysé les données, nous constatons que python est le langage de programmation de choix pour les développeurs qui s'identifient en tant que Data Scientists et Machine Learning Specialist. Les salaires des Data Scientists et Machine Learning Specialist sont les plus élevés des États-Unis. Étonnamment, jQuery est le framework web de choix.

Pour plus de détails, référez-vous à l'analyse complète [ici](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/model_dev/sof-dataviz.ipynb).
</p>

## Machine Learning Flask web app
<p align="justify">
Application Web conçue pour montrer la structure du projet pour un modèle d'apprentissage automatique déployé à l'aide de flask. Ce projet comprend un modèle d'apprentissage automatique qui a été formé pour détecter si un commentaire en ligne est un `Cyber-Troll` ou `non Cyber-Troll`. Cette application agit comme une interface permettant à un utilisateur de soumettre de nouvelles requêtes. Le modèle d'apprentissage automatique a été construit à l'aide de diverses fonctionnalités de scikit learn:

Machine à vecteur de support (SVM)\
Représentation textuelle Bag-of-Words (BoW)\
Grid Search + Cross Validation

Chacun de ces composants est développé dans le projet dans un paramètre hors ligne à l'intérieur de / model_dev. Les modèles SVM et BoW seront toujours nécessaires dans un cadre de production ou de test afin de pouvoir prédire les requêtes soumises par l'utilisateur, afin qu'ils puissent être sérialisés via la fonctionnalité de pickle de python et stockés dans le dossier / model_assets.

Afin de détecter si un commentaire en ligne provient ou non d'un cyber-troll, vous pouvez déployer cette application localement et soumettre des requêtes au modèle d'apprentissage automatique pour recevoir des prédictions via une interface utilisateur simple. Le modèle a été formé à l'aide du Dataset for Detection of Cyber-Trolls ([voir ici](https://dataturks.com/projects/abhishek.narayanan/Dataset-for-Detection-of-Cyber-Trolls)). 

Le fichier notebook du modèle se trouve [ici](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/model_dev/model_dev.ipynb).
</p>

## Installation 
Premièrement, faites clone le repisitory localement\
`git clone git@github.com:alfahami/sof-dataviz_ml-flask-app.git`

Créer un nouvel environement virtuel python dans le dossier du projet\
`pyhton3 -m venv ./venv`

Activation de l'environement que nous vennons de créer\
`source /venv/bin/activate`

Installation des paquets python prérequis\
`pip install -r paquets-prerequis.txt`

Maintenant nous pouvons déployer l'application (Vous devez avoir flask déjà installé)\
`python app.py`

Naviguez vers `http://127.0.0.1:5000/` pour voir la page d'accueil de l'application
Vous pouvez soit visualizer le notebook du stackoverflow survey, soit utiliser le service de prédiction
[image goes here]

Nous essayons de prédire le commentaire : "Get the fuck out here"

