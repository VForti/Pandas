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

# Access to elements of a Series object is possible by their index
# (an analogy with a dictionary and access by key comes to mind).

print(my_series[4]) # result - 9

# Indexes can be set explicitly:

my_series2 = pd.Series([3, 1, 6, 2, 9, 4], index=['a', 'b', 'c', 'd', 'e', 'f'])  

# will output all values and keys

print(my_series2) # a    3
                  # b    1
                  # c    6
                  # d    2
                  # e    9
                  # f    4
                  # dtype: int64

# will output the value under the key 'f'

print(my_series2['f']) # 4

# Make a selection based on several indices and carry out group assignment:

print(my_series2[['f','b','a']]) # f    4
                                 # b    1
                                 # a    3
                                 # dtype: int64

# Filter Series as you see fit, as well as apply mathematical operations and much more:


# will display all values greater than 3, but only in the bool value

print(my_series2 > 3) # a    False
                      # b    False
                      # c     True
                      # d    False
                      # e     True
                      # f     True
                      # dtype: bool

# outputs the value

print(my_series2[my_series2 > 3]) # c    6
                                  # e    9
                                  # f    4
                                  # dtype: int64

# If Series reminds us of a dictionary, where the key is the index, and the value is the element itself, then you can do this:

my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
print(my_series3) # a    5
                  # b    6
                  # c    7
                  # d    8
                  # dtype: int64

# it is also possible to search for bool(False or True) by key

print('d' in my_series3) # True

# The Series object and its index have a name attribute that specifies the name of the object and the index, respectively.

my_series3.name = 'numbers' # name
my_series3.index.name = 'letters' # index name
print(my_series3) # letters
                  # a    5
                  # b    6
                  # c    7
                  # d    8
                  # Name: numbers, dtype: int64

# The index can be changed "on the fly" by assigning a list to the index attribute of the Series object

my_series3.index = ['A', 'B', 'C', 'D'] 
print(my_series3) # A    5
                  # B    6
                  # C    7
                  # D    8
                  # Name: numbers, dtype: int64

# Keep in mind that the length of the indexed list must match the number of elements in the Series.




