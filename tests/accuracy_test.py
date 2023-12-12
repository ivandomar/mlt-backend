from classification.Dataset import Dataset
from classification.SVMClassificator import SVMClassificator
from classification.Evaluator import Evaluator

def test_svm_accuracy():
    dataset = Dataset('../assets/golden_dataset.csv')
    dataset.load(['gender', 'age', 'city_zone', 'mother_education', 'father_education', 'educational_support', 'private_classes', 'internet', 'dating', 'free_time', 'friends', 'alcohol_business_days', 'alcohol_weekend', 'outcome'])

    data = dataset.get()
    X = data.iloc[:, 0:-1]
    Y = data.iloc[:, -1]

    model = SVMClassificator()
    model.load('../assets/classificator.pkl')

    evaluator = Evaluator(model)
    accuracy = evaluator.accuracy(X, Y)

    assert accuracy >= 0.75