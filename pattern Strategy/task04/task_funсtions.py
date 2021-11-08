from task04.LinkedList import LinkedList
from task04.Validation import validation
from task04.generator import randomly_generate


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
    print('Enter low bound:')
    a = validation.get_number()
    print('Enter up bound:')
    b = validation.get_number()
    print('Enter number of elements in list:')
    N = validation.get_positive_number()
    LinkedList.generate(list, a, b, N)
    return list


def enter_list():
    list = LinkedList()
    print('Enter number of elements in list:')
    N = validation.get_positive_number()
    list.enter(N)
    return list


def del_at_k(list):
    print("Enter position to delete element:")
    k = validation.get_positive_number()
    LinkedList.pop(list, k)
    return list


def add_at_k(list):
    print("Enter position to add element:")
    k = validation.get_positive_number()
    el = input("Enter element:\n")
    LinkedList.insert(list, k, el)
    return list


def next(list):
    return deleteElements(list)


def generator_generate():
    lst = LinkedList()
    print('Enter low bound:')
    a = validation.get_number()
    print('Enter up bound:')
    b = validation.get_number()
    print('Enter number of elements in list:')
    N = validation.get_positive_number()
    gen_items = randomly_generate(a, b, N)
    for i in gen_items:
        lst.append(i)
    return lst


def menu():
    options = {'1 - Generate List' : generate_list,
               '2 - Generate List with generator' : generator_generate,
               '3 - Enter List' : enter_list,
               '4 - Exit' : exit}

    print("Hello :)\nYou are in Menu, choose one option to continue:")

    while True:
        for key in options.keys():
            print(key)
        option = input()
        for i in options.keys():
            if option == i[0]:
                return options[i]()
        print('Oops!\nTry to choose from available options:')


def menu_2(list):
    options = {'1 - Add element at k position' : add_at_k,
               '2 - Delete element at k position' : del_at_k,
               '3 - Next' : next,
               '4 - Exit' : exit}

    while True:
        for key in options.keys():
            print(key)
        option = input()
        for i in options.keys():
            if option == i[0]:
                return options[i](list)
        print('Oops!\nTry to choose from available options:')
    
