x=4
if x<5:
    print("x is less than 5")
if x>10:
    print("x is greater than 10")

print("finish")

x=20
if x<2:
    print("small")
elif x<10:
    print("medium")
else :
    print("Large")
print("all done")

astr="hello Bob"
try:
    istr=int(astr)
except:
    istr=-1
print("First", istr)
astr="123"
try:
    istr=int(astr)
except:
    istr=-1    
istr=int(astr)
print("second",istr)


try:
    les=int(input('Haftada kaç saat çalışıyorsunuz ?'))
    les=int(les)

    if les<=40:
        les=(10*les)
        print(les ," ücret alacaksınız")
    else:
        les=(10*40)+(les-40)*15
        print(les,"ücret alacaksınız")

    print('Ayda',les ,'saat çalışacaksınız')
except ValueError:
    print("lütfen geçerli bir sayı giriniz")

answer=input("What is the greatest answer in the world ?")
if answer=="42"  or answer == "forty two":
    print("Correct")
else:
    print("Wrong")

# bank.py

greeting = input("Bir şey yaz: ")

# Baştaki/sondaki boşlukları temizle ve küçük harfe çevir
greeting = greeting.strip().lower()

if "hello" in greeting and greeting.startswith("hello"):
    print("$0")
elif "h" in greeting and greeting.startswith("h"):
    print("$20")
else:
    print("$100")   