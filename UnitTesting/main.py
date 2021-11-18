from menu.menu import menu 
from menu.menu import collection_from_json
from Advertisment.Advertisment import ADVERTISEMENT as AD
from Advertisment.Collection import Collection
from Patterns.Memento import Memento


collection = collection_from_json()
menu(collection)
