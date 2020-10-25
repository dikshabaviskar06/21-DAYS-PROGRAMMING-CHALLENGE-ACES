import pandas as pd
import numpy as np

#***********window functions***************


df = pd.DataFrame(np.random.randn(10,4),
                  index=pd.date_range('1/1/2000',periods=10),
                  columns=['A','B','C','D'])
print(df)

#rolling() function
print(df.rolling(window=3).mean())

#expanding() function
print(df.expanding(min_periods=3).mean())

#ewm() function
print(df.ewm(com=0.5).mean())

#************aggregations********************
r = df.rolling(window=3,min_periods=1)
print(r)
print(r.aggregate(np.sum))#apply aggregation on a whole dataframe
print(r['A'].aggregate(np.sum))#Apply aggregation on a single column of a Dataframe
print(r[['A','B']].aggregate(np.sum))#Apply aggregation on a multiple columns of a Dataframe
print(r['A'].aggregate([np.sum,np.mean]))#apply multiple functions on a single column of a dataframe
print(r[['A','B']].aggregate([np.sum,np.mean]))#apply multiple functions on a multiple columns of a dataframe
print(r.aggregate({'A':np.sum,'B':np.mean}))#apply different functions to different columns of a dataframe


#***************missing data***************
df=pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
df=df.reindex(['a','b','c','d','e','f','g','h'])
print(df)
print(df['one'].isnull())
print(df['one'].notnull())
print(df['one'].sum())

#---------------------------------------------------------------------------

df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print(df['one'].sum())

#-----------------------------------------------------------------------------

df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c'])
print(df)
print("NaN replaced with zero:")
print(df.fillna(0))
#-------------------------------------------------------------------------------

df = pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e','f','g','h'])
print(df.fillna(method='pad'))
print(df.fillna(method='backfill'))
print(df.dropna())#drop missing values
print(df.dropna(axis=1))

#------------------------------------------------------------------------------------

df=pd.DataFrame({'one':[10,20,30,40,50,2000],'two':[1000,0,30,40,50,60]})
print(df.replace({1000:10,2000:60}))#replace missing values

#-------------------------------xxx---------------------------------------------