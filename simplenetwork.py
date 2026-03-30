import numpy

class neuralNetwork:
    def __init__(self,inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        pass
    def train(self):
        pass
    def query(self):
        pass

rows = 3
columns = 3
randarray=numpy.random.rand(rows,columns)

# self.wih = (numpy.random.rand(self.hnodes,self.inodes)-0.5)
# self.who = (numpy.random.rand(self.onodes,self.hnodes)-0.5)
