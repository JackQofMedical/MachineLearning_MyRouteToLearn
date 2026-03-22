import numpy as np
from function_sets import function_sets

class neuralNetwork:
    def __init__(self,inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        
        # weight as random number between -0.5 and 0.5
        self.wih = (np.random.rand(self.hnodes,self.inodes))
        self.who = (np.random.rand(self.onodes,self.hnodes))
        
        self.func_sets = function_sets()
        
    def train(self):
        pass
    def query(self):
        pass
    pass

caculation = neuralNetwork(3,3,3,0.1)
print(caculation.wih)
print(caculation.func_sets.sigma(0.8))

input = [1.0, 0.5, -1.5]

expected_output = [0.5, 0.1, 0.9]



for layer in range(2):
    if layer == 0:
        input = np.array(input, ndmin=2).T
        weight = caculation.wih
    else:
        input = output
        weight = caculation.who
        
    output = caculation.func_sets.sigma(caculation.func_sets.matrix_multiply(weight, input))
    print(output)