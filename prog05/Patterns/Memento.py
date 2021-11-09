class Memento:

    max_num_of_conditions = 100

    def __init__(self):
        self.conditions = []
        self.index = 0


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
        if self.index != 0:
            self.index -= 1


    def redo(self):
        if self.index != self.top_index():
            self.index += 1


    def get_current(self):
        return self.conditions[self.index].copy()
