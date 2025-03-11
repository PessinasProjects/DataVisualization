from random import randint

class Dado:
    
    def __init__(self, num_sides=6):
    
        self.num_sides = num_sides
    
    def roll(self):
    
        return randint(1, self.num_sides) #zufällige Nummer zw. 1 und Anzahl der Seiten
