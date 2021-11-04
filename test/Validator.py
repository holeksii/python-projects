import datetime


class Validators:
    
    @staticmethod
    def isInt(val):
        try:
            int(val)
            return True
        except:
            return False


    @staticmethod
    def isPositive(val):
        if not Validators.isInt(val):
            print("Value should be number")
            return False
        return val >= 0

    
    @staticmethod
    def get_number():
        while True:
            num = input()
            if not Validators.isInt(num):
                print("Value should be a number")
                continue
            num = int(num)
            return num


    @staticmethod
    def get_index(up):
        print('Index:')
        index = Validators.get_number()
        if index in range(up):
            return index
        print("invalid index")
        return Validators.get_index(up)


    @staticmethod
    def a_bigger_b(a, b):
        if not Validators.isInt(a) or not Validators.isInt(b):
            return "Value should be number"
        return a > b


    @staticmethod
    def Exit(val):
        if val != 'exit':
            print("If you want to exit, type 'exit'")
        else:
            exit()

    ###
    @staticmethod
    def Url(url):
        url = str(url)
        if url[:8] == "https://" or url[:7] == "http://":
            if url[len(url) - 1] != '.' and '.' in url:
                return url
        raise ValueError("invalid url")
    
    ###
    @staticmethod
    def Date(date):

        formats = ["%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y\%m\%d"]

        for format in formats:
            try:
                datetime.datetime.strptime(date, format)
                return date
            except:
                continue
        raise ValueError("invalid date")
          

    ###
    @staticmethod
    def Currency(val):
        max_price = 99999
        val = float(val)
        if not Validators.isInt(val) or not Validators.isPositive(val):
            raise ValueError("invalid currency type")
        if val < 1 or val > max_price:
            raise ValueError("invalid currency type")
        return round(val, 2)

    ###
    @staticmethod
    def Transaction_number(trsct_num):
        """
            FORMAT:
            XX-YYY-XX/YY
            X - letter
            Y - number
        """
        if trsct_num[2] != '-' or trsct_num[6] != '-' or trsct_num[9] != '/':
            raise ValueError("invalid transaction number")

        if len(trsct_num) != 12:
            raise ValueError("invalid transaction number")

        if not trsct_num[:2].isalpha() or not trsct_num[7:9].isalpha():
            raise ValueError("invalid transaction number")

        if not Validators.isInt(trsct_num[3:6]) or not Validators.isInt(trsct_num[-2:]):
            raise ValueError("invalid transaction number")

        return trsct_num


    ###
    @staticmethod
    def Title(title):
        if str(title).istitle():
            return title
        raise ValueError("invalid title")

    ###
    @staticmethod
    def wrong_date(start, end):
        if start >= end:
            raise ValueError("invalid start or end date")


    ###
    @staticmethod
    def ID(func):
        def wrapper(self, id):
            try:
                id = int(id)
            except:
                raise ValueError("Invalid ID")
                
            if id >= 0:
                result = func(self, id)
                return result
            else:
                raise ValueError("invalid ID")
            
        return wrapper

    @staticmethod
    def url(func):
        def wrapper(self, url):
            url = str(url)
            if url[:8] == "https://" or url[:7] == "http://":
                if url[len(url) - 1] != '.' and '.' in url:
                    return func(self,url)
            raise ValueError("invalid url")
            
        return wrapper

    @staticmethod
    def date(func):
        def wrapper(self, date):
            
            formats = ["%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y\%m\%d"]

            for format in formats:
                try:
                    d = datetime.datetime.strptime(date, format)
                    if d < datetime.datetime(2000, 1, 1) or d > datetime.datetime(2099, 12, 31):
                        raise ValueError("invalid date")
                    return func(self, date)
                except:
                    continue
            raise ValueError("invalid date")
        return wrapper


    @staticmethod
    def currency(func):
        def wrapper(self, price):
            max_price = 99999999
            
            try:
                price = float(price)
            except:
                raise ValueError("invalid price")
            if not Validators.isInt(price) or not Validators.isPositive(price):
                raise ValueError("invalid currency type")
            if price < 1 or price > max_price:
                raise ValueError("invalid currency type")
            return func(self, round(price, 2))

        return wrapper


    @staticmethod
    def transaction_number(func):
        def wrapper(self, trsct_num):
            """
                FORMAT:
                XX-YYY-XX/YY
                X - letter
                Y - number
            """
            if trsct_num[2] != '-' or trsct_num[6] != '-' or trsct_num[9] != '/':
                raise ValueError("invalid transaction number")

            if len(trsct_num) != 12:
                raise ValueError("invalid transaction number")

            if not trsct_num[:2].isalpha() or not trsct_num[7:9].isalpha():
                raise ValueError("invalid transaction number")

            if not Validators.isInt(trsct_num[3:6]) or not Validators.isInt(trsct_num[-2:]):
                raise ValueError("invalid transaction number")

            return func(self, trsct_num)

        return wrapper

    
    @staticmethod
    def title(func):
        def wrapper(self, title):
            if str(title).istitle():
                return func(self, title)
            raise ValueError("invalid title")

        return wrapper


    @staticmethod
    def name(func):
        def wrapper(self, name):
            try:
                str(name).isalpha()
                return func(self, name)
            except:
                raise ValueError("invalid name")

        return wrapper


    @staticmethod
    def datetime(func):
        def wrapper(self, datetime):
            try:
                datetime.datetime.strptime(datetime, '%Y-%m-%d %I:%M')
                return func(self, datetime)
            except:
                raise ValueError("invalid datetime")
        
        return wrapper
