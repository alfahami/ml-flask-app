from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import pickle
import string
import json
import random
import os


def load_data(raw=None):
    """ Chargement des données de travail

    Parametres
    --------------
        raw: (bool) si Vrai, la fonction retourne un datatest nettoyé
        return (df) : retourne la data frame de données et ses étiquettes
    """
    raw_data = []
    with open('./data/cyber_data.json') as f:
        for line in f:
            raw_data.append(json.loads(line))

    labels = [int(d['annotation']['label'][0]) for d in raw_data] # liste d'entiers 0, 1 pour nos étiquettes
    text = [d['content'] for d in raw_data]                       # commentaire en texte
    data = {'text': text, 'label': labels}                        #dictionnaire de texte et de labels
    df = pd.DataFrame(data, columns=['text', 'label'])  # data frame brute

    if raw:
        return df
    else:
        df.text = df.text.apply(clean_text)
        return df


def clean_text(text):
    """ nettoyage du texte pour le model de prediction

    Parametres
    -------------
        text: (str) texte à nettoyer
        return (str) texte post-traité et nottoyé
    """
    lemmatizer = WordNetLemmatizer()
    punctuation = list(string.punctuation)
    punctuation.extend(['.', "’", ','])
    text = BeautifulSoup(text, 'html.parser').text
    filtered_text = ' '.join([word.lower() for word in text.split() if word not in stopwords.words('english')])
    filtered_text = ''.join([c for c in filtered_text if c not in punctuation])
    filtered_text = ''.join([c for c in filtered_text if not c.isdigit()])
    filtered_text = filtered_text.replace('-', ' ')
    filtered_text = ' '.join([lemmatizer.lemmatize(w) for w in filtered_text.split()])
    return filtered_text


def persist_model(clf, description):
    """ enregistrement des classifiers pickles dans le dossier /model_assets avec la convention de nommage: model_[description].pkl

    Parametres
    -------------
        clf: (obj) model scikit-learn entrainé
        description: (str) model version/descripteur
    """
    model_path = open(os.path.join(os.pardir, "model_assets/model_{}.pkl".format(description)), "wb")
    pickle.dump(clf, model_path)
    print('Model Sauvegardé.')


def build_encoder(text, count_vectorizer=None, tf_idf=None):
    """ Exctracteur de fonctionnalité de texte à partir d'un itérable de données dans le texte

    Parametres
    ---------------
        text: (list ou series) de texte de données à transformer
        count_vectorizer: (bool) Si `True` transforme en model BoW 
        tf_idf: (bool) Si `True` transforme en representation TF-IDF

    """

    if count_vectorizer:
        vectorizer = CountVectorizer()
        vectorizer.fit(text)
        return vectorizer

    if tf_idf:
        transformer = TfidfVectorizer()
        transformer.fit(text)
        return transformer


def persist_vectorizer(vectorizer, description):
    """ enregistre un bag-of-words vectorizer dans /model_assets avec la convention de nommage: vectorizer_[description].pkl

    Parametres
    -------------
        vectorizer: (obj) objet sickit-learn vectorizer 
        description: (str) vectorizer version/descripteur
    """
    vectorizer_path = open(os.path.join(os.pardir, "model_assets/vectorizer_{}.pkl".format(description)), "wb")
    pickle.dump(vectorizer, vectorizer_path)
    print('Vectorizer Sauvegardé.')


def sample_data(df, n):
    """ affiche n échantillons aléatoires (e.g commentaire en ligne et étiquette)

    Parameters
    -------------
        df: pandas DataFrame qui sera traité
         n: number d'échantillon à être generé

    """
    for label in set(df.label):
        subset = df[df.label == label]
        rand_idxs = [random.randint(0, subset.shape[0]) for _ in range(n)]
        for idx in rand_idxs:
            print('Label: {}\nIndex: {}\t{}\n'.format(subset.iloc[idx]['label'], idx, subset.iloc[idx]['text']))
