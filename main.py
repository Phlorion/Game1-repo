import numpy as np
import random
from choose_number import choose_seq

grid = np.zeros((10, 10))
num = []
for row in grid:
    for i in range(len(row)):
        row[i] = random.randint(0, 9)
print(grid)

choose_seq(grid, num)
