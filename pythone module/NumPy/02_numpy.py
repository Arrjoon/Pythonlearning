import numpy as np

import sys

list = range(100)

print("The size of the list is ", sys.getsizeof(list))

print("Size of whole list in sthe byte", sys.getsizeof(list)*len(list))

N = np.arange(100)
print("The size of the Numparr is ", N.itemsize)

print("Size of whole list in sthe byte", N.size * N.itemsize)
