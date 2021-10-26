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
    def url(url):
        url = str(url)
        if url[:8] == "https://" or url[:7] == "http://":
            if url[len(url) - 1] != '.' and '.' in url:
                return url
        raise ValueError("invalid url")
    
    ###
    @staticmethod
    def date(date):

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
    def currency(val):
        max_price = 99999
        if not Validators.isInt(val) or not Validators.isPositive(val):
            raise ValueError("invalid currency type")
        if val < 1 or val > max_price:
            raise ValueError("invalid currency type")
        return "{:.2f}".format(val)

    ###
    @staticmethod
    def transaction_number(trsct_num):
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
    def ID(id, Len):
        try:
            int(id)
        except:
            raise ValueError("invalid ID")
        if int(id) >= 0 and len(str(id)) <= Len:
            id = str(id)
            return '0' * (Len - len(id)) + id
        else:
            raise ValueError("invalid ID")


    ###
    @staticmethod
    def title(title):
        if str(title).istitle():
            return title
        raise ValueError("invalid title")


    @staticmethod
    def wrong_date(start, end):
        if start >= end:
            raise ValueError("invalid start or end date")
        


    # @staticmethod
    

    # @staticmethod
    # def url(url):
    #     if url[:8] != "https://":
    #         print("invalid url")
    #         return False

    #     TLDs = [".com", ".net", ".org", ".ua"]

    #     for i in TLDs:
    #         if url[-(len(i) - 1):] == i:
    #             return True
    #     print("invalid url")
    #     return False

