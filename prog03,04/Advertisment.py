from typing import overload
from Validator import Validators as Vld
import json

class ADVERTISEMENT:

    ID_length = 8

    def __init__(self, ID, website_url, start_date, end_date, price, title, photo_url, transaction_number):

        self.ID = Vld.ID(ID, self.ID_length)
        self.website_url = Vld.url(website_url)
        self.start_date = Vld.date(start_date)
        self.end_date = Vld.date(end_date)
        Vld.wrong_date(start_date, end_date)
        self.price = Vld.currency(price)
        self.title = Vld.title(title)
        self.photo_url = Vld.url(photo_url)
        self.transaction_number = Vld.transaction_number(transaction_number)



    def __str__(self) -> str:
        ret = ''
        for item in self.__dict__.values():
            ret += str(item) + '\n'
        return ret


    @classmethod
    def from_json(cls, file):
        objFile = open(file, "r")
        text = objFile.read()
        y = json.loads(text)
        objFile.close()
        return y
    
    @classmethod
    def from_list(cls, l):
        fields = 8
        if len(l) != fields:
            raise ValueError("invalid size of list")
        return cls(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])

    @classmethod
    def from_keyboard(cls):
        vlds = [Vld.ID, Vld.url, Vld.date, Vld.date, Vld.currency, Vld.title, Vld.url, Vld.transaction_number]
        flds = ["ID", "website_url", "start_date", "end_date", "price", "title", "photo_url", "transaction_number"]
        f = []
        print(flds[0], ':')
        f.append(vlds[0](input(), ADVERTISEMENT.ID_length))

        for i in range(1, len(vlds)):
            print(flds[i], ':')
            f.append(vlds[i](input()))
        
            
        Vld.wrong_date(f[2], f[3])
        return cls(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7],)

# ad = ADVERTISEMENT(4082020, "https://fkdlfp.dde", "2020/08/04", "2021/10/10", 3000.3000, "Hello", "https://oode.png", "yG-857-Se/98")
# print(ad)

a = ADVERTISEMENT.from_keyboard()
print(a)