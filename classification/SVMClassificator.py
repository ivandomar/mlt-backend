import pickle
from .Classificator import Classificator

class SVMClassificator(Classificator):
    __model = None

    def __init__(self):
        super().__init__()

    def load(self, model_file: str):
        pickle_input = open(model_file, 'rb')
        self.__model = pickle.load(pickle_input)
        pickle_input.close()

    def train(self, X_train, Y_train):
        self.fit(X_train, Y_train)

    def predict(self, X):
        return self.predict(X)