import pandas as pd

class Dataset:
    __url = None
    __dataset = None

    def __init__(self, url: str):
        self.__url = url

    # loads CSV into instance dataset
    def load(self, attributes: list):
        self.__dataset = pd.read_csv(self.__url, names=attributes)

    # returns data from dataset
    def get(self):
        return self.__dataset