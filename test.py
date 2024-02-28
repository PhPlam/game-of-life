#%%

import numpy as np
import random

glider_matrix = np.array([[0,1,0],
                          [0,0,1],
                          [1,1,1],
                          [2,2,2]])

#print(np.rot90(glider, 4))

start_pos = (random.randint(0, 1000), random.randint(0, 720))
print(start_pos)

for i in range(np.shape(glider_matrix)[0]):
    for j in range(np.shape(glider_matrix)[1]):
        if glider_matrix[i][j]:
            print(i, j)

# %%

a = (255, 0, 255)
b = (0, 255, 1)

print(zip(a,b))
print(tuple(map(sum, zip(a, b))))

# %%

a = tuple((1,2))
b = (*a, (255, 0, 233))

print(b)
# %%
