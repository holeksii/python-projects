class Event():
    def __init__(self, action, **kwargs):
        self.action = action
        self.specs = dict(kwargs)
        
    def to_dict(self):
        dict = {self.action : self.specs}
        # dict.update(self.specs)
        return dict
        
    def __str__(self) -> str:
        return f"{self.action}       {self.specs}"
