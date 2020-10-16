#******************exception handling*********************
try:
    print(x)
except:
    print("an exception occured")
else:
    print("nothing went wrong")

#****************************************************

from datetime import *
x=datetime.now()
def cal_age(dob):
    age=x.year-dob
    if dob<0:
        raise ValueError("positive values only")
    else:
        print("your age is",age)



try:
    dob=int(input("enter your birthyear"))
    cal_age(dob)
except ValueError:
    print("positive value only")
#********************************************

try:
    a=int(input("enter the no"))
    b=int(input("enter the no"))
    c=a/b
    print("div=",c)
except:
    print("enter int no only")
else:
    print("nothin went wrong")

#***************************************************
x="str"
if not type(x) is str:
    raise Exception("only strings are allowed")
else:
    print("string is printed",x)

#****************************************************

try:
    print(y)
except NameError:
    print("variable y is not defined")
except:
    print("something went wrong")

#******************************************************

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

#*************************************************************
