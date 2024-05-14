# Import pandas and numpy
import pandas as pd
import numpy as np

# Set numpys random number generator seed to 101
random =  np.random.seed(101)

# create a numpy matrix of 100 rows by 5 columns consisting of random integers from 1-100 (keep in mind that the upper limit may be exclusive)
matrix = np.random.randint(1,101,(100,5))


# Create a dataframe from this matrix
df = pd.DataFrame(data=matrix)

# Rename columnas
df.columns = ['f1','f2','f3','f4','label']

# Create a Datagrame with the following columns: ['A','B','C','D']
# with each column having 50 rows of random numbers between 1 and 100.
# (Hint): Use numpy to create the numbers, then pass them to pandas.
df2 = pd.DataFrame(data=np.random.randint(1,101,(50,4)),columns=['A','B','C','D'])

print(df2)
