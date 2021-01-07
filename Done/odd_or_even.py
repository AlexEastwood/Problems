number = int(input("Give me a number\n"))

if number % 2 == 0:
    if number % 4 == 0:
        print("That's a multiple of four")
    else:
        print("That number's even")
else:
    print("That number's odd")

num = int(input("Give me another number\n"))
check = int(input("One more\n"))

if check % num == 0:
    print("Yup, that works")
else:
    print("Nope")