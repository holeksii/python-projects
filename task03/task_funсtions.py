from LinkedList import LinkedList
from Validation import validation

def isNonDecreaseSorted(arr):
    for i in range(0, len(arr) - 1):
        if arr.index(i) > arr.index(i + 1):
            return False
    return True

def isNonIncreaseSorted(arr):
    for i in range(0, len(arr) - 1):
        if arr.index(i) < arr.index(i + 1):
            return False
    return True

def deleteElements(arr):
    if (isNonDecreaseSorted(arr)) or (isNonIncreaseSorted(arr)):
        return arr
    else:
        m = len(arr) // 4
        for i in range(1, m + 1):
            arr.pop(4 * i - i)
    return arr


def generate_list():
    list = LinkedList()
    print('Enter low bound')
    a = validation.get_number()
    print('Enter up bound')
    b = validation.get_number()
    print('Enter number of elements in list')
    N = validation.get_positive_number()
    list.generate(a, b, N)
    return list


def menu():
    options = {'1 - Generate List' : generate_list,
               '2 - Exit' : exit}

    print("Hello :)\nYou are in Menu, choose one option to continue:")

    while True:
        for key in options.keys():
            print(key)
        option = input()
        for i in options.keys():
            if option == i[0]:
                return options[i]()
        print('Oops!\nTry to choose from available options:')
