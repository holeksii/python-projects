from task_funсtions import menu
from task_funсtions import menu_2


def main():    
    while True:
        list = menu()
        print("Your list:\n", list)
        list = menu_2(list)
        print(list)

main()
