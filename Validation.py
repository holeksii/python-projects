class validation:

    @staticmethod
    def isInt(val):
        try:
            int(val)
            return True
        except:
            return False


    @staticmethod
    def isPositive(val):
        if not validation.isInt(val):
            return "Value should be number"
        return val > 0


    @staticmethod
    def a_bigger_b(a, b):
        if not validation.isInt(a) or not validation.isInt(b):
            return "Value should be number"
        return a > b


    @staticmethod
    def Exit(val):
        if val != 'exit':
            print("If you want to exit, type 'exit'")
        else:
            exit()


    @staticmethod
    def get_positive_number():
        while True:
            num = input()
            if not validation.isInt(num):
                print("Value should be a number")
                validation.Exit(num)
                continue
            num = int(num)

            if not validation.isPositive(num):
                print("Value should be a positive number")
                validation.Exit(num)
                continue
            return num


    @staticmethod
    def get_number():
        while True:
            num = input()
            if not validation.isInt(num):
                print("Value should be a number")
                validation.Exit(num)
                continue
            num = int(num)
            return num 