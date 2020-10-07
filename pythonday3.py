def MyFunction(name):
    print("welcome to python" +" "+ name + "!")

MyFunction('john')

def Function1(f1,f2,f3="tulip"):
    print("The favourite flower is"+" "+f1)

Function1(f1="rose",f2="lotus")

def Flowers(flower):
    for X in flower:
        print(X)

flower=["rose","tulip","lotus"]
Flowers(flower)

def mul(x):
    return 2 * x

print(mul(4))

def Function3(**flwer):
    print("The fav flower is"+" "+ flwer["f3"])

Function3(f3="rose",f4="lotus")

#lambda function
l=lambda a, b, c : a * b * c
print(l(1,2,3))


def lfunc(n):
    return lambda a:a*n

double=lfunc(2)
print(double(34))


def show(x,y):
    if x>y:
        return x
    else:
        return y
print(show(8,9))
f=lambda x,y:x

from functools import reduce
list1=[1,5,8,2,5,6]
sum=reduce((lambda x,y:x+y),list1)
print(sum)

li=[2,4,6]
final_li= list (filter(lambda x:(x*2!=0),li))
print(final_li)

li2=[2,4,6]
final_li= list(map(lambda x:x*2,li2))
print(final_li)