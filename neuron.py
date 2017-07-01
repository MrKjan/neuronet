from dendr import *

class neuron:
    def __init__(self, name = None):
        self.dendrs = []
        self.acted = 0b0
        self.out = None
        self.name = name
        #TODO: out, acted
        #TODO: Не забыть обнулять acted

    def add_dendr(self, dendr):
        self.dendrs.append(dendr)

    def connect_entry_neuron(self, entry_neuron):
        new_dendr = dendr(self.name)
        new_dendr.set_neuron_in(entry_neuron)
        self.add_dendr(new_dendr)

    def connect_output_neuron(self, output_neuron):
        new_dendr = dendr(output_neuron.name)
        new_dendr.set_neuron_in(self)
        output_neuron.add_dendr(new_dendr)

    def is_connected(self):
        pass

    def del_dendr(self): #По номеру или по элементу(или по нейрону?)
        pass #TODO

    def set_f_acts(self, f_act, f_act_):
        self.f_act, self.f_act_= f_act, f_act_

    def set_f_act(self, f_act):
        self.f_act = f_act

    def set_f_act_(self, f_act_):
        self.f_act_ = f_act_

    def act(self):
        if self.acted == 0b0:
            self.out = self.f_act(self.sum_dendrs)
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
                dendrit.set_not_acted();
            self.acted = 0b0
            # return self.name

    def show(self, offset):
        print("   "*offset, self)
        print("   " * offset, "Acted: ", self.acted)
        if len(list(self.dendrs)) != 0:
            print("   "*offset, "Dendrs")
            for dendrit in self.dendrs:
                dendrit.show(offset + 1)

    def __str__(self):
        return self.name


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
        self.out = data








