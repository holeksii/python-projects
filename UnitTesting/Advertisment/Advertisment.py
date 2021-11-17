from Validators.Validator import Validators as Vld


class ADVERTISEMENT:

    ID_length = 8

    def __init__(self, ID, website_url, start_date, end_date, price, title, photo_url, transaction_number):
        self.ID = ID
        self.website_url = website_url
        self.start_date = start_date
        self.end_date = end_date
        Vld.wrong_date(start_date, end_date)
        self.price = price
        self.title = title
        self.photo_url = photo_url
        self.transaction_number = transaction_number

    @property
    def ID(self):
        return self._ID

    @ID.setter
    @Vld.ID
    def ID(self, id):
        self._ID = id

    
    @property
    def website_url(self):
        return self._website_url

    @website_url.setter
    @Vld.url
    def website_url(self, urll):
        self._website_url = urll

    
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    @Vld.date
    def start_date(self, date):
        self._start_date = date

    
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    @Vld.date
    def end_date(self, date):
        self._end_date = date


    @property
    def price(self):
        return self._price

    @price.setter
    @Vld.currency
    def price(self, pr):
        self._price = pr

    
    @property
    def title(self):
        return self._title


    @title.setter
    @Vld.title
    def title(self, ttl):
        self._title = ttl


    @property
    def photo_url(self):
        return self._photo_url


    @photo_url.setter
    @Vld.url
    def photo_url(self, urll):
        self._photo_url = urll


    def __str__(self) -> str:
        ret = ''
        for item in self.__dict__.values():
            ret += str(item) + '\n'
        return ret

    
    @classmethod
    def from_list(cls, l):
        fields = 8
        if len(l) != fields:
            raise ValueError("invalid list")
        return cls((l[0]), l[1], l[2], l[3], l[4], (l[5]), l[6], l[7])



    @classmethod
    def from_keyboard(cls):
        num_of_flds = 8
        flds = []
        out = ["ID:", "website_url:", "start_date:", "end_date:", "price:", "title:", "photo_url:", "transaction_number:"]

        i = 0
        while i < num_of_flds:
            if i == 0 or i == 4:
                try:
                    print(out[i])
                    flds.append(float(input()))
                except:
                    flds.append(-1)
            else:
                print(out[i])
                flds.append(input())
            i += 1
        
        try:
            return cls.from_list(flds)
        except:
            err = ADVERTISEMENT.get_errors(flds)
            for e in err:
                print(e)
            return ADVERTISEMENT.from_keyboard()
        


    @staticmethod
    def get_errors(flds):
        fieldsstr = ['ID', 'website_url', 'start_date', 'end_date', 'price', 'title', 'photo_url', 'transaction_number']
        vlds = [Vld.ID, Vld.url, Vld.date, Vld.date, Vld.currency, Vld.title, Vld.url, Vld.transaction_number]
        
        errors = []
        
        for i in range(len(flds)):
            vld = vlds[i]
            fld = flds[i]
            @vld
            def get_error(self, value):
                pass
    
            try:
                get_error(None, fld)
            except:
                errors.append(f'invalid {fieldsstr[i]}')
            i += 1
        return errors
        