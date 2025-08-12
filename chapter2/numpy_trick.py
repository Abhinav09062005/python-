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

