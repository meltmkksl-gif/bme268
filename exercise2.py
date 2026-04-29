'''astr = 'Bob'
try:
    print('Hello') 
    istr = int(astr)
    print('There') 
except:
    istr = -1

print('Done', istr) 

hours = int(input('Enter Hours: '))
r=10
def computepay(h, r):
    pay=40*r+(h-40)*15
    return pay

print(computepay(hours, r))



x=0
count=0
for i in [56,32,45,11,8,5,47]:
    x=x+i
    count=count+1
    
print(x/count)

notlar = "ali veli ahmet ali"
print(notlar.rfind("ali")) # Çıktı: 9 (Sondaki 'ali'nin başladığı yer)
print(notlar.find("ali"))  # Çıktı: 0 (Baştaki 'ali'nin başladığı yer)

email = input("Email adresini girin (user@domain.com): ")
at_index = email.find("@")
dot_index = email.rfind(".")

username = email[:at_index]
domain = email[at_index+1 : dot_index]
extension = email[dot_index+1:]

print(f"Kullanıcı adı: {username}\nAlan adı: {domain}\nUzantı: {extension}")

'''
x=int(input("Enter a number"))
y=0
while x>0:
    y=x%10+y*10
    x=x//10
print(y)    