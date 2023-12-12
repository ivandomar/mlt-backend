class Classificator:

    def load(self, model_file: str):
        raise NotImplementedError()

    def train(self, X_train, Y_train):
        raise NotImplementedError()
    
    def predict(self):
        raise NotImplementedError()
    