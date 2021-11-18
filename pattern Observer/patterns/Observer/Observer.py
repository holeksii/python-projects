import json

class Event():
    def __init__(self, action, **kwargs):
        self.action = action
        self.specs = dict(kwargs)
        
    def to_dict(self):
        dict = {"action":self.action}
        dict.update(self.specs)
        return dict
        
    def __str__(self) -> str:
        return f"{self.action}       {self.specs}"



class Logger():
    @staticmethod
    def EventsToFile(path, events : list):
        try:
            with open(path, "w") as file:
                json.dump(events, file, indent=4)
        except:
            return -1

        


class Observer():
    path = "data\out.json"
    

    def update(self, change : list):
        Logger.EventsToFile(self.path, change)
        