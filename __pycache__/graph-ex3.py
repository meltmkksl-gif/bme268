from numpy import*
from matplotlib.pyplot import*
import matplotlib.pyplot as plt

x=linspace(0,2*pi,100)
y1=sin(2*pi*x)
y2=cos(2*pi*x)
y3=tan(2*pi*x)
plot(x,y1,'b-',label='sin(2*pi*x)')
plot(x,y2,'r--',label='cos(2*pi*x)')
plot(x,y3,'g:',label='tan(2*pi*x)')
show()

