from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC


class SVM:
    """ Modèle SVM pour prendre en charge la détection de commentaires Troll en ligne

    Attributs
    ----------
    description : string, model description pour referencer les parametres d' object

    clf : objet sklearn svm model

    """

    def __init__(self, description):
        """ Initialisation de la configuration

        Parameters
        --------------
            data: (dict) dictionnaire d'entrainements et de tests de set de données 
            description: (str) description du model en entrainement
        """
        self.description = description
        self.clf = LinearSVC()

    def train(self, data, **params):
        """ Entrainement du model avec GRidSearch sur les paramètres que nous avons défini

        Parametres
        -------------
            parametres: (dict) paire de clé valeur specifiant le parametre de recherche sklearn

        """

        self.clf = GridSearchCV(self.clf, params, cv=5)
        self.clf.fit(data['X_train'], data['y_train'])

    def display_results(self, data):
        """ Imprime les précisions de test et d'entrainement avec d'autres modèles
            métriques de validation.

        Parametres
        ---------------
            clf: (scikit-learn model) modèle prédictif à tester
            data: (dict) entrainement et test de données pour le model
        """
        train_accuracy = self.clf.score(data['X_train'], data['y_train'])
        test_accuracy = self.clf.score(data['X_test'], data['y_test'])
        y_pred = self.clf.predict(data['X_test'])
        print('{:>20s} {:.2f}'.format('Train Accuracy:', train_accuracy))
        print('{:>20s} {:.2f}'.format('Test Accuracy:', test_accuracy))
        print(confusion_matrix(data['y_test'], y_pred))