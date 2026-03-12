'''
def firstfonction():
    print("Hello Biomedical Engineering")


print("example code")
firstfonction()

def sum(a,b):
    print(a+b)

sum(4,5)


hours=int(input("Enter hours:"))
rate=float(input("Enter rate:"))          
def computepay(hours,rate):
    if hours>40:
        pay=(40*rate)+((hours-40)*rate*1.5)
    else:
        pay=hours*rate
        print("Pay:",pay)
computepay(hours,rate)

hour = int(input("Enter hours: "))
rat = float(input("Enter rate: "))

def computepay(hour, rat):
    if hour > 40:
        pa = (40 * rat) + ((hour - 40) * rat * 1.5)
    else:
        pa = hour * rat
    
    return pa


pa = computepay(hour, rate)
print("Pay:", pa)

while True:
    x=input("Enter someting")
    if x=="done":
        break
    else:
        print("Enter again")

print("DONE")


while True:
    line=input('>')
    if line[0]== '#':
        continue
    if line=="done":
        break
    print(line)
print("Done")

for i in [5,4,3,2,1]:
    print(i)
print ("Blastoff")        

print("Before")
largest=9
for thing in [9,41,12,3,74,15]:
  
    if thing>largest:
        largest=thing
        
print (largest)
print("After")    


'''
'''
sum=0
count=0
for i in [9,41,12,3,74,15]:
    sum=sum+i
    count=count+1
average=sum/count

        
print (average)



x=51


while True:
    num=float( input("Guess a number:"))
    if num==x:
        print("Congratulations")
        break
    elif num>x:
        print("Too high")
    else:
        print("Too low")
        


x=int(input("Enter a number"))
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(x))
'''
'''
#Asal yazdırma
for x in range(2, 101):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x)
'''    
'''
#Ters çevirme
number = int(input("Enter a number: "))
counter = 0
realnumber = number  # Orijinal sayıyı sakla

# Basamak sayısı
while number > 0:
    number //= 10
    counter += 1

print("Number of digits:", counter)


num = 0
while realnumber != 0:
    num = num * 10 + realnumber % 10
    realnumber //= 10

print("Reversed number:", num)
     

#Color and Fruit    
def fruit_by_color(color):
    if color == "red":
        return "apple"
    elif color == "yellow":
        return "banana"
    elif color == "green":
        return "kiwi"
    elif color == "orange":
        return "orange"
    else:
        return "No fruit example"

color = input("Enter a color: ")
print(fruit_by_color(color))     
'''

number = int(input("Enter a number: "))
def is_divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

if is_divisible_by_3_and_5(number):
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")
    