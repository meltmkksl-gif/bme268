from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

def drug_concentration(t):
    return 20* np.exp(-0.15 * t)

auc, error = quad(drug_concentration, 0, 48)
print(f"AUC (0-48h)={auc:.2f}mg/hr/L")

t=np.linspace(0, 48, 200)
C= drug_concentration(t)

fig, ax=plt.subplots(figsize=(8, 4))
ax.plot(t,C,'b-',lw=2)
ax.fill_between(t,C,alpha=0.3)
ax.set_xlabel('Time (hr)')
ax.set_ylabel('Concentration (mg/L)')
ax.set_title('Drug Concentration-Time Profile (mg/L)')
ax.grid(True,alpha=0.3)
plt.show()