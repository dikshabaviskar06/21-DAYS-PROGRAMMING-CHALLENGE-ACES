#*************pandas****************
import pandas as pd
import numpy as np
#---Create a series from ndarray and dictionary----
data = np.array(['a','b','c','d'])
data1 = {'a':0.,'b':1.,'c':2.}
s = pd.Series(data,index=[10,11,12,13])
s1 = pd.Series(data1)
print(s)
print(s1)


data2 = {'a':0.,'b':1.,'c':2.}
s3 = pd.Series(data2,index=['b','c','d','a'])
print(s3)


#---create a series from scalar-----
s4 = pd.Series(5,index=[0,1,2,3])
print(s4)


s5=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s5[0]) #---retriving first element--
print(s5[:3]) #--retriving first three elements--
print(s5[-3:]) #retriving last three elements--
print(s5['a']) #retrive a single element--
print(s5[['a','c','d']]) #--retriving multiple elements--


#--empty dataframe--
df=pd.DataFrame()
print(df)


#-------dataframe using list---------
data = [1,2,3,4]
df = pd.DataFrame(data)
print(df)


data = [['john',10],['kosmina',12],['soram',20]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)


#------data frame using dict of ndarray-----
data = {'Name':['Tom','Jerry','mickey','minnie'],'Age':[20,21,22,23]}
df = pd.DataFrame(data)
print(df)


#---dataframe using passing a list of dictionary and the row indices----
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data,index=['First','Second'])
print(df)


#data frame with list of dictionaries, row indices, and column indices.
data = [{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df1 = pd.DataFrame(data,index=['First','Second'],columns=['a','b'])
df2 = pd.DataFrame(data,index=['First','Second'],columns=['a','b'])
print(df1)
print(df2)
