#numpy
import numpy as np
arr = np.array(23)               #0 dimensional array
print(arr)


arr = np.array([1,2,3,4]) #list to create numpy array
print(arr)
print(np.__version__)
print(type(arr))                                                  #1dimensional array

arr = np.array((1,2,3,4)) #tuple to create numpy array
print(arr)
print(arr[1:3])                 #array slicing
print(arr[-3:-1])


arr = np.array([[1,2,3],[4,5,6]])          #2D array
print(arr)
print("2nd element on 1st dimension",arr[0,1])
print("3rd element of 2nd dimension",arr[1,2])
print("last element from second dimension",arr[1,-1])  #negative indexing
print(arr[1,1:4])
print(arr[0:2,2])
print(arr[0:2,1:4])


arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,2,3]]])  #3D array
print(arr)
print(arr.ndim)        #prints dimension of array

arr = np.array([1,2,3,4,5],ndmin = 5)  #5D array
print(arr)
print("shape of array",arr.shape)


arr = np.array([1,2,3],dtype='S') #creating array with datatype string
print(arr)
print(arr.dtype)          #checking datatype of array
newarr = arr.astype('f')  #changing datatype from int to float
print(newarr)

arr = np.array([1,2,3,4])
x= arr.copy()  #making a copy results in change only in original array
arr[0]=23
print(arr)
print(x)
y=arr.view()    #make a view results change in both copied array and original array also
arr[0]=23
print(arr)
print(y)
print(x.base)
print(y.base)
print(arr.reshape(2,2))

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x = arr.reshape(2,3,2)
print(x)
print(x.base)    #returns view

arr = np.array([[1,2,3],[4,5,6]])
new = arr.reshape(-1)   #flattening the array
print(new)

arr = np.array([[1,2,3],[4,5,6]]) #iterating
for x in arr:
    for y in x:
        print(y)
for x in np.nditer(arr):   #iterating using nditer function
    print(x)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1,arr2))
print(arr3)
arr4=np.stack((arr1,arr2),axis=1)
print(arr4)
arr5 = np.hstack((arr1,arr2))   #stacking along row
print(arr5)
arr6 = np.vstack((arr1,arr2))   #stacking along column
print(arr6)
arr7 = np.dstack((arr1,arr2))   #stacking along height
print(arr7)

arr = np.array([2,1,3,4])
nwar = np.array_split(arr,3,)
print(nwar)
x=np.where(arr==4)
print(x)
y=np.searchsorted(arr,3,side='right')
print(y)
print(np.sort(arr))


arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,2,3]]])
nwar1 = np.array_split(arr,3,axis=1)
print(nwar1)

from numpy import random

x=random.rand()  #generate a random float from 0 to 1
print(x)
