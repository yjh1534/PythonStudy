import card

class player:
    def __init__(self):
        self.card = []
        self.hasace = False
        self.points = 0
        
    def addcard(self, c):
        self.card.append(c)
        if type(c.value) == int:
            self.points += c.value
        elif c.value == 'A':
            self.points += 1
            self.hasace = True
        else:
            self.points += 10
            
    def printCards(self):
        texts = ""
        for c in self.card:
            p, v = c.cardinfo()
            texts += f"{p}{str(v)} "
        return texts

    def getScore(self):
        if self.hasace and self.points <= 11:
            return self.points + 10
        return self.points


