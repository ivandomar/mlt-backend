from sklearn.metrics import accuracy_score

class Evaluator:
    __classificator = None


    def __init__(self, classificator):
        self.__classificator = classificator

    def accuracy(self, X_test, Y_test):
        predicoes = self.__classificator.predict(X_test)
        
        return accuracy_score(Y_test, predicoes)