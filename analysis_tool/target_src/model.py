
class Model():
    def __init__(self):
        self.param = Param()
    
    def update(self):
        self.param.a = 2
        self.param.b = 3
        self.param.c = 4


class Param():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3