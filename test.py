import numpy as np
a = np.array([1, 2, 6, 4, 2, 3, 2])
u, indices = np.unique(a,  return_counts=True)
print(u)
print(indices)
print(a[indices])