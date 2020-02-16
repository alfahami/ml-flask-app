# Stack Overflow Survey 2019 and Machine Learning flask Web app

<p align="justify">
Application Web conçue pour montrer la structure du projet pour un modèle d'apprentissage automatique déployé à l'aide de flask. Ce projet comprend un modèle d'apprentissage automatique qui a été formé pour détecter si un commentaire en ligne est un `Cyber-Troll` ou `non Cyber-Troll`. Cette application agit comme une interface permettant à un utilisateur de soumettre de nouvelles requêtes. Le modèle d'apprentissage automatique a été construit à l'aide de diverses fonctionnalités de scikit learn:

Machine à vecteur de support (SVM)\
Représentation textuelle Bag-of-Words (BoW)\
Grid Search + Cross Validation

Chacun de ces composants est développé dans le projet dans un paramètre hors ligne à l'intérieur de / model_dev. Les modèles SVM et BoW seront toujours nécessaires dans un cadre de production ou de test afin de pouvoir prédire les requêtes soumises par l'utilisateur, afin qu'ils puissent être sérialisés via la fonctionnalité de pickle de python et stockés dans le dossier / model_assets.

Afin de détecter si un commentaire en ligne provient ou non d'un cyber-troll, vous pouvez déployer cette application localement et soumettre des requêtes au modèle d'apprentissage automatique pour recevoir des prédictions via une interface utilisateur simple. Le modèle a été formé à l'aide du Dataset for Detection of Cyber-Trolls ([voir ici](https://dataturks.com/projects/abhishek.narayanan/Dataset-for-Detection-of-Cyber-Trolls)). 

Le fichier notebook du modèle se trouve [ici](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/model_dev/model_dev.ipynb).
</p>
