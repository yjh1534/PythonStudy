class card:
    def __init__(self, p, v):
        self.pattern = p
        self.value = v
    
    def cardinfo(self):
        return self.pattern, self.value
    
    def getpoint(self):
        if type(self.value) == int:
            return self.value
        if self.value != 'A':
            return 10
        return 1

