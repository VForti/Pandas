import pandas as pd

# In the string representation of a Series object,
# the index is on the left and the element is on the right. If the index is not explicitly set,
# then pandas automatically creates a RangeIndex from 0 to N-1, where N is the total number of elements.
# It is also worth noting that Series has a type of stored elements,
# in our case it is int64, because we passed integer values.

my_series = pd.Series([3, 1, 6, 2, 9, 4])
print(my_series) # 0    3
                 # 1    1
                 # 2    6
                 # 3    2
                 # 4    9
                 # 5    4
                 # dtype: int64


# The Series object has attributes through which you can get a list of elements and indices,
# these are values and index, respectively.

#index
print(my_series.index) # RangeIndex(start=0, stop=6, step=1)
#values
print(my_series.values) # [3, 1, 6, 2, 9, 4]
