from neuron import *
from dendr import *

n0, n1, n2, n3 = neuron("n0"), neuron("n1"), neuron("n2"), neuron("n3")

n3.connect_entry_neuron(n2)
n3.connect_entry_neuron(n1)
n2.connect_entry_neuron(n0)
n1.connect_entry_neuron(n0)

def fep():
    print('yes')
    return 0