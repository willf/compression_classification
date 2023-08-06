import itertools

from nltk.lm import KneserNeyInterpolated
from nltk.lm.preprocessing import padded_everygram_pipeline

# Ok, next pass is to forget using Pandas and just have
# a list of sentences. I'm not sure I'm ever going to
# get this to work with Pandas. I'm not sure I need to.!


def flatten(list_of_lists):
    return list(itertools.chain.from_iterable(list_of_lists))


def tokenize(text):
    return [list(sentence) for sentence in text.split("\n")]


def readtext(path):
    with open(path) as f:
        return f.read()


class CompressionClassifier:
    def __init__(self, n=4):
        self.models = {}
        self.n = n

    def train(self, text, label):
        model = KneserNeyInterpolated(self.n)
        self.models[label] = model
        tokenized = tokenize(text)
        train, vocab = padded_everygram_pipeline(self.n, tokenized)
        model.fit(train, vocab)

    def perplexities(self, text):
        tokenized = tokenize(text)
        perplexity_values = {}
        classes = list(self.models.keys())
        for c in classes:
            model = self.models[c]
            perprlexity = model.perplexity(tokenized)
            perplexity_values[c] = perprlexity
        return perplexity_values

    def predict(self, text):
        perplexities = self.perplexities(text)
        return min(perplexities, key=perplexities.get)
