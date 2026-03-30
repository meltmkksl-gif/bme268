isimler = ["Ali", "Veli", "Ayşe"]

for i in range(len(isimler)):
    print(isimler[i])
#range sayı ürettir    
for i in range(5):
    print(i)   


isimler = ["Ali", "Veli", "Ayşe"]

for isim in isimler:
    print(isim)    


a = [1, 2]
b = [3, 4]

c = a + b
print(c)  # [1, 2, 3, 4]  
#liste dilimleme
liste = [10, 20, 30, 40, 50]

print(liste[1:3])  # [20, 30]

liste = [1, 2]
liste.append(3)

print(liste)  # [1, 2, 3]
liste = [3, 1, 2]
liste.sort()

print(liste)  # [1, 2, 3]

liste = [1, 2, 3]

print(2 in liste)   # True
print(5 in liste)   # False

veri = "elma,armut,muz"
print(veri.split(","))

# ['elma', 'armut', 'muz']