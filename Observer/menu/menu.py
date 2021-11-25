from menu.Option import Option


menu_options =\
{
    1: "strategy 1",
    2: "strategy 2",
    3: "generate",
    4: "delete item at position",
    5: "delete elements in range",
    6: "task",
    7: "print",
    8: "exit"
}

def print_menu(options):
    for key in options.keys():
        print (key, '--', options[key] )


def options(options, option):

    return {
        1: options.option1,
        2: options.option2,
        3: options.option3,
        4: options.option4,
        5: options.option5,
        6: options.option6,
        7: options.print_linked_list,
        8: options.Exit

    }.get(option)


def run(method):
        return method()
    

def get_option():
    max = menu_options.__len__()
    try:
        option = int(input("Enter option: "))

        if option < 1 or option > max:
            raise ValueError("invalid option")
    except:
            raise ValueError("invalid option")
    return option


def menu(List):

    opts = Option(List)
    i = 0
    while True:
        print_menu(menu_options)
        try:
            option = get_option()
        except Exception as e:
            print(e)
            continue
        
        method = options(opts, option)
        run(method)
