#what is pandas?
# pandas is a fast powerful flexible and easy to use open source data analysis and manipulation tool built on top of the python programming language.
import numpy as np
import pandas as pd

#strings
country=['India', 'USA', 'China', 'Japan', 'Germany']
print(pd.Series(country))


#numbers
population=[1.4e9, 331e6, 1.4e9, 126e6, 83e6]
print(pd.Series(population))

# conversion of float into int
population_int = [int(pop) for pop in population]
print(pd.Series(population_int))

#custom index
marks=[67,57,89,90,78]
subjects=['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
marks_series = pd.Series(marks, index=subjects,name='Marks of Students')
print(marks_series)


# setting a name
marks_series.name = 'Marks of Students'
print(marks_series)


# series from dict
marks={
    'Maths': 67,
    'Physics': 57,
    'Chemistry': 89,
    'Biology': 90,
    'English': 78
}
marks_series_from_dict = pd.Series(marks, name='Marks of Students')
print(marks_series_from_dict)
# series attribute

# size
print("Size of the series:", marks_series.size)

# dtype
print("Data type of the series:", marks_series.dtype)

# index
print("Index of the series:", marks_series.index)

#is_unique
print("Is the index unique?", marks_series.index.is_unique)

#values
print("Values of the series:", marks_series.values)

#key
print("Key of the series:", marks_series.keys())


print ("ghjvg",marks_series.index)

import sys
print(sys.path)
# ye fiile ka path find krke dega
print(sys.modules)

a = 'Geeks'
print(sys.getrefcount(a))

x=pd.Series([12,13,14,15,16,35,34,76])
print(x[0])

