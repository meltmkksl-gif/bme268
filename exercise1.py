#Bir dosyayı "data.txt" adıyla açıp sadece ilk 5 satırını ekrana yazdır.
fhand=open("mel.txt")
count=0
for line in fhand:
    if count<5:
        print(line.strip().upper())
        count+= 1

fhand=open("data.txt")
count=0
for line in fhand:
    count+= 1
print("Toplam satır sayısı:", count)

fhand=open("data.txt")
sayı=0
for line in fhand:
    if line.startswith("From:"):
        print(line.strip())
        sayı+= 1
print("Toplam From satır sayısı:", sayı)


input_file = input("Enter file name: ")
try:
    fhand = open(input_file)
    print(line)
except:
    print("File cannot be opened:", input_file)
    exit()  
              
# Sadece "@uct.ac.za" içeren satırları yazdır ama:  
fhand = open("data.txt")

for line in fhand:
    line = line.strip()          # baş-son boşlukları sil
    if "@uct.ac.za" in line:     # içinde geçiyor mu kontrol et
        print(line)
 
count=0     
print("Total lines found:", count)

with open("data.txt", "r") as f:
    content = f.read()

print("Total characters:", len(content))
print("First 50 characters:", content[:50])