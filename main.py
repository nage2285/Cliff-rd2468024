#Write your code below this row 👇
x = 0
for x in range (1, 2001):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
# range has been added to 201