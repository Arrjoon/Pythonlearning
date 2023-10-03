# Python program for basic slicing.
import numpy as np

# Arrange elements from 0 to 19
a = np.arange(20)
print("\n Array is:\n ", a)

# a[start:stop:step]
print("\n a[-8:17:1]  = ", a[-8:17:1])

# The : operator means all elements till the end.
print("\n a[10:]  = ", a[10:])
