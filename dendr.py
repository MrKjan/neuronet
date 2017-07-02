# import basis
from basis import *
import random
from neuron import *

class dendr:

    def __init__(self, name = None):
        self.weight = random.uniform(-1, 1)
        self.neuron_in = None
        self.acted = 0b0
        self.out = None
        self.name = name
        #print(self.weight)#TODO: for test

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self): #TODO: for test
        return self.weight


    def set_neuron_in(self, neuron):
        self.neuron_in = neuron

    def act(self):
        if self.acted == 0b0:
            self.out = self.neuron_in.act()*self.weight
            self.acted = 0b1
        return self.out

    def set_not_acted(self):
        if self.acted == 0b1:
            self.neuron_in.set_not_acted()
            self.acted = 0b0
            #



    def decrease_weight(self):
        pass

    def show(self, offset):
        print("   "*offset, self)
        print("   " * offset, "Acted: ", self.acted)
        print("   "*offset, "Neuron")
        self.neuron_in.show(offset+1)

    def __str__(self):
        # return self.name
        return str(self.weight)