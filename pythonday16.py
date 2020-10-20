import pandas as pd
import numpy as np

#******series functionality*******

s=pd.Series(np.random.randn(4))
print("original series",s)
print("The axes are:",s.axes)
print("Is the object empty?",s.empty)
print("The dimensions of the object:",s.ndim)
print("The size of the object:",s.size)
print("The actual data series is",s.values)
print("The first two rows of the data series:",s.head(2))
print("The last two rows of the ata series:",s.tail(2))


#*****dataframe functionality*******
d={'Name':pd.Series(['Tom','Jerry','Oggy','Mickey','minnie','chutki','Nobita']),#dictionary of series
   'Age':pd.Series([10,12,13,14,15,16,17])}

df = pd.DataFrame(d) #create a dataframe
print("Our dataseries is:")
print(df)
print("The transpose of data series")
print(df.T)
print("row axis labels and column axis labels are:")
print(df.axes)
print("The datatypes of each column are:")
print(df.dtypes)
print("is there object empty?")
print(df.empty)
print("oue obbject is")
print(df)
print("The dimensions of the object is:")
print(df.ndim)
print("shape of the object is:")
print(df.shape)
print("The total number of elements in object is:")
print(df.size)
print("actual data in dataframe is:")
print(df.values)
print("first two row of dataframe is:")
print(df.head(2))
print("last two rows of dataframe is:")
print(df.tail(2))

#--operations on dataframe--
d={'Name':pd.Series(['Tom','Jerry','Oggy','Mickey','minnie','chutki','Nobita']),#dictionary of series
   'Age':pd.Series([10,12,13,14,15,16,17]),
   'Ratings':pd.Series([3.23,4.2,6.8,6.5,8.0,4.6,3.0])}
df = pd.DataFrame(d)
print(df.sum())
print(df.sum(1))
print(df.mean())
print(df.std()) #standard deviation
print(df.describe())#summarixe data
print(df.describe(include=['object'])) #object=summarize string columns
print(df.describe(include='all')) #summarize all columns
