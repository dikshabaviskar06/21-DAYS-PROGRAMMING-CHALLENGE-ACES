import pandas as pd
import numpy as np

#*********Table wise function application***********
#--adder function--
def adder(num1,num2):
    return num1+num2

df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print(df.apply(np.mean))

#******Row or column wise function application**********
df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print(df.apply(np.mean))

#---------------------------------------------------
df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
print(df.apply(np.mean))

#---------------------------------------------------
df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x:x.max() - x.min())
print(df.apply(np.mean))

#**********element wise function application****************
df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df['col1'].map(lambda x:x*100)
print(df.apply(np.mean))

#----------------------------------------------------
df=pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print(df.apply(np.mean))

#**************Reindexing***********************
N=20
df=pd.DataFrame({
    'A':pd.date_range(start='2000-01-01',periods= N ,freq='D'),
    'x':np.linspace(0,stop=N-1,num=N),
    'y':np.random.rand(N),
    'c':np.random.choice(['Low','Medium','High'],N).tolist(),
    'D':np.random.normal(100,10,size=(N)).tolist()

})
df_reindex = df.reindex(index=[0,3,6],columns=['A','c','B'])
print(df_reindex)
#----------------------------------------------------
df1=pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)
df2=pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
df1=df1.reindex_like(df2)
print("dataframe with forward fill")
print(df2.reindex_like(df1,method='ffill'))#filling while reindexing
print("dataframe with forward fill limiting to 1")
print(df2.reindex_like(df1,method='ffill',limit=1))
print("after renaming the rows and columns")
print(df1.rename(columns={'col1' :'c1','col2' : 'c2'},index ={0 : 'apple', 1:'banana',2:'pineapple'}))