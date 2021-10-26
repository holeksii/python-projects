import json
from Advertisment import ADVERTISEMENT as AD
from operator import itemgetter, attrgetter
from Memento import Memento


class Collection:
    
    size = 0
    FILEPATH = "data/AdvertismentData.json"
    memento = Memento()

    def __init__(self, lst_of_ads):
        self._lst_of_ads = lst_of_ads
        self.size = len(self._lst_of_ads)
        self.memento.add_condition(self)

    @classmethod
    def from_json(cls, filename = FILEPATH):
        objFile = open(filename, "r")
        text = objFile.read()
        data = json.loads(text)

        lst_of_ads = []
        i = 0
        for dict in data:
            lst_of_items = []
            for dict_item in dict.values():
                lst_of_items.append(dict_item)
            try:
                ad = AD.from_list(lst_of_items)
            except:
                errors = AD.get_errors(lst_of_items)
                print(f'errors in ADVERTISMENT {i}')
                for error in errors:
                    print(error)
            i += 1
            lst_of_ads.append(ad)

        
        objFile.close()

        collection = cls(lst_of_ads)
        collection.memento.add_condition(collection)
        return collection


    def __str__(self):
        st = ""
        for i in range(self.size):
            st += f'ADVERTISMENT {i}:\n\n'
            st += self._lst_of_ads[i].__str__()
            st += 2 * '\n'
        return st


    def search(self, srch):
        found = ''
        i = 0
        for ad in self._lst_of_ads:
            for item in ad.__dict__.values():
                item = str(item)
                if str(srch) in item:
                    found += f'ADVERTISMENT {i}\n'
                    found += item + '\n'
            i += 1
        if not found:
            raise LookupError("value not found")
        return found



    def ads_to_dict(self):
        d = []
        for i in range(self.size):
            d.append(self._lst_of_ads[i].__dict__)
        return d


    def sort(self, field):        
        self._lst_of_ads.sort(key = attrgetter(field))
        self.memento.add_condition(self)


    def delete_item(self, id):
        i = 0
        for ad in self._lst_of_ads:
            for item in ad.__dict__.values():
                if str(id) in str(item):
                    self._lst_of_ads.pop(i)
                    self.size -= 1
            i += 1
        
        dicts = self.ads_to_dict()

        self.memento.add_condition(self)
        with open(self.FILEPATH, "w") as outfile: 
            json.dump(dicts, outfile, indent=4)


    def add_item(self, ad):
        if not isinstance(ad, AD):
            raise TypeError
        
        self._lst_of_ads.append(ad)
        self.size += 1

        dicts = self.ads_to_dict()

        self.memento.add_condition(self)
        with open(self.FILEPATH, "w") as outfile: 
            json.dump(dicts, outfile, indent=4)

    
    def edit(self, id, field_to_edit, new):
        for ad in self._lst_of_ads:
            for item in ad.__dict__.values():
                if str(id) in str(item):
                    ad.__dict__[field_to_edit] = new
        
        dicts = self.ads_to_dict()

        self.memento.add_condition(self)
        with open(self.FILEPATH, "w") as outfile: 
            json.dump(dicts, outfile, indent=4)


    def undo(self):
        self.memento.undo()
        self = self.memento.conditions


    def redo(self):
        self.memento.redo()
        self = self.memento.conditions
