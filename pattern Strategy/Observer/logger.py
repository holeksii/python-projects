import json

class Logger:

    @staticmethod
    def write_into_file(list_, FILEPATH="list.json"):
        with open(FILEPATH, "w") as outfile: 
            json.dump(list_, outfile, indent=4)
        