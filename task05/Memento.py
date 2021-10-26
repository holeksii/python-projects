class Memento:

    max_num_of_conditions = 100

    def __init__(self):
        self.conditions = []
        self.down = []
        self.up = []

    def add_condition(self, condition):
        self.conditions.append(condition)
        if len(self.conditions) > self.max_num_of_conditions:
            self.conditions.pop()
        if len(self.up) > self.max_num_of_conditions / 2:
            self.up.pop()
        if len(self.down) > self.max_num_of_conditions / 2:
            self.down.pop()
        




    def undo(self):
        self.up.append(self.conditions[len(self.conditions) - 1])
        self.dowm = self.conditions[:-1]
        self.conditions.pop(-1)

    
    def redo(self):
        self.conditions.append(self.up[0])
        self.dowm.append(self.up[len(self.up) - 1])
        self.up.pop()
