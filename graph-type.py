from numpy import*
from matplotlib.pyplot import*
import matplotlib.pyplot as plt



x=linspace(0,1,100)
y=sin(2*3*pi*x)

fig, axes=plt.subplots(1,4, figsize=(12, 3))
n=arange(1,10)
axes[0].scatter(x,y)
axes[1].step(n,n**2,color='yellow')
axes[2].bar(n,n**2,color='red')
axes[3].fill_between(x,y, color='lightblue')
axes[0].hist(np.random.randn(1000),bins=50)
show()
  

# 18. ve 19. satırları şöyle güncelle:
axes[1].set_xticks([1, 2, 3, 4, 5]) # Yazım yanlışı düzeltildi
axes[1].set_xticklabels(['bir', 'iki', 'üç', 'dört', 'beş'], fontsize=18)

# 21. satırı mevcut grafik sayına göre güncelle (Örneğin 1 numaralı grafik için):
axes[1].grid()  