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

#sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Example usage
x = np.array([1, 2, 3])
print("Sigmoid of x:", sigmoid(x))


#mean square error
def mean_square_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)