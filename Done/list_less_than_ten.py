a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for item in a:
    if item < 5:
        print(item)

for item in a:
    if item < 5:
        b.append(item)

print(b)

num = int(input("Give me a number\n"))

for item in a:
    if item < num:
        c.append(item)
        
print(c)