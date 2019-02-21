import numpy as np
import time
import sys

# let's declare the size
Size = 100000

# Creating two lists
list1 = range(Size)
list2 = range(Size)

# Creating two NumPy arrays
arr1 = np.arange(Size)
arr2 = np.arange(Size)

# Calculating time for Python list
start = time.time()
result = [(x, y) for x, y in zip(list1, list2)]

print("Time for Python List in msec: ", (time.time() - start) * 1000)

# Calculating time for NumPy array
start = time.time()
result = arr1, arr2
print("Time for NumPy array in msec: ", (time.time() - start) * 1000)

# print("This means NumPy array is faster than Python List” )