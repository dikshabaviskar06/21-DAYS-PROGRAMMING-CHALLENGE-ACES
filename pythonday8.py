#***************type conversion*******************
#___implicit type conversion___
num1=12
num2=1.2
newnum=num1+num2
print("datatype of num1",type(num1))
print("datatype of num2",type(num2))
print("addition is",newnum)            #answer is in float,conversion of int(lower datatype) into float(higher datatype)
print("datatype of newnum",type(newnum))

#___explicit type conversion___
#addition of string and integer
int_num = 123
str_num = "456"
print(int_num+int(str_num))             #string(higher data type) converted into int(lower datatype)


#**********iterating through iter()*************
my_list=[1,2,3,4]
my_iter=iter(my_list)
print(my_iter)
print(next(my_iter))
print(my_iter.__next__())

#**************printing id**************
a=2
print("id(2)=",id(2))
print("id(a)=",id(a))
a=a+1
print("id(a)=",id(a))
print("id(3)=",id(3))

#*********formatting of output**********
x=2;y=5
print("the value of x is {} and y is {}".format(x,y))
print("I like {0} and {1}".format('bread','butter'))
print("hello {name}, {greeting}".format(greeting='goodmorning',name='john'))

x=12.345678
print("the value of x is %3.2f" %x)
print("the value of x is %3.4f" %x)

#********python directory***********
import os
d=os.getcwd()         #get current directory
print(d)
print(os.listdir())    #prints list of subdirectories in current directory
os.mkdir('test')       #creates new directory
os.rename('test','new_one')  #rename the directory
os.remove('test')            #removes the directory
