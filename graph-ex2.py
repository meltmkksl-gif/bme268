from numpy import*
from matplotlib.pyplot import*



x=linspace(0,1,100)
y=sin(2*3*pi*x)#3 ile çarparak 3 periyot oluşturduk

figure
plot(x,y,'r')
xlabel('x')
ylabel('y')
title('Sine Wave')
show()

subplot(1,2,1)
plot('x')
subplot(1,2,2)
plot(x,y,'g*-')

