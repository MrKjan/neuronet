from dendr import *
from copy import copy

class neuron:
    def __init__(self, name = None):
        self.dendrs = []
        self.acted = 0b0
        self.out = None
        self.name = name
        self.sum_for_propagation = 0
        #TODO: out, acted
        #TODO: Не забыть обнулять acted

    def __call__(self, *args, **kwargs):
        return self.act()

    def add_dendr(self, dendr):
        self.dendrs.append(dendr)

    def connect_entry_neuron(self, entry_neuron, weight = None):
        new_dendr = dendr(self.name)
        if weight != None:
            new_dendr.set_weight(weight)
        new_dendr.set_neuron_in(entry_neuron)
        self.add_dendr(new_dendr)

    def connect_output_neuron(self, output_neuron, weight = None):
        new_dendr = dendr(output_neuron.name)
        if weight != None:
            new_dendr.set_weight(weight)
        new_dendr.set_neuron_in(self)
        output_neuron.add_dendr(new_dendr)

    def is_connected(self):
        pass

    def del_dendr(self): #По номеру или по элементу(или по нейрону?)
        pass #TODO

    def set_f_acts(self, f_act, f_act_weight,f_act_in_act):
        self.f_act, self.f_act_weight, self.f_act_in_act = f_act, f_act_weight, f_act_in_act

    def set_f_act(self, f_act):                       #Функция одной переменной суммы
        self.f_act = f_act

    def set_f_act_weight(self, f_act_weight):         #Функция трёх переменных активности, входной активности и веса
        self.f_act_weight = f_act_weight

    def set_f_act_in_act(self, f_act_in_act):         #Функция трёх переменнух активности, входной активности и веса
        self.f_act_in_act = f_act_in_act

    def act(self):
        if self.acted == 0b0:
            self.out = self.f_act(self.sum_dendrs())
            self.acted = 0b1
        return self.out

    #@property
    #TODO: Что значит property?
    def sum_dendrs(self):
        return sum(map(dendr.act, self.dendrs))

    def set_not_acted(self):
        if self.acted == 0b1:
            #map(dendr.set_not_acted, self.dendrs)
            for dendrit in self.dendrs:
                dendrit.set_not_acted()
            self.acted = 0b0
            # return self.name

    def show(self, offset):
        print("   "*offset, self)
        print("   " * offset, "Acted: ", self.acted)
        print("   " * offset, "Out:   ", self.out)
        print("   " * offset, "Sum_d: ", self.sum_dendrs())
        if len(list(self.dendrs)) != 0:
            print("   "*offset, "Dendrs")
            for dendrit in self.dendrs:
                dendrit.show(offset + 1)

    def __str__(self):
        return self.name

    def all_act(self):
        for d in self.dendrs:
            d.neuron_in.all_act()
        self.act()

    def fill_funcs(self, f, f_w, f_aa , setted_neurons = []):
        #print('зашло в ', self.name)
        setted_neurons.append(self)
        for d in self.dendrs:
            if (d.neuron_in not in setted_neurons):
                d.neuron_in.fill_funcs(f, f_w, f_aa, setted_neurons)
        #setted_neurons.remove(self)
        self.set_f_acts(f,f_w,f_aa)
        if self == setted_neurons[0]:
            #print('зашло')                     # Нейрон, с которого начинается
            setted_neurons.clear()              # Заполнение, входит в первым
        #print(self.name,' setted')

    def back_propagation(self, delta):
        self.sum_for_propagation += delta
        for d in self.dendrs:
            d.delta_weight                   = self.f_act_weight(self.sum_dendrs(),d.neuron_in.act(),d.weight)*self.sum_for_propagation
            d.neuron_in.sum_for_propagation += self.f_act_in_act(self.sum_dendrs(),d.neuron_in.act(),d.weight)*self.sum_for_propagation


###########################################################
########################## neuron_entry ###################
###########################################################
class neuron_entry(neuron):

    def __init__(self, name = None):
        super().__init__(name)

    def act(self):
        if self.acted == 0b0:
            print("Error: you didn't setup input")
        return self.out

    def set_out(self, data):
        self.acted = 0b1
        self.setted_data = 0b1
        self.out = data

    def set_not_acted(self):
        if self.setted_data != 0b1:
            super().set_not_acted()
        else:
            self.acted = 0b1



###################################################
################support############################
###############function############################
###################################################








