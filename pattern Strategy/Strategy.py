from task04.LinkedList import LinkedList

class Strategy:

    @classmethod
    def strategy1(cls, low, up, size):
        """ generate list """
        List = LinkedList()
        List.generate(low, up, size)
        return List
    
    @classmethod
    def strategy2(cls, FILEPATH):
        """ read from file """
        return LinkedList.from_json(FILEPATH)
