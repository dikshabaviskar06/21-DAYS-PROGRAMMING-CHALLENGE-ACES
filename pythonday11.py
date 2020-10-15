import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.0,2,0.01)
y1 = np.sin(2*np.pi*x)
y2 = 0.8*np.sin(4*np.pi*x)
fig,(ax1,ax2,ax3)=plt.subplots(3,1,sharex=True,figsize=(6,6))
ax1.fill_between(x,y1)
ax1.set_title('fill between y1 and 0')
ax2.fill_between(x,y1,1)
ax2.set_title('fill between y1 and 1')
ax3.fill_between(x,y1,y2)
ax3.set_title('fill between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()
plt.show()


#***************************************


fig,ax = plt.subplots()
x=np.arange(0,4*np.pi,0.01)
y=np.sin(x)
ax.plot(x,y,color='black')
threshold = 0.75
ax.axhline(threshold,color='green',lw=2,alpha=0.7)
plt.show()

#****************************************************


N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
plt.show()