print("Hello, its the fizzbuzz game")

answer = int(input("write a number between 1 and 100: "))

for num in range(1, answer+1):

    if answer % 3 == 0:
        print("Fizz")

    if answer % 5 == 0:
        print("Buzz")
    if answer % 5 and answer % 3 == 0:
        print("fizzbuzz")

    else:
        print(num)


