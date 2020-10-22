import pandas as pd
import numpy as np

#*******************Iteration***********************************************
N=20
df=pd.DataFrame({
    'A':pd.date_range(start='2000-01-01',periods= N ,freq='D'),
    'x':np.linspace(0,stop=N-1,num=N),
    'y':np.random.rand(N),
    'c':np.random.choice(['Low','Medium','High'],N).tolist(),
    'D':np.random.normal(100,10,size=(N)).tolist()

})

#--Iterating a dataframe--
for col in df:
    print(col)

#--iter over rows of dataframe--
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems(): #iterate over (key,value) pairs
    print(key,value)

#------------------------------------------------------------
for row_index,row in df.iterrows():#iterate over rows as (index,series) pairs
    print(row_index,row)
    row['a']=10
print(df)

#------------------------------------------------------------
for row in df.itertuples():#iterate over the rows as namedtuples
    print(row)

#***********************sorting************************
unsort_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsort_df)

#--by label--

sort_df = unsort_df.sort_index()
print(sort_df)

sort_df = unsort_df.sort_index(ascending=False)#order of sorting
print(sort_df)

sort_df = unsort_df.sort_index(axis=1)#sort the column
print(sort_df)

#--by value--
unsort_df1 = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sort_df = unsort_df1.sort_values(by='col1')
print(sort_df)

sort_df1 = unsort_df1.sort_values(by=['col1','col2'])#by argument takes a list of column values
print(sort_df1)

#---sorting algorithm---
sorted_df = unsort_df1.sort_values(by='col1',kind='heapsort')