

filename = input("Enter filename: ")
keyword = input("Enter keyword: ")

count = 0

with open(filename, "r") as f:
    for line in f:
        if keyword in line:
            print(line.strip())
            count += 1

print("Total lines found:", count)

with open("data.txt", "r") as f:
    content = f.read()

print("Total characters:", len(content))
print("First 50 characters:", content[:50])

domain = "@uludag.edu.tr"
count = 0



filename = input("Enter filename: ")
keyword = input("Enter keyword: ")

count = 0

with open(filename, "r") as f:
    for line in f:
        if keyword in line:
            print(line.strip())
            count += 1

with open("mel.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("Total characters:", len(content))
print("First 50 characters:", content[:50])