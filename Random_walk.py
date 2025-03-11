#zufallbewegung
import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #Alle Bewegungen neginnen nei (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all points in the walk"""

        #Führt Schritte aus, bis der Pfad die angegebene Läange erreicht hat.
        while len(self.x_values) < self.num_points:

            #Wählt die Richtung und die Weglänge in dieser Richtung aus.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Lehnt Bewegung ab, die nicht vom Fleck führen
            if x_step == 0 and y_step == 0:
                continue
            #Berechnet den nächsten x- und y-Wert.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)