import pickle
import numpy as np

class LinearClassifier:
    def __init__(self):
        self.model = pickle.load(open("./MachineLearning/linearSVC/linearSVC_model.pkl", 'rb'))
        self.preprocessor = pickle.load(open("./MachineLearning/linearSVC/linearSVC_preprocessor.pkl", 'rb'))
        self.transformer = pickle.load(open("./MachineLearning/linearSVC/linearSVC_tfidfTransformer.pkl", 'rb'))
        self.classes = {0: 'Appetizer or side dish', 1: 'Dessert', 3: 'Main course', 2: 'Drinks', 4: 'Other'}

    def predict(self, text):
        processed = self.preprocessor.transform([text])
        transformed = self.transformer.transform(processed)
        prediction = self.model.predict(transformed)[0]
        return self.classes[prediction]