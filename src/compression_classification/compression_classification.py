from sklearn.base import BaseEstimator, ClassifierMixin


class CompressionClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self):
        self.models = {}

    def fit(self, X, y=None):
        pass

    def predict(self, X, y=None):
        pass

    def predict_proba(self, X, y=None):
        raise NotImplementedError(
            "CompressionClassifier does not support predict_proba"
        )
