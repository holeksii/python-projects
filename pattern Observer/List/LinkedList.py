from List.Node import Node
from random import randrange
from List.Validation import validation
from List.generator import *
import json


class LinkedList:

    def __init__(self):
        self.count = 0
        self.head = None


    def __str__(self):
        if self.head:
            temp_node = self.head
            lst = '[ '
            while temp_node is not None:
                lst += f'{temp_node.data} '
                temp_node = temp_node.next
        else:
            return "The List is empty"
        return lst + ']'


    def __len__(self):
        return self.count


    def __iter__(self):
        self.ind = 0
        return self


    def __next__(self):
        if self.ind >= self.count:
            raise StopIteration("Out of list")
        self.ind += 1
        return self.index(self.ind - 1)


    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            self.count += 1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)
        self.count += 1

    def empty(self):
        return self.head is None


    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def index(self, index):
        pos = 0
        current = self.head
        if index >= self.__len__() or index < 0:
            print('Invalid index')
            return None
        while pos != index:
            current = current.next
            pos += 1
        return current.data


    def insert(self, index, value):

        if index > self.__len__() or index < 0:
            raise IndexError('Invalid index')
            return None
        elif index == 0:
            self.head = Node(value, self.head)
        elif index == self.__len__():
            self.append(value)
        else:
            i = 0
            current = self.head
            while current.next:
                if i == index - 1:
                    current.next = Node(value, current.next)
                current = current.next
                i += 1
        self.count += 1


    def pop(self, index=None):
        ret = False
        if index is None:
            index = self.__len__() - 1

        if self.head == None or index >= self.__len__():
            raise IndexError("LinkedList is empty")

        if self.count == 1:
            ret = self.head.data
            self.head = None
            self.count = 0
            return ret


        temp = self.head

        if index == 0:
            ret = self.head.data
            self.head = temp.next
            temp = None
            self.count -= 1
            return ret

        

        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        ret = temp.next.data
        next = temp.next.next
        temp.next = None
        temp.next = next

        self.count -= 1
        return ret


    def generate(self, a, b, N):
        if validation.a_bigger_b(a, b):
            print("invalid bounds")
            return
        for i in range(N):
            value = randrange(a, b)
            self.append(value)


    def enter(self, N):
        print(f"Enter {N} elements of List:")
        for i in range(N):
            self.append(input())
    

    def clear(self):
        temp = self.head
        if temp is None:
            raise IndexError('The List is empty')
        while temp:
            self.head = temp.next

    @classmethod
    def from_list(cls, list):
        List = LinkedList()
        for item in list:
            List.append(item)
        return List

    @classmethod
    def from_json(self, FILEPATH):
        objFile = open(FILEPATH, "r")
        text = objFile.read()
        data = json.loads(text)

        if not isinstance(data, list):
            raise TypeError

        return LinkedList.from_list(data)
    
    def clear(self):
        for i in range(self.__len__()):
            self.pop()


    # @classmethod
    def to_list(self):
        temp = self.head
        l = list()
        l.append(temp.data)
        for i in range(self.count):
            temp = temp.next
            if temp is None:
                break
            l.append(temp.data)
            
        return l
        