#********************data encapsulation**************************
class computer:
    def __init__(self):
        self.__maxprice = 200

    def sell(self):
        print("selling price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice=price

c = computer()
c.sell()
#changing the price
c.__maxprice = 2000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()

class base:
    def __init__(self):
        self._a=2

class derived(base):
    def __init__(self):


        base.__init__(self)
        print("calling protected member of base class")
        print(self._a)

obj1=derived()
obj2=base()
print(obj2._a)

#*******************polymorphism****************
class parrot:
    def fly(self):
        print("parrot is flying")
    def swim(self):
        print("parrot is not flying")

class penguin:
    def fly(self):
        print("penguin cant fly")
    def swim(self):
        print("penguin can swim")

#common interface
def flying(bird):
    bird.fly()

blu = parrot()
peggy = penguin()

#passing the object
flying(blu)
flying(peggy)

def add(x,y,z=0):
    return x+y+z
print(add(5,6))
print(add(5,6,7))