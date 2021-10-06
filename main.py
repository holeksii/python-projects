from task_functions import deleteElements
from task_functions import menu


def main():    
    while True:
        option = menu()
        result = deleteElements(option)
        print(result)


main()
