from neuron import *
from dendr import *



def fep():
    print('yes')
    return 0

def fact(sumd):
    return 1 / (1 + exp(-sumd))

def fact_w(sumd,y_in,w):
    return fact(sumd)*(1-fact(sumd))*y_in

def fact_y(sumd,y_in,w):
    return fact(sumd)*(1-fact(sumd))*w


n00, n01 = neuron_entry('n00'), neuron_entry('n00')
n00.set_out(1)
n01.set_out(1)

n10, n11 = neuron('n10'),neuron('n11')

n10.connect_entry_neuron(n00,1)
n10.connect_entry_neuron(n01,2)

n00.connect_output_neuron(n11,3)
n01.connect_output_neuron(n11,4)

n2 = neuron('n2')
n2.connect_entry_neuron(n10,5)
n2.connect_entry_neuron(n11,6)

n2.fill_funcs(fact,fact_w,fact_y)
n2.set_not_acted()
n2.all_act()
n2.back_propagation(0.5)
n10.back_propagation(0)
n11.back_propagation(0)
n2.show(0)