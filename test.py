from neuron import *
from dendr import *



def fep():
    print('yes')
    return 0

#test
n0, n1, n2, n3, n4, n5 = neuron("n0"), neuron("n1"), neuron("n2"), neuron("n3"), neuron("n4"), neuron("n5")

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

n5.show(0)

n5.acted = 0b1
n5.dendrs[0].acted = 0b1
n5.dendrs[1].acted = 0b1
n5.dendrs[2].acted = 0b1
n4.acted = 0b1
n1.acted = 0b1
n3.dendrs[0].acted = 0b1


print("\nAfter reset acted\n")

n5.set_not_acted()
n5.show(0)

n5.fill_funcs(fep,fep)
print("\nAfter reset acted\n")
n5.fill_funcs(fep,fep,[])
n1.f_act()
