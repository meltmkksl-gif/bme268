from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Diferansiyel denklem
def model(y, t):
    return -y+1

# Başlangıç değeri: y(0)=1
y0 = 0

# Zaman aralığı
t = np.linspace(0, 10, 100)

# Sayısal çözüm
y = odeint(model, y0, t)

# Grafik
fig, ax = plt.subplots()

ax.plot(t, y, label="y(t)")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

plt.show()
