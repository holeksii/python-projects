import json
from Advertisment import ADVERTISEMENT as AD
from operator import itemgetter, attrgetter

class Collection:
    
    size = 0
    FILEPATH = "data/AdvertismentData.json"

    def __init__(self, lst_of_ads):
        self._lst_of_ads = lst_of_ads
        self.size = len(self._lst_of_ads)

    @classmethod
    def from_json(cls, filename = FILEPATH):
        objFile = open(filename, "r")
        text = objFile.read()
        data = json.loads(text)

        lst_of_ads = []
        for dict in data:
            lst_of_items = []
            for dict_item in dict.values():
                lst_of_items.append(dict_item)
            
            ad = AD.from_list(lst_of_items)
            lst_of_ads.append(ad)


        objFile.close()
        return cls(lst_of_ads)


    def __str__(self) -> str:
        st = ""
        for i in range(self.size):
            st += f'Advertisment {i}:\n\n'
            st += self._lst_of_ads[i].__str__()
            st += 2 * '\n'
        return st


    def search(self, srch):
        found = ""
        i = 0
        for ad in self._lst_of_ads:
            for item in ad.__dict__.values():
                item = str(item)
                if str(srch) in item:
                    found += f'Advertisment{i}\n'
                    found += item + '\n'
            i += 1
        
        return found


    def sort(self, field):        
        self._lst_of_ads.sort(key = attrgetter(field))


    def ads_to_dict(self):
        d = []
        for i in range(self.size):
            d.append(self._lst_of_ads[i].__dict__)
        return d


    def delete_item(self, id):
        i = 0
        for ad in self._lst_of_ads:
            for item in ad.__dict__.values():
                if str(id) in str(item):
                    self._lst_of_ads.pop(i)
                    self.size -= 1
            i += 1
        
        dicts = self.ads_to_dict()

        with open(self.FILEPATH, "w") as outfile: 
            json.dump(dicts, outfile, indent=4)


    def add_item(self):
        while True:
            try:
                item = AD.from_keyboard()
                break
            except Exception as e:
                print(e)
        
        self._lst_of_ads.append(item)
        self.size -= 1

    
    def edit(self):
        pass
        

        



col = Collection.from_json()
col.delete_item("https://ghyc.com")
print(col)
