import numpy as np

class function_sets:
    def __init__(self):
        pass
    def sigma(self, x):
        return 1 / (1 + np.exp(-x))
    def matrix_multiply(self, weight, input):
        return np.dot(weight, input)