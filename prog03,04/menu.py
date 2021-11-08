from Collection import Collection as C
from Option import Option
import sys


def collection_from_json():
    ok = False
    while not ok:
        answr = input("\nread data from AdvertismentData.json\n(y/n)?\n")
        if answr == 'y':
            collection = C.from_json()
            ok = True
        elif answr == 'n':
            try:
                collection = C.from_json(input("enter FILEPATH:\n"))
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
    7: "exit"
}

def print_menu(options):
    for key in options.keys():
        print (key, '--', options[key] )

def options(option, collection):
    options = Option(collection)
    return {
        "1": options.add_to_collection,
        "2": options.delete_in_collection,
        "3": options.edit_collection,
        "4": options.sort_collection,
        "5": options.search_in_collection,
        "6": options.print_collection,
        "7": sys.exit()
    }.get(option)

def run(method, collection):
    if method:
        return method()
    else:
        print("Choose correct option")
        menu(collection)

def menu(collection):
    print_menu(menu_options)
    option = input("Enter option: ")
    method = options(option, collection)
    run(method, collection)
    menu(collection)
