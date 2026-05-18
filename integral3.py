from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Diferansiyel denklem
def tumor_growth(V,t, r, k):
    return r*V*(1-V/k)

# Başlangıç değeri: y(0)=1
V0 = 0.5
r=0.04
k=100.0
# Zaman aralığı
t = np.linspace(0, 300, 3000)

# Sayısal çözüm
y = odeint(tumor_growth, V0, t, args=(r, k))

# Grafik
fig, ax = plt.subplots()

ax.plot(t, y, label="y(t)")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

plt.show()