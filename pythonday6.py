#math functions
x = min(4,5,6)
y = max(3,7,5)
print(x)
print(y)
x=abs(-20.4)
print(x)
x=pow(3,6)
print(x)


#math module
import math
x= math.sqrt(5)
print(x)
z=math.cosh(45)
print(z)
x=math.degrees(37)
print(x)
y=math.exp(4)
print(y)
z=math.factorial(5)
print(z)
x=math.ceil(2.9)
print(x)
y=math.floor(2.9)
print(y)
z=math.pi
print(z)
x=math.log(10,10)
print(x)
y=math.gamma(67)
print(y)
z=math.gcd(3,8)
print(z)
x=math.isnan(10)
print(x)
y=math.isinf(200)
print(y)


#date module
import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%d"))
y=datetime.datetime(2000,6,26,3,00,00)
print(y)
print(y.strftime("%W"))


#json package
import json
x='{"name":"john","age":32}'
y=json.loads(x)         #parse x
print(y["age"])
z=json.dumps(x) # convert into json
print(z)
print(json.dumps("hello"))
print(json.dumps(True))
print(json.dumps(27.04))
y=json.dumps(x,indent=3,separators=(".","="))
print(y)
print(json.dumps(None))
