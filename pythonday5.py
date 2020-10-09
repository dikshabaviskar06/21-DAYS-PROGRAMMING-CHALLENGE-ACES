#**************class and object*******************
class myclass:
    def my_func(self):
        print("hello! welcome to python")

obj = myclass()
obj.my_func()

#**************constructors**************************
class myclass:
    def __init__(self):  #default
        self.num=100

    def printval(self):
        print(self.num)

obj = myclass()
obj.printval()



class my_class:
    def __init__(self,name):  #parameterised
        self.name = name
    def my_func(self):
        print("name="+self.name)


obj1= my_class("kosmina")
obj1.my_func()

#************************inheritance*****************************
class parent:
    def first_func(self):                #single inheritance
        print("parent function")

class child(parent):
    def sec_func(self):
        print("child function")

obj = child()
obj.first_func()
obj.sec_func()

class parent1:                              #multiple inheritance
    def parent_func1(self):
        print("parent1 function")

class parent2:
    def parent_func2(self):
        print("parent2 function")

class child(parent1,parent2):
    def child_func(self):
        print("child function")

obj = child()
obj.parent_func1()
obj.parent_func2()
obj.child_func()


class grandparent:              #multilevel inheritance
    def grand_func(self):
        print("inside grandparent class")

class parent(grandparent):
    def parent_func(self):
        print("inside parent class")

class child(parent):
    def child_func(self):
        print("inside child class")

obj = child()
obj.grand_func()
obj.parent_func()
obj.child_func()

class parent:
    def first_func(self):                #hierarchial inheritance
        print("parent function")

class child1(parent):
    def child1_func(self):
        print("inside first child class")

class child2(parent):
    def child2_func(self):
        print("inside second child class")

obj1=child1()
obj2=child2()
obj1.first_func() #calling parent class function by child1 class object
obj2.first_func()  #calling parent class function by child2 class obje
obj1.child1_func()
obj2.child2_func()

class parent:                      #hybrid inheritance
    def func1(self):
        print("inside parent function")

class child(parent):
    def func2(self):
        print("inside child function")

class child1(parent):
    def func3(self):
        print("inside child1 function")

class child3(child,parent):
    def func4(self):
        print("inside child2 function")

obj = child3()
obj.func1() #calling parent class function by child3 class object
obj.func2() #calling child class function by child3 class object

