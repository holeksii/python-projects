from Advertisment.Collection import Collection
from menu.Option import Option
import sys


def collection_from_json():
    ok = False
    while not ok:
        answr = input("\nread data from AdvertismentData.json\n(y/n)?\n")
        if answr == 'y':
            collection = Collection.from_json()
            ok = True
        elif answr == 'n':
            try:
                Collection.FILEPATH = input("enter FILEPATH:\n")
                collection = Collection.from_json()
                ok = True
            except Exception as e:
                print(e)
    return collection


menu_options = {
    1: "add_to_collection",
    2: "delete_in_collection",
    3: "edit_collection",
    4: "sort_collection",
    5: "search_in_collection",
    6: "print_collection",
    7: "undo",
    8: "redo",
    9: "exit"
}

def print_menu(options):
    for key in options.keys():
        print (key, '--', options[key] )


def options(options, option):
    
    #options.update_memento()

    return {
        1: options.add_to_collection,
        2: options.delete_in_collection,
        3: options.edit_collection,
        4: options.sort_collection,
        5: options.search_in_collection,
        6: options.print_collection,
        7: options.undo,
        8: options.redo,
        9: sys.exit
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


def menu(collection):
    opts = Option(collection)
    i = 0
    while True:
        # if i != 0:
        #     opts.save()
        # else:
        #     i += 1

        print_menu(menu_options)
        try:
            option = get_option()
        except Exception as e:
            print(e)
            continue
        
        method = options(opts, option)
        run(method)
        
