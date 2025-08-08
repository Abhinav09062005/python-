#speed
#list

a=[i for i in range(1000000)]
b=[i for i in range(2000000)]


c=[]
import time

start =time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])
print("Time taken for list addition:", time.time() - start)

# import numpy as np
# a=np.arange(1000000)
# b=np.arange(1000000,4000000)
# start=time.time():
# c = []
#      for i in range(len(a)):
#           c.append(a[i]+b[i])
# print("Time taken for list addition:", time.time() - start)


# memory
a=[i for i in range(10000000)]
import sys
sys.getsizeof(a)
print("Memory size of list a:", sys.getsizeof(a), "bytes")


import numpy as np
a = np.arange(10000000,dtype=np.int8)
print("Memory size of numpy array a:", a.nbytes, "bytes")  # Memory size in bytes


#advanced indexing and slicing
import numpy as np
# 0-> col 1->row

#fancy indexing
a=np.arange(24).reshape(6,4)
print("1D Array a:", a)
print(a[::2,])

##
print(a[[0,1,2]]) #rows


print(a[:,[0,2,3]]) #columns

#boolean indexing
b=np.random.randint(1,100,24).reshape(6,4)
print("Random Array a:\n", b)
print([b>50])  # Elements greater than 50
print(b[b>50])  # Elements greater than 50 in a flat array

print(b[b%2==0])