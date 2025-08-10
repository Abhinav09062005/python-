import numpy as np

arr = np.array([1, 2, 3, 4])
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))


b=np.array([[1,2,3],[4,5,6]])
print("NumPy Array:", b)


c=np.array([0,1,2,3],dtype=bool)
print("Data Type of Array:", c)

c=np.array([0,1,2,3],dtype=complex)
print("Data Type of Array:", c)


print("Array with arange:", np.arange(1, 11))

print("array reshape", np.arange(1, 11).reshape(5,2))
print("Array with linspace:", np.linspace(1, 10, 5))
    # lower range upper range number of elements  equal range or equal distance
print("Array with zeros:", np.zeros((2, 3)))
print("Array with ones:", np.ones((2, 3)))
print("Array with empty:", np.empty((2, 3)))
print("Array with identity matrix:", np.identity(3))
print("Array with random values:", np.random.random((2, 3)))    
print("Array with random integers:", np.random.randint(1, 10, (2, 3)))

a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print("1D Array:", a1)
print("2D Array:", a2)
print("3D Array:", a3)


# //numer of dimensions ndim

print("Number of dimensions of a1:", a1.ndim)
print("Number of dimensions of a1:", a1.shape)

print("Number of dimensions of a2:", a2.ndim)
print("Number of dimensions of a2:", a2.shape)
print("Number of dimensions of a3:", a3.ndim)

# kitne 2 d array haar array ka kitne row aur column h (2,2,2)
print("Number of dimensions of a3:", a3.shape)

print("Size of a1:", a1.size)
print("Size of a2:", a2.size)   
print("Size of a3:", a3.size)# kitne lement h

print("Data type of a1:", a3.itemsize)
# int & float ka same size hota h

#chnge data type of array
a1_float = a1.astype(np.float32)
print("Data type of a1 after conversion:", a1_float.dtype)



# Array operations
a = np.arange(12).reshape(3, 4)
b = np.arange(12, 24).reshape(3, 4)
print("Array a:\n", a)
print("Array b:\n", b)  
#scalar operationa
print("Array a + 10:\n", a + 10)

#relational operations
print ("array",a)
print("Array a ** 2:\n", a ** 2)

#logical operations
print("Logical AND of a and b:\n", np.logical_and(a > 5, b < 20))   
# Mathematical operations
print("Element-wise addition of a and b:\n", np.add(a, b))      
print("Element-wise subtraction of a and b:\n", np.subtract(a, b))  
print("Element-wise multiplication of a and b:\n", np.multiply(a, b))
print("Element-wise division of a and b:\n", np.divide(a, b))
print("Element-wise power of a and b:\n", np.power(a, 2))   
print("Element-wise square root of a:\n", np.sqrt(a))   



#array function
a1=np.random.random((3,3))
a1=np.round(a1*100)
print("Random Array a1:\n", a1)
print("Sum of all elements in a:", np.sum(a1))
print("Sum of each column in a:", np.sum(a1, axis=0))
print(np.max(a1))
print(np.min(a1))
print(np.prod(a1))  
print("Mean of all elements in a:", np.mean(a1))
print("Standard deviation of all elements in a:", np.std(a1))   
print("Variance of all elements in a:", np.var(a1))
print("Median of all elements in a:", np.median(a1))


np.max(a1, axis=0)  # maximum value in each column
np.min(a1, axis=1)  # Minimum value in each row
np.prod(a1,axis=0) # Product of each column


np.sin(a1)

#dot product createria for dot product is that the 
# number of columns in the first matrix must be equal to the number 
# of rows in the second matrix
a2=np.arange(12).reshape(3,4)
b2=np.arange(12,24).reshape(4,3)
print("Array a2:\n", a2)
print("Array a2:\n", b2)
c=np.dot(a2, b2)  # Dot product of a2 and b2
print("Dot product of a2 and b2:\n", c) 

d=np.exp(a2)  # Exponential of each element in a2
e=np.log(a2 + 1)  # Natural logarithm of each element in a2 (adding 1 to avoid log(0))


np.round(np.random.random((3, 3)) * 100)  # Random array with values between 0 and 100
# np.floor // ye number ke piche wale ko deta h
#np.ceil // ye number ke aage wale ko deta h

# 0-> col 1->row

# indexing and slicing
a = np.arange(10)
b= np.arange(12).reshape(3, 4)
c= np.arange(8).reshape(2, 2, 2)

print("1D Array a:", b)

print(b[2,3])

print(c)
print(c[1,0,1])

print (a[2:5])

print(b[:,2])
print(b[1:3, 1:3])  # Slicing rows and columns
print(b[::2,::3])  # Slicing with step size
print (c[:,1,:] )

print(b[::2,])

print(b[1,::3])
print (b[0:2,::3])

d= np.arange(27).reshape(3,3,3)
print("3D Array d:\n", d)

print (d[1])
print(d[::2])

print (d[0,1,:])

print (d[1,:,1])
print (d[2,1:3,1:3])
print (d[::2,0,::2])

#iteration

print (a)
print (b)
print (c)

for i in b:
    print(i)

for i in c:
    print(i)

for i in np.nditer(c):
    print (i)

    #transpose
print("Original Array b:\n", b)
print("Transposed Array b:\n", b.T)  # Transpose of b

#ravel
print("Ravelled Array b:", b.ravel())  # Flatten the array 0ne D aaray dedega

#horizontal stacking
a4=np.arange(12).reshape(3, 4)
b4=np.arange(12, 24).reshape(3, 4)  
x=np.hstack((a4, b4))  # Horizontal stacking of a4 and b4
print("Horizontal Stacking of a4 and b4:\n", x)
#vertical stacking
y=np.vstack((a4, b4))  # Vertical stacking of a4 and b4
print("Vertical Stacking of a4 and b4:\n", y)

#splitting
a5=np.arange(12).reshape(3, 4)
b5=np.arange(12, 24).reshape(3, 4)
x_split=np.hsplit(a5, 2)  # Horizontal split of a5 into 2 equal parts
print("Horizontal Split of a5 into 2 equal parts:\n", x_split)


#broadcasting

# the term broadcastign describes 
# how numpy treats arrays with different shapes during arithemetic operations
# the smaller array is "broadcast" across the larger
# array so that they have compatible shapes


#same shape
a1=np.arange(12).reshape(3, 4)
b1=np.arange(12, 24).reshape(3, 4)
print("Array a1:\n", a1)
print("Array b1:\n", b1)


#diff shape
#broadcasting rules
#1 make the two arrays have the same number of dimensions
# if the numbers of dimensions of the two arrays are different, add new dimension
#with the size 1 to the head of the array with the smaller dimensions

#2 make each dimensions of the two arrays the same size
# if the sizes of the two dimensions are different,
# the size of the dimension of the smaller array must be 1
# if the size of the dimension of the smaller array is not 1, an error will be raised
# if the size of the dimension of the smaller array is 1, it will be stretched
# to match the size of the larger array


x=np.arange(12).reshape(4,3)
y=np.arange(3)
print("Array x:\n", x)
print("Array y:\n", y)
print("Broadcasted Addition of x and y:\n", x + y)  # Broadcasting addition

# x1=np.arange(12).reshape(3, 4)
# y1=np.arange(3)
# print("Array x1:\n", x1)
# print("Array y1:\n", y1)
# print("Broadcasted Addition of x1 and y1:\n", x1 + y1)  # Broadcasting addition not possible


d=np.arange(3).reshape(1,3)
e=np.arange(4).reshape(4,1)

print("Array d:\n", d)
print("Array e:\n", e)
print("Broadcasted Addition of d and e:\n", d + e)  # Broadcasting addition

f=np.arange(12).reshape(3,4)
g=np.arnage(12).reshape(4,3)
#issme nhi hoga kyuki badne ke liye 1 nhi h

h=np.arange(16).reshape(4,4)
j=np.arange(4).reshape(2,2)
# issme v nhi hoga kyuki badne ke liye 1 nhi h
# streched nhi hoga

