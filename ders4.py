'''
word = input("Enter a word: ")
character = input("Enter a character: ")

index = 0
is_found = False
while index < len(word):
    if word[index] == character:
        print("The character is found at index:", index)
        is_found = True
    index += 1
if not is_found:
    print("The character is not found in the word.")

word = input("Enter a word: ")
length = len(word)

while length > 0:
    print(word[length-1], end="")
    length -= 1

word = input("Enter a word: ")
new_word = ""

for letter in word:
    new_word = letter + new_word

print(new_word)


fruit="banana"
a=fruit.find("a")
print(a)
a=fruit.find("c")
print(a)


word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print("Number of vowels:", count)

first = input("Enter first name: ")
last = input("Enter last name: ")

email = first + "." + last + "@student.university.com"

print("Email:", email)
print("Length:", len(email))
'''