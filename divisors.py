divisors = []
num = int(input("Give me a number\n"))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

