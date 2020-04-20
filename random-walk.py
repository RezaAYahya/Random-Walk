import numpy
import pylab
import random

# Initialization
n_particle = 10
n_iter = 100
x_pos = numpy.zeros((n_particle, n_iter))
y_pos = numpy.zeros((n_particle, n_iter))

# Iteration
for i in range(1, n_iter):
  for j in range(n_particle):
    rand = random.uniform(0, 1)
    if rand <= 0.25:
      x_pos[j][i] = x_pos[j][i - 1] + 1
      y_pos[j][i] = y_pos[j][i - 1]
    elif rand <= 0.5:
      x_pos[j][i] = x_pos[j][i - 1]
      y_pos[j][i] = y_pos[j][i - 1] - 1
    elif rand <= 0.75:
      x_pos[j][i] = x_pos[j][i - 1] - 1
      y_pos[j][i] = y_pos[j][i - 1]
    else:
      x_pos[j][i] = x_pos[j][i - 1]
      y_pos[j][i] = y_pos[j][i - 1] + 1

#Plotting 
for j in range(n_particle):
  for i in range(1, n_iter):
    pylab.plot(x_pos[j], y_pos[j])
    
pylab.title("Random Walk 2D (" + str(n_iter) + " steps and " + str(n_particle) + " Partikel)")
pylab.show()
