import pandas as pd
import numpy as np

#---create a dataframe from dict of series---
d = {'one' : pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df)


#--column selection--
d = {'one' : pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df['one'])


#--column addition--
d = {'one' : pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print("adding a new column by passing as series")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print("adding a new column using existing column in dataframe:")
df['four']=df['one']+df['three']
print(df)



#---column deletion---
d = {'one' : pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
     'three':pd.Series([10,20,30],index=['a','b','c'])}
print("dataframe is")
df = pd.DataFrame(d)
print("deleting the first column using del function")
del df['one']
print("deleting another column using pop function")
df.pop('two')
print(df)



d = {'one' : pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df = pd.DataFrame(d)
print(df.loc['b'])#--selection by label--
print(df.iloc[2])#--selection by int location--
print(df[2:4])#--slice rows--



#---addition of rows---
df = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=df.append(df2)
print(df)



#---deletion of rows---
df = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=df.append(df2)
df = df.drop(0)#--drop row with label 0
print(df)