from operator import index
from Advertisment.Collection import Collection
from copy import deepcopy

class Memento:

    max_num_of_conditions = 100

    def __init__(self):
        self.conditions = []
        self.index = -1


    def top_index(self):
        return len(self.conditions) - 1

    def top_condition(self):
        return self.conditions[self.top_index()]


    def add_condition(self, cond):
        if self.index != self.top_index():
            self.conditions = self.conditions[:(self.index + 1)]
        self.conditions.append(cond)

        self.index += 1

        
    def undo(self):
        if self.index != -1:
            self.index -= 1


    def redo(self):
        if self.index != self.top_index():
            self.index += 1


    def get_current(self):
        if index == -1:
            return None
        if isinstance(self.conditions[0], Collection):
            return self.conditions[self.index].copy()
        else:
            return deepcopy(self.conditions[self.index])
        


    
    
    def __eq__(self, o: object) -> bool:
        if self.conditions != o.conditions or self.index != o.index:
            return False
        return True