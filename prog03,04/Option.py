from Collection import Collection
from Advertisment import ADVERTISEMENT as AD
import sys


class Option:
    
    def __init__(self, collection):
        self.collection = collection
    

    @property
    def collection(self):
        return self.collection

    @collection.setter
    def collection(self, collection):
        if not isinstance(collection, Collection):
            raise TypeError()
        self._collection = collection


    def add_to_collection(self):
        to_add = AD.from_keyboard()
        self.collection.add_item(to_add)
        pass


    def search_in_collection(self):
        value = input("value to search:\n")
        try:
            self.collection.search(value)
        except Exception as e:
            print(e)

    def sort_collection(self):
        field = input()
        self.collection.sort(field)
        pass

    def delete_in_collection(self):
        to_delete = int(input("enter value of ADVERTISMENT, you want to delete"))
        self.collection.delete_item(to_delete)
        pass

    def edit_collection(self):
        id = int(input("item to edit id:"))
        field = input("field to edit:")
        if field == "price" or field == "ID":
            new = int(input("new value:"))
        new = input("new value:")
        self.collection.edit(id, field, new)

    def print_collection(self):
        print(self)

