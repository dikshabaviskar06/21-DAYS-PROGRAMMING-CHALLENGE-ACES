import pandas as pd
import numpy as np

#*************Indexing and selecting data**********************
df = pd.DataFrame(np.random.randn(8,4),index=['a','b','c','d','e','f','g','h'],columns=['A','B','C','D'])
#select all rows for specific column
print(df.loc[:,'A'])
#select all rows for multiple columns
print(df.loc[:,['A','C']])
#select few rows for multiple columns
print(df.loc[['a','b','f','h'],['A','C']])
#select range of rows for all columns
print(df.loc['a':'h'])
#for getting values with boolean array
print(df.loc['a']>0)

#--iloc()--

df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])

#select all rows for specific column
print(df.iloc[:4])

#integer slicing
print(df.iloc[:4])
print(df.iloc[1:5,2:4])

#slicing through list of values
print(df.iloc[[1,3,5],[1,3]])
print(df.iloc[1:3,:])
print(df.iloc[:,1:3])


#use of basic indexing operator
print(df['A'])
print(df[['A','B']])
print(df[2:2])

#attribute access
print(df.A)

#************Statistical Functions******************

s=pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df=pd.DataFrame(np.random.randn(5,2))
print(df.pct_change())

#covariance
s1=pd.Series(np.random.randn(10))
s2=pd.Series(np.random.randn(10))
print(s1.cov(s2))

frame = pd.DataFrame(np.random.randn(10,5),columns=['a','b','c','d','e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())

#correlation
print(frame['a'].corr(frame['b']))
print(frame.corr())

#data ranking
s = pd.Series(np.random.randn(5),index=list('abcde'))
s['d']=s['b']
print(s.rank())