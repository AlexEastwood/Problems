name = input("What is your name?\n")
age = int(input("How old are you?\n"))
repeat = int(input("Give me a number\n"))

hundred_year = (2021 - age) + 100

for i in range(repeat):
    print("Well {0}, you will be 100 in the year {1}".format(name, hundred_year))

