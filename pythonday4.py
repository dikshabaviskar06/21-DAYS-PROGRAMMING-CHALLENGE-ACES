import re
txt = "welcome to python"
x = re.search("welcome",txt)
print(x)

x=re.findall("come",txt)
print(x)

x=re.split("\s",txt,1)
print(x)

x=re.sub("\s"," ",txt)
print(x)

x=re.A
print(x)

x=re.compile("we")
res=x.findall('welcome to python')
print(res)


print(re.search(r'[^a-z]', 'c'))
print(re.search(r'w[^e]', 'welcome'))

match = re.search(r'^wel', 'welcome to python')
print('Beg. of String:', match)

match = re.search(r'python$', 'welcome to python')
print('End of String:', match)

print('Any Character', re.search(r'w.c.e', 'python 3'))


print('Color',re.search(r'colou?r', 'color'))
print('Colour',re.search(r'colou?r', 'colour'))

print('Date{mm-dd-yyyy}:', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}','10-08-2020'))

print('Three Digit:', re.search(r'[\d]{3,4}', '189'))
print('Four Digit:', re.search(r'[\d]{3,4}', '2145'))
