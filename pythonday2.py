list1=["rose","lotus","passion","sunflower"]
print(list1)
print(list1[2:5])
print(list1[-4:-1])
print(len(list1))
list1.append("tulip")
print(list1)
list1.remove("tulip")
print(list1)
list1.pop()
print(list1)
list2=[1,2,3]
l3 = list1 + list2
print(l3)
print(list2.reverse())
print(list1.clear())

tuple1=("rose","lotus","passion","sunflower")
print(tuple1)
print(tuple1[1:4])
print(tuple1.count("passion"))
print(tuple1.index("rose"))
print(tuple1[-3:-1])

set1={"rose","lotus","passion","sunflower"}
print(set1)
print("rose" in set1)
set1.add("tulip")
print(set1)
set1.update(["hibiscus","chrysynthmum"])
print(set1)
set1.discard("hibiscus")
print(set1)
set2={1,2,3}
set3=set1.union(set2)
print(set3)
set3=set1.intersection(set2)
print(set3)
set3=set1.difference(set2)
print(set3)

dict1={1:"rose",2:"lotus",3:"passion",4:"sunflower"}
x=dict1[2]
print(x)
print(len(dict1))
dict1.pop(3)
print(dict1)
del dict1[4]
print(dict1)
mydict=dict(dict1)
print(mydict)
dict1.clear()
print(dict1)
