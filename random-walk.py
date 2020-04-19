import numpy
import pylab
import random
import random

# Initialization
n_particle = 10
n_iter = 100
x_pos = [0]
y_pos = [0]

# Iteration
for i in range(1, n_iter):
  rand = random.uniform(0, 1)
  if rand <= 0.25:
    x_pos.append(x_pos[i - 1] + 1)
    y_pos.append(y_pos[i - 1])
  elif rand <= 0.5:
    x_pos.append(x_pos[i - 1])
    y_pos.append(y_pos[i - 1] - 1)
  elif rand <= 0.75:
    x_pos.append(x_pos[i - 1] - 1)
    y_pos.append(y_pos[i - 1])
  else:
    x_pos.append(x_pos[i - 1])
    y_pos.append(y_pos[i - 1] + 1)

# Plotting
pylab.title("Random Walk 2D ($n = " + str(n_iter) + "$ steps)")
pylab.plot(x_pos, y_pos, 'r')
pylab.show()
