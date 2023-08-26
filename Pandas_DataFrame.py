# DataFrame
# A DataFrame is best thought of as a regular table, and rightly so, because a DataFrame is a tabular data structure. Every table always has rows and columns. The columns in a DataFrame are Series objects whose rows are their immediate members.

# The DataFrame is easiest to construct using a Python dictionary as an example:

df = pd.DataFrame({
  'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
  'population': [17.04, 143.5, 9.5, 45.5],
  'square': [2724902, 17125191, 207600, 603628]
})
print(df) #       country  population    square
          # 0  Kazakhstan       17.04   2724902
          # 1      Russia      143.50  17125191
          # 2     Belarus        9.50    207600
          # 3     Ukraine       45.50    603628
        
  
  
  # To make sure that the column in the DataFrame is a Series, we extract any:

print(df['country']) # 0    Kazakhstan
                     # 1        Russia
                     # 2       Belarus
                     # 3       Ukraine

print(type(df['country'])) # <class 'pandas.core.series.Series'>



# The DataFrame object has 2 indexes: by rows and by columns.
# If the row index is not explicitly set (for example, the column on which to build them),
# then pandas sets an integer RangeIndex from 0 to N-1, where N is the number of rows in the table.

print(df.columns) # Index(['country', 'population', 'square'], dtype='object')

print(df.index) # RangeIndex(start=0, stop=4, step=1)
# In the table we have 4 elements from 0 to 3.




# Access by index in DataFrame
# The row index can be set in different ways, for example, when forming the DataFrame object itself or on the fly:

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])

df.index.name ='Country Code'
print(df) #                  country  population    square
         # Country Code                                  
         # KZ            Kazakhstan       17.04   2724902
         # RU                Russia      143.50  17125191
         # BY               Belarus        9.50    207600
         # UA               Ukraine       45.50    603628

          
          
          
          
          

# .loc - used to access by string label
# .iloc - used to access by numeric value (starting from 0)


print(df.loc['KZ']) # country       Kazakhstan
                    # population         17.04
                    # square           2724902
                    # Name: KZ, dtype: object


print(df.iloc[0]) # country       Kazakhstan
                  # population         17.04
                  # square           2724902
                  # Name: KZ, dtype: object
      

      
      
      
# You can select by index and columns of interest:
print(df.loc[['KZ', 'RU'], 'population']) # Country Code
                                          # KZ     17.04
                                          # RU    143.50
                                          # Name: population, dtype: float64
 

# As you can see, .loc in square brackets takes 2 arguments: the index of interest, including slicing and column support.

print(df.loc['KZ':'BY',:]) #                  country  population    square
                           # Country Code                                  
                           # KZ            Kazakhstan       17.04   2724902
                           # RU                Russia      143.50  17125191
                           # BY               Belarus        9.50    207600
        
        
 


# Filter the DataFrame using the so-called. boolean arrays:
print(df[df.population > 10][['country', 'square']]) #                  country    square
                                                     # Country Code                      
                                                     # KZ            Kazakhstan   2724902
                                                     # RU                Russia  17125191
                                                     # UA               Ukraine    603628




# Incidentally, columns can be accessed using attribute or Python dictionary notation, i.e. df.population and df['population'] are the same thing.
# You can reset indexes like this:

print(df.reset_index()) #   Country Code     country  population    square
                        # 0           KZ  Kazakhstan       17.04   2724902
                        # 1           RU      Russia      143.50  17125191
                        # 2           BY     Belarus        9.50    207600
                        # 3           UA     Ukraine       45.50    603628
        
        
        
        
# pandas, when operating on a DataFrame, returns a new DataFrame object.

# Let's add a new column in which we divide the population (in millions) by the area of the country, thereby obtaining the density: 
            
df['density'] = df['population'] / df['square'] * 1000000
print(df) #                  country  population    square    density
          # Country Code                                             
          # KZ            Kazakhstan       17.04   2724902   6.253436
          # RU                Russia      143.50  17125191   8.379469
          # BY               Belarus        9.50    207600  45.761079
          # UA               Ukraine       45.50    603628  75.377550
          
          
          
          
          
          
# Don't like the new column? No problem, let's remove it:          
         
print(df.drop(['density'], axis='columns')) #                  country  population    square
                                            # Country Code                                  
                                            # KZ            Kazakhstan       17.04   2724902
                                            # RU                Russia      143.50  17125191
                                            # BY               Belarus        9.50    207600
                                            # UA               Ukraine       45.50    603628
          

# The lazy ones can just write del df['density'].

# You need to rename columns using the rename method:      

df = df.rename(columns={'Country Code': 'country_code'})
print(df) #  country_code     country  population    square
          # 0           KZ  Kazakhstan       17.04   2724902
          # 1           RU      Russia      143.50  17125191
          # 2           BY     Belarus        9.50    207600
          # 3           UA     Ukraine       45.50    603628
                   
          
          
          


df = df.rename(columns={'Country Code': 'country_code'})
print(df) #  country_code     country  population    square
          # 0           KZ  Kazakhstan       17.04   2724902
          # 1           RU      Russia      143.50  17125191
          # 2           BY     Belarus        9.50    207600
          # 3           UA     Ukraine       45.50    603628
                   
          
          
          
             
          
          
          
