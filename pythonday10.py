from matplotlib.pyplot import *

x=[1998,1999,2000,2001,2002]
y=[10,20,30,40,50]
plot(x,y)

#naming x and y axis
xlabel("year")
ylabel("production")
#giving title
title("production study")
show()

#two lines in one graph
x=[1998,1999,2000,2001,2002]
y1=[10,20,30,40,50]
y2=[15,25,33,56,60]
plot(x,y1,label="pen",color="red",marker='o')    #giving label,color and marker
plot(x,y2,label="books",color="blue",linestyle="dashed") #adding linestyle
legend()
show()
#bar graph
x=[1998,1999,2000,2001,2002]
y2=[15,25,33,56,60]
bar(x,y2,color=['red','green'],width=0.5)
show()

#histogram
y=[15,25,33,46,50]
hist(y)
show()

#scatter plot
x=[5,2,6,9,3]
y=[10,5,8,3,0]
scatter(x,y)
show()

#pie chart
x=[1998,1999,2000,2001]
y=[10,20,30,40]
exp=[0,0,0.1,0]
pie(y,labels=x,explode=exp,colors=['red','green','blue','yellow',],autopct='%1.1f%%',shadow='True',radius=1.2,startangle=90)
show()