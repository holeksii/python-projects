import json

class Logger():
    @staticmethod
    def dump_to_file(path, events : list):
        try:
            with open(path, "w") as file:
                json.dump(events, file, indent=4)
        except:
            return -1
