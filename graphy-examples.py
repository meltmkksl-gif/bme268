from numpy import *

# --- SORU 1 ---
I = eye(10)                       # 10x10 Birim matris
A = random.rand(10, 10)            # 10x10 Rastgele matris
result = I @ A                     # Matris çarpımı
print("Soru 1 - Eşit mi?:", allclose(result, A))

# --- SORU 2 ---
x = linspace(0, 2 * pi, 100)       # 0-2pi arası 100 değer
mask = sin(x) > 0.5                # Boolean maskeleme
filtered = x[mask]
print("Soru 2 - Şartı sağlayan eleman sayısı:", len(filtered))

# --- SORU 3 ---
# 3x3 rastgele tam sayı matrisleri
A_mat = random.randint(1, 10, (3, 3))
B_mat = random.randint(1, 10, (3, 3))

print("Soru 3a - Eleman bazlı çarpım:\n", A_mat * B_mat)
print("Soru 3b - Matris çarpımı (dot):\n", dot(A_mat, B_mat))

A_inv = linalg.inv(A_mat)          # Tersini alma
verify = A_mat @ A_inv             # Doğrulama
print("Soru 3d - Birim matris doğrulaması:\n", round(verify))

# --- SORU 4 ---
arr = random.randint(0, 101, 20)   # 20 rastgele tam sayı
print("Soru 4 - Ortalama:", mean(arr))
print("Soru 4 - Medyan:", median(arr))
print("Soru 4 - Standart Sapma:", std(arr))

indices = where(arr > 50)          # 50'den büyüklerin indisleri
arr[arr < 25] = 0                  # 25'ten küçükleri sıfırla
print("Soru 4 - Güncellenmiş dizi:", arr)

# --- SORU 5 ---
# 1-36 arası sayılardan 6x6 matris
mat = arange(1, 37).reshape(6, 6)

# 3x3 orta alt matrisi kesip alma (indisler 0'dan başlar)
sub = mat[1:4, 1:4] 
print("Soru 5 - 3x3 Orta Matris:\n", sub)

# Düzleştirme ve her 3. elemanı seçme
flat_mat = mat.flatten()
every_third = flat_mat[::3]
print("Soru 5 - Her 3. eleman:", every_third)