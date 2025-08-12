# np.sort

import numpy as np
a=np.random.randint(1,100,15)
print('sorted array',np.sort(a))

b=np.random.randint(1,100,15).reshape(3,5)
print('sorted array',np.sort(b,axis=0))  # sort by column
print('sorted array',np.sort(b,axis=1))  # sort by row

#descending order
print ('descending sorted array',np.sort(a)[::-1])  # sort by row in descending order



# np.append
# the numpy.append() append values along the nmentioned axis at the end of the array

print ('appended array',np.append(a,200))  # append c to a
print ("append",np.append(b,[[1,2,3,4,5]],axis=0))  # append a row to b

# np.concatenate
# numpy.concatinate() function conctenate a sequence of arrays along an existing axis

c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
print('array c',c)
print('array d',d)
print('concatenated array',np.concatenate((c,d),axis=0))  # concatenate c and d along axis 0
print('concatenated array',np.concatenate((c,d),axis=1))  # concatenate c and d along axis 1


#np.unique
# with the help of np.unique() method we can get the unique values from an array given as parameter in np.unique() method

e=np.array([1,1,2,2,3,3,4,4,5,5,6,6])
f=np.array([[1,2,3,1],[1,2,3,2]])

print('unique values in e:', np.unique(e))  # unique values in 1D array


#np.expand_dims(dimension)
#with the help of numpy.expand_dims() method we can get the expanded dimensions of an array
print(e.shape)  # original shape of e
print('expanded dimensions of e:', np.expand_dims(e, axis=0))  # expand dimensions along axis 0
print('expanded dimensions of e:', np.expand_dims(e, axis=1))  # expand
print(e.shape)



#npp.where
#tthe numpy where() function returns the indices of elements in an input array where the given condition is satisfied

g=np.array([10, 200, 30, 40, 50, 60,70,80])
print('indices of elements greater than 30:', np.where(g > 30))  # find indices where elements are greater than 30
# find all indices with value greater than 50
print('indices of elements greater than 50:', np.where(g > 50))  # find indices where elements are greater than 50

#replace all indices with value greater than 50
g[np.where(g > 50)] = 100
print('g after replacing values greater than 50:', g)  # print g after replacing values greater than 50

#np.argmax
# the numpy.argmax() function returns indices of the max element of the array in a particular axis

print('index of max element in g:', np.argmax(g))  # index of max element in g

#same np.argmin

#np.cumsum
# numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis

print('cumulative sum of g:', np.cumsum(g))  # cumulative sum of g
# sb ko add krte jayga

# same cumprod kaam krega multipy ke liye

#np.percentile
# numpy.percentile() function used to compute the nth percentile of the given data along the specified axis

h=np.array([1,2,3,4,5,6,7,8,9,10])
print('50th percentile of h:', np.percentile(h, 100))  # 50th percentile (median) of h
print('90th percentile of h:', np.percentile(h, 0))  # 90th percentile of h



#np.histogram
# numpy.histogram() function is used to compute the histogram of a set of data
#numpy has a built in numpy histogram() function which represent the frequency of the data distribution in a graphical form


print('histogram of h:', np.histogram(h, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # histogram of h with specified bins
print(np.histogram(h,bins=[0,50,100]))

#np.corrcoef
# return pearson products-moment correlation coefficients

salary=np.array([2000,4000,25000,35000,6000])
experience=np.array([1,2,3,4,5])

print(np.corrcoef(salary, experience))  # correlation coefficient between salary and experience


#np.isin
# with the help of numpy.isin() method we can see that one array having values are checked in a different numpy array having different element with different sizes
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
print('elements of arr1 in arr2:', np.isin(arr1, arr2))  # check if elements of arr1 are in arr2

#np.flip
# the numpy.flip() function reverse the order of the array elements along the specified axis preserving the shape of the array
arr3=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('original array arr3:\n', arr3)  # original array
print('flipped array along axis 0:\n', np.flip(arr3, axis=0))  # flip arr3 along axis 0
print('flipped array along axis 1:\n', np.flip(arr3, axis=1))  # flip arr3 along axis 1


#np.put
# the numpy.put() function replaces specific elements of an array with given values of p_array array indexed works on flattened array
arr4 = np.array([1, 2, 3, 4, 5])
np.put(arr4, [0, 2], [10, 30])  # replace elements at index 0 and 2 with 10 and 30
print('array after np.put:', arr4)  # print arr4 after np.put permanent chnages krta h

#np.delete
# the numpy.delete() function is used to delete elements from an array along a specified axis
arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('original array arr5:\n', arr5)  # original array
print('array after deleting row 1:\n', np.delete(arr5, 1, axis=0))  # delete row at index 1

# set function

n=np.array([1, 2, 3, 4, 5])
m=np.array([4, 5, 6, 7, 8])
print('union of n and m:', np.union1d(n, m))  # union of n and m
print('intersection of n and m:', np.intersect1d(n, m))  # intersection of n and m
print('difference of n and m:', np.setdiff1d(n, m))  # difference of n and m
print('symmetric difference of n and m:', np.setxor1d(n, m))  # common wala ko hata dega baki de dega symmetric difference of n and m
print('elements of n in m:', np.in1d(n, m))  # check if elements of n are in m


#np.swapaxes
# the numpy.swapaxes() function is used to interchange two axes of an array
arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('original array arr6:\n', arr6)  # original array
print('array after swapping axes 0 and 1:\n', np.swapaxes(arr6, 0, 1))  # swap axes 0 and 1 of arr6

# np.clip
# the numpy.clip() function is used to limit the values in an array to a specified range
arr7 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('original array arr7:', arr7)  # original array
print('array after clipping values between 3 and 7:', np.clip(arr7,2,7))  # clip values in arr7 between 3 and 7


# np.uniform
# the numpy.uniform() function is used to generate random numbers from a uniform distribution over a specified range
arr8 = np.random.uniform(1, 10, 5)  # generate 5 random numbers from a uniform distribution between 1 and 10
print('random numbers from uniform distribution:', arr8)  # print random numbers from uniform distribution

