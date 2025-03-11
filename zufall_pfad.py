import matplotlib.pyplot as plt
from Random_walk import RandomWalk

#Ertstellen einen Zufallspfad
rw = RandomWalk()
rw.fill_walk()

#Gibt die Punkte in einem Diagram aus.
plt.style.use("classic")

fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect("equal")

plt.show()