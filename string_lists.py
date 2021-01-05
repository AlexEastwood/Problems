forward = list(input("Please give me a word\n"))
backward = forward[::-1]

if forward == backward:
    print("That's a palindrome")
else:
    print("That's not a palindrome")
