import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randrange, random

# Initialization
n_particle = 10
n_iter = 100
x_pos = [0]
y_pos = [0]

# Iteration
for i in range(n_iter):
  for j in range(n_particle):
    # Generate Random
    rand = random.uniform(0,1)
    # Update X and Y position based on the defined probability
    if rand <= 0.25 :
      x_pos[i+1] = x_pos[i] + 1
    elif rand <= 0.5 :
      y_pos[i+1] = y_pos[i] - 1
    elif rand <= 0.75:
      x_pos[i+1] = x_pos[i] - 1
    else :
      y_pos[i+1] = y_pos[i] + 1
