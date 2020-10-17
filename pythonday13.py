#**********************operator overloading**********************
#---- + operator for different purpose -----
print(1+2)
print("hi"+"John")
#* operator for different purpose
print(3*4)
print("welcome!"*4)

#----- overloading of binary + operator ---------

class plus:
    def __init__(self,a):
        self.a=a

    def __add__(self, o):
        return self.a+ o.a

obj1 = plus(1)
obj2 = plus(2)
obj3 = plus("hello")
obj4 = plus("John")

print(obj1 + obj2)
print(obj3 + obj4)

#------- addition of two complex numbers ----------
class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return self.a + other.a,self.b + other.b

    def __str__(self):
        return self.a,self.b

obj5=complex(5,6)
obj6=complex(7,8)
obj7=obj5+obj6
print(obj7)

#------- overloading of comparison operator -------

class comparison:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "obj1<obj2"
        else:
            return "obj2<obj1"
    def __eq__(self, other):
        if(self.a==other.a):
            return "both are equal"
        else:
            return "not equal"

obj1=comparison(2)
obj2=comparison(7)
print(obj1<obj2)

obj3=comparison(5)
obj4=comparison(5)
print(obj1==obj2)
print(obj3==obj4)

#-----------------------------------------------

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __lt__(self, other):
        smg = (self.x ** 2) + (self.y ** 2)
        omg = (other.x **2) + (other.y **2)
        return smg < omg

p1=point(1,2)
p2=point(-2,-3)
p3=point(1,-1)

print(p1<p2)
print(p2<p3)
print(p1<p3)
#-----------------------------------------------------