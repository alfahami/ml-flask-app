# STack Overflow Survey 2019 - ML Flask Web app

# Sommaire

 * [Analyse des résultats du Stack Overflow Survey 2019](#stack-overflow)
      1. [Présentation des données](#presentation) 
      2. [Résumé d'analyse des résultats](#resume-resultat)
      3. [Données et code](#code-donnees)
      4. [Prérequis](#prerequis)
      5. [Instructions d'exécution](instructions)
 * [Machine Learning Flask app](#ml-flask-app)
      1. [Objectif de l'application](#objectif)
      2. [Installtion et exécution](#installation)
 * [Structure du projet](#repository)
      1. [Présentation](#projet-presentation)
      2. [Détails](#details)

## Analyse des resultats du Stack Overflow Survey 2019 <a name="stack-overflow"></a>
  1. ### Présentation des données <a name="presentation"></a>
<p align="justify">
Avec près de 90 000 réponses provenant de plus de 170 pays et territoires dépendants, le sondage Stack Overflow Annual Developer Survey continue d'être le sondage le plus complet jamais réalisée auprès des développeurs de logiciels. Le sondage couvre des aspects tels que la satisfaction professionnelle et la recherche d'emploi dans les langages de programmation...etc<br>
Inline-style: 
![alt text](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/screen/salaries_pour_data_science_usa.png "Salaire des datascientists auw USA")
Les données du sondage peuvent être télécharger [2019 Stack Overflow Survey results](https://insights.stackoverflow.com/survey)<br>
Dans ce projet, les résultats du sondage seront utilisées pour répondre aux questions suivantes pour les aspirants scientifiques des données (data scientists):
</p>

  * Quel est le langage de programmation de votre choix?
  * Quel est le salaire des développeurs?
  * Quel est le framework de choix numéro un pour les développeurs?

  2. ### Resumé des résultats <a name="resume-resultat"></a>
<p align="justify">
Après avoir analysé les données, nous constatons que python est le langage de programmation de choix pour les développeurs qui s'identifient en tant que Data Scientists et Machine Learning Specialist. Les salaires des Data Scientists et Machine Learning Specialist sont les plus élevés des États-Unis. Étonnamment, jQuery est le framework web de choix.

  3. ### Données et code <a name="code-donnees"></a>
L'analyse principale est contenue dans le fichier jupyter notebook [sof-dataviz.ipynb](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/model_dev/sof-dataviz.ipynb). Toutes les fonctions et le code, ainsi que la justification des décisions prises, sont contenus dans ce fichier notebook.

  4. ### Prérequis <a name="prerequis"></a>
   * Jupyter Notebook
   * Numpy
   * Pandas
   * Seaborn
   * Matplotlib
    
  5. ### Instruction d'exécution
Téléchargez les de données requis ainsi que les bibliothèques requis, si nécessaire, modifiez les chemins de répertoire.
Téléchargez le [fichier notebook](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/model_dev/sof-dataviz.ipynb) et exécutez le avec jupyter notebook
</p>

## Machine Learning Flask web app <a name="ml-flask-app"></a>
  1. ### Objectif de l'application <a name="objectif"></a>
<p align="justify">
Application Web conçue pour montrer la structure du projet pour un modèle d'apprentissage automatique déployé à l'aide de flask. Ce projet comprend un modèle d'apprentissage automatique qui a été formé pour détecter si un commentaire en ligne est un <i>Cyber Troll</i> ou <i>non Cyber-Troll</i>. Cette application agit comme une interface permettant à un utilisateur de soumettre de nouvelles requêtes. Le modèle d'apprentissage automatique a été construit à l'aide de diverses fonctionnalités de scikit learn:

    - Machine à vecteur de support (SVM)
    - Représentation textuelle Bag-of-Words (BoW)
    - Grid Search + Cross Validation

Chacun de ces composants est développé dans le projet dans un paramètre hors ligne à l'intérieur de `/ model_dev`. Les modèles SVM et BoW seront toujours nécessaires dans un cadre de production ou de test afin de pouvoir prédire les requêtes soumises par l'utilisateur, afin qu'ils puissent être sérialisés via la fonctionnalité de pickle de python et stockés dans le dossier `/model_assets`.

Afin de détecter si un commentaire en ligne provient ou non d'un cyber-troll, vous pouvez déployer cette application localement et soumettre des requêtes au modèle d'apprentissage automatique pour recevoir des prédictions via une interface utilisateur simple. Le modèle a été formé à l'aide du Dataset for Detection of Cyber-Trolls ([voir ici](https://dataturks.com/projects/abhishek.narayanan/Dataset-for-Detection-of-Cyber-Trolls)). 

Le fichier notebook du modèle se trouve [ici](https://github.com/alfahami/sof-dataviz_ml-flask-app/blob/master/model_dev/model_dev.ipynb).
</p>

   2. ### Installation <a name="installation"></a>
Premièrement, faites clone le repisitory localement\
`git clone git@github.com:alfahami/sof-dataviz_ml-flask-app.git`

Créer un nouvel environement virtuel python dans le dossier du projet\
`pyhton3 -m venv ./venv`

Activation de l'environement que nous vennons de créer\
`source /venv/bin/activate`

Installation des paquets python prérequis\
`pip install -r ./paquets-prerequis.txt`

Maintenant nous pouvons déployer l'application (Vous devez avoir flask déjà installé)\
`python app.py`

Naviguez vers `http://127.0.0.1:5000/` pour voir la page d'accueil de l'application
Vous pouvez soit visualizer le notebook du stackoverflow survey, soit utiliser le service de prédiction



Nous voyons bien que "**Get the fuck out here**" a été bien prédi comme commentaire troll

## Structure du projet <a name="repository"></a>
   1. ### Présentation <a name="projet-presentation"></a>
            sof-dataviz_ml-flask-app
            ├── model_assets
            │   ├── model_V0.pkl
            │   └── vectorizer_V0.pkl
            ├── model_dev
            │   ├── data
            │   |   └── cyber-troll.json
            │   |   └── survey_results_public.csv
            │   |   └── survey_results_schema.csv
            │   └── model_dev.ipynb
            │   └── sof-dataviz.ipynb
            │   └── BaseModel.py
            ├── templates
            │   └── index.html
            │   └── cyber-troll.html
            │   └── sof-dataviz.html
            ├── app.py
            ├── utils.py
            ├── paquets-prerequis.txt
            └── README.md

   2. ### Details <a name="details"></a>

`/model_assets` est utilisé pour stocker les états persistants du modèle prédictif et les extracteurs de fonctions apprises de scikit-learn.

`/model_dev` est utilisé comme le dossier contenant les modèles où un .ipynb est utilisé pour développer le modèle et enregistrer de nouvelles versions des états persistants.

Le stockage de nouveaux états persistants du modèle peut être effectué depuis jupyter notebook. Par exemple, dans model_dev.ipynb, je peux créer un nouveau modèle / recyclage et l'inclure dans le dossier `./model_assets` lorsque je suis satisfait de l'entrainement.

La sélection de la version des modèles à utiliser pendant l'exécution est choisie dans la fonction de requête POST à l'intérieur de `app.py.`

`/templates` contient les modèles html pour l'application.

### Auteur
[AL-FAHAMI TOIHIR](https://alfahami.github.io/ "View my resume")

[FACULTE DES SCIENCES - KENITRA](http://fs.uit.ac.ma/ "Site officiel de FSK")

DEPARTEMENT DE MATHEMATIQUES ET INFORMATIQUE

### Remerciements
Merci à Modingwa et W.M Gopar pour la clarté de leur blog post


**Licence**: Le projet est disponible en open source selon les termes de la licence MIT.

