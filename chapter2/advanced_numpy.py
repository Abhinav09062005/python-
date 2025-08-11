import numpy as np
import matplotlib.pyplot as plt
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
actual =np.random.randint(1,50,25)
predicted = np.random.randint(1, 50, 25)
print("Actual values:", actual)
print("Predicted values:", predicted)
def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)
print("Mean Squared Error (function):", mse(actual, predicted))
print("Mean Squared Error (numpy):", np.mean((actual - predicted) ** 2))

# working with missing values

x=np.array([1, 2, np.nan, 4, 5])
print("Original array with NaN:", x)
print("Is NaN:", np.isnan(x))

print("nan",x[~np.isnan(x)]) # remove nan 

# plotting graph
x=np.linspace(-10, 10, 100)
y=x
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()

h=np.linspace(-10, 10, 100)
d=-(h**2)
plt.plot(d,h)
plt.title("Graph of h^2")
plt.xlabel("h^2")   
plt.ylabel("h")
plt.grid()
plt.show()


k=np.linspace(-10, 10, 100)
plt.plot(np.sin(k))
plt.title("Sine Function")
plt.xlabel("X-axis")
plt.ylabel("sin(X)")
plt.grid()
plt.show()

l=np.linspace(-10, 10, 100)
plt.plot(x*np.log(l))
plt.title("Logarithmic Function")
plt.xlabel("X-axis")    
plt.ylabel("log(X)")
plt.grid()
plt.show()