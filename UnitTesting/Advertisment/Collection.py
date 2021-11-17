import json
from Advertisment.Advertisment import ADVERTISEMENT as AD
from operator import attrgetter#, itemgetter
import copy


class Collection:
    

    FILEPATH = "data/AdvertismentData.json"
    

    def __init__(self):
        self._lst_of_ads = []
        self.size = 0
        

    def copy(self):
        col = Collection()
        col._lst_of_ads = copy.deepcopy(self._lst_of_ads)
        col.size = self.size
        return col


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
                lst_of_ads.append(ad)
            except:
                errors = AD.get_errors(lst_of_items)
                print(f'errors in ADVERTISMENT {i}')
                for error in errors:
                    print(error)
            i += 1
        
        objFile.close()
        collection = cls.from_list(lst_of_ads)
        return collection


    @classmethod
    def from_list(cls, lst):
        col = cls()
        col._lst_of_ads = lst
        col.size = len(lst)
        return col


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

        
    def dump_to_json(self, file=FILEPATH):
        dicts = self.ads_to_dict()
        with open(file, "w") as outfile: 
            json.dump(dicts, outfile, indent=4)


    def sort(self, field):        
        self._lst_of_ads.sort(key = attrgetter(field))
        

    def delete_item(self, id):
        for i in range(len(self._lst_of_ads)):
            if id == self._lst_of_ads[i]._ID:
                self._lst_of_ads.pop(i)
                self.size -= 1
        
        
    def add_item(self, ad):
        if not isinstance(ad, AD):
            raise TypeError
        
        self._lst_of_ads.append(ad)
        self.size += 1
        
    
    def edit(self, id, field_to_edit, new):
        for ad in self._lst_of_ads:
            for item in ad.__dict__.values():
                if str(id) in str(item):
                    ad.__dict__[field_to_edit] = new
        
