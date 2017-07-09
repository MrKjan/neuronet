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

#test
n0, n1, n2, n3, n4, n5 = neuron_entry("n0"), neuron_entry("n1"), neuron("n2"), neuron("n3"), neuron("n4"), neuron("n5")

n5.connect_entry_neuron(n2)
n5.connect_entry_neuron(n3)
n5.connect_entry_neuron(n4)
n5.dendrs[0].set_weight(1)
n5.dendrs[1].set_weight(2)
n5.dendrs[2].set_weight(4)

n4.connect_entry_neuron(n1)
n4.connect_entry_neuron(n0)
n4.dendrs[0].set_weight(-2)
n4.dendrs[1].set_weight(3)

n3.connect_entry_neuron(n1)
n3.connect_entry_neuron(n0)
n3.dendrs[0].set_weight(1)
n3.dendrs[1].set_weight(1)

n2.connect_entry_neuron(n1)
n2.connect_entry_neuron(n0)
n2.dendrs[0].set_weight(2)
n2.dendrs[1].set_weight(-1)

# n3.dendrs[0].acted = 0b1

n0.set_out(0.2)
n1.set_out(0.5)
n5.fill_funcs(fact,fact_w,fact_y)

n5.show(0)

# n5.acted = 0b1
# n5.dendrs[0].acted = 0b1
# n5.dendrs[1].acted = 0b1
# n5.dendrs[2].acted = 0b1
# n4.acted = 0b1
# n1.acted = 0b1

print("\nAfter reset acted\n")

n5.set_not_acted()
n5.show(0)

n5.all_act()
n5.back_propagation(0.4-n5.out)
n4.back_propagation(0)
n3.back_propagation(0)
n2.back_propagation(0)

n5.show(0)
