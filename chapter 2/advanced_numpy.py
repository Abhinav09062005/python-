import numpy as np
import array

# Integer array
arr = array.array('i', [1, 2, 3, 4, 5])

# Empty array
empty_arr = array.array('i')

# Array with zeros
zeros_arr = array.array('i', [0] * 5)

print("Integer array:", arr)
print("Empty array:", empty_arr)
print("Array with zeros:", zeros_arr)

a=np.arange(12)
print("Sum of array a:", np.sum(a))

