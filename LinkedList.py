from Node import Node
from random import randrange
from Validation import validation

class LinkedList:

    count = 0

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None)
        self.count += 1

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

    def empty(self):
        return self.head is None

    def __len__(self):
        return self.count

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
        if self.__len__() <= index:
            print('Invalid index')
            return None
        while pos is not index:
            current = current.next
            pos += 1
        return current.data

    def insert(self, index, value):

        if index > self.__len__() or index < 0:
            print('Invalid index')
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


    def pop(self, index = None):
        ret = "Not found"
        if index is None:
            index = self.__len__() - 1

        if self.head == None:
            return "List is empty"

        temp = self.head

        if index == 0:
            ret = self.head.data
            self.head = temp.next
            temp = None
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
            print("low bound cannot be bigger then up bound")
            return
        for i in range(N):
            value = randrange(a, b)
            self.append(value)


    def clear(self):
        temp = self.head
        if temp is None:
            raise IndexError('The List is empty')
        while temp:
            self.head = temp.next
            temp = self.head
