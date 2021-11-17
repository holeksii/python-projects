from Advertisment.Collection import Collection
from Advertisment.Advertisment import ADVERTISEMENT as AD
from Patterns.Memento import Memento



class Option:
    
    def __init__(self, collection):
        self.collection = collection
        cond = self.collection.copy()
        self.memento = Memento()
        self.memento.add_condition(cond)
    
    
    def update_memento(self):
        
        self.collection = self.memento.get_current()


    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, collection):
        if not isinstance(collection, Collection):
            raise TypeError()
        self._collection = collection

    @property
    def memento(self):
        return self._memento

    @memento.setter
    def memento(self, memento):
        if not isinstance(memento, Memento):
            raise TypeError()
        self._memento = memento



    def add_to_collection(self):
        to_add = AD.from_keyboard()
        self.collection.add_item(to_add)
        cond = self.collection.copy()
        self.memento.add_condition(cond)

    def search_in_collection(self):
        value = input("value to search:\n")
        try:
            self.collection.search(value)
        except Exception as e:
            print(e)

    def sort_collection(self):
        while True:
            field = input("input field: ")
            try:
                self.collection.sort(field)
                break
            except:
                print("invalid field")
        
        cond = self.collection.copy()
        self.memento.add_condition(cond)

    def delete_in_collection(self):
        while True:
            try:
                to_delete = int(input("enter value of ADVERTISMENT, you want to delete:\n"))
                self.collection.delete_item(to_delete)
                break
            except:
                print("invalid id")
        
        cond = self.collection.copy()
        self.memento.add_condition(cond)

    def edit_collection(self):
        while True:
            try:
                id = int(input("ID of item to edit:"))
                field = input("field to edit:")
                if field == "price" or field == "ID":
                    new = int(input("new value:"))
                new = input("new value:")
                self.collection.edit(id, field, new)
                break
            except:
                print("invalid")
        
        cond = self.collection.copy()
        self.memento.add_condition(cond)

    def print_collection(self):
        for ad in self.collection._lst_of_ads:
            print(ad)


    def undo(self):
        self.memento.undo()
        self.update_memento()
        

    def redo(self):
        self.memento.redo()
        self.update_memento()


    def save(self):
        while True:
            print(f"save to {self.collection.FILEPATH}/n(y/n)?")
            answr = input()
            if answr == 'y':
                self.collection.dump_to_json()
                break
            elif answr == 'n':
                break
            else:
                continue

