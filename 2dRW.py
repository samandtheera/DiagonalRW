import numpy as np
import pylab
import random
import numpy as np

# Diagonal 2D Random Walk Modelled

# Number of steps
n = 1000

# Size of step
s = 1

# Array to store position
x = np.zeros(n)
y = np.zeros(n)

# Assuming the four diagonal directions of movement.
# Quad 1 is upper right quadrant, and it goes clockwise.
direction = ["Quad1", "Quad2", "Quad3", "Quad4"]
for i in range(1, n):
    # Randomly choosing the direction of movement.
    step = np.random.choice(direction, p=[0.25, 0.25, 0.25, 0.25])

    # updating the direction with respect to the direction of motion choosen.
    if step == "Quad1":
        x[i] = x[i - 1] + s
        y[i] = y[i - 1] + s
    elif step == "Quad2":
        x[i] = x[i - 1] + s
        y[i] = y[i - 1] - s
    elif step == "Quad3":
        x[i] = x[i - 1] - s
        y[i] = y[i - 1] - s
    else:
        # Quad 4 is the upper left quadrant.
        x[i] = x[i - 1] - s
        y[i] = y[i - 1] + s


pylab.title("Random Walk 2-D where p = q = 0.5 - Problem Set 4")
fig = pylab.plot(x, y)  # plotting the walk.
pylab.show()
