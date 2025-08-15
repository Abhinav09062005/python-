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

