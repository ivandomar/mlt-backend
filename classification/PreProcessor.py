from sklearn.model_selection import train_test_split

class PreProcessor:
    __x_train = None
    __x_test = None
    __y_train = None
    __y_test = None

    def __setup_holdout(self, dataset, test_rate, seed):
        my_data = dataset.values
        X = my_data[:, 0:-1]
        Y = my_data[:, -1]

        return train_test_split(X, Y, test_size=test_rate, random_state=seed)

    # setups entire classification training resources
    def run(self, dataset, test_rate, seed=7):
        # divisão em treino e teste
        self.__x_train, self.__x_test, self.__y_train, self.__y_test = self.__setup_holdout(
            dataset,
            test_rate,
            seed
        )

    def x_train(self):
        return self.__x_train

    def x_test(self):
        return self.__x_test

    def y_train(self):
        return self.__y_train

    def y_test(self):
        return self.__y_test