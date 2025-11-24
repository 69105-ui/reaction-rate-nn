# model.py
# Basic skeleton for your Reaction Rate Neural Network

import numpy as np
from sklearn.neural_network import MLPRegressor

class ReactionRateNN:
    def __init__(self):
        self.model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu')

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
