#Write your code below this row 👇
x = 0
for x in range (1, 201):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 15 == 0:
        print("FizzBuzz")
    else:
        print(x)
# range has been added to 201