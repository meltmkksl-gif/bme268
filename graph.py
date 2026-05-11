import numpy as np

v = np.array([1, 2, 3, 4])
M = np.array([[1,2],[3,4]])

print(v.shape)
print(M.shape)
print(M.size)
print(M.dtype)



# Random fonksiyonları için np.random kullanmalısın
np.random.rand(5, 5)
np.random.randn(5, 5)

# Diğer NumPy fonksiyonları için np. kullanmalısın
np.zeros((3, 3))
np.ones((3, 3))

np.diag([1, 2, 3])
np.diag([1, 2, 3], k=1)
np.diag([1, 2, 3], k=-1)

from numpy import*
x=random.rand(3, 3)
x=5*x
x=x-2
print(x)


from numpy import *

matris = array([[3, 2], 
                [1, 4]])

print(matris)

# 4 tane sıfırdan oluşan bir dizi
print(zeros(4))
# Çıktı: [0. 0. 0. 0.]


# 2 satır, 3 sütun tamamen sıfır
print(zeros((2, 3)))
# Çıktı:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 3 satır, 2 sütun tamamen bir
print(ones((3, 2)))
# Çıktı:
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

x=random.rand(3, 3)
print(x)
y=x[2,:]
print(y)



from numpy import *

A = array([1, 2, 3, 4, 5])

print(A[1:3])   # 1. indisten başla, 3. indise kadar (3 dahil değil): [2, 3]
print(A[::2])   # En baştan başla, ikişer atlayarak git: [1, 3, 5]
print(A[:3])    # Baştan başla, 3. indise kadar: [1, 2, 3]
print(A[-1])    # En sondaki eleman: 5
print(A[-3:])   # Sondan 3. elemandan başla, sona kadar git: [3, 4, 5] 