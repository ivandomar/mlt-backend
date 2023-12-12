from sklearn.svm import SVC
from Classificator import Classificator

class SVMClassificator(Classificator, SVC):

    def __init__(self):
        super().__init__()

    def train(self, X_train, Y_train):
        self.fit(X_train, Y_train)

    def predict(self, X):
        return self.predict(X)