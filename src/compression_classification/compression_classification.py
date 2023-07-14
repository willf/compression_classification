
import zlib

from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin


class CompressionClassifier(BaseEstimator, ClassifierMixin):

    def __init__(self):
        self.models = {}

    def fit(self, X, y=None):
        for x_val, y_val in zip(X, y):
            model = self.models.get(y_val, None)
            if model is None:
                model = zlib.compressobj()
                self.models[y_val] = model
            for x in x_val:
                model.compress(str(x).encode())


    def predict(self, X, y=None):
        # make a shallow copy of the models
        copies = self.models.copy()
        for key in copies.keys():
            copies[key] = self.models[key].copy()
        # compress the data
        for x_val in X:
            for key in copies.keys():
                for x in x_val:
                    copies[key].compress(str(x).encode())
        # flush the copies and get lengths
        results = [(key, len(copies[key].flush())) for key in copies.keys()]
        # return the key with the smallest length
        return min(results, key=lambda x: x[1])[0]

    def predict_proba(self, X, y=None):
        raise NotImplementedError("CompressionClassifier does not support predict_proba")

    def train_with_examples(self, example_dict):
        for key, value in example_dict.items():
            self.fit([value], [key])

    def predict_text(self, text):
        return self.predict([text])
