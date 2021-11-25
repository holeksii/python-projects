from patterns.Observer.logger import Logger


class Observer():
    path = "data\out.json"

    def update(self, change : list):
        Logger.dump_to_file(self.path, change)
        