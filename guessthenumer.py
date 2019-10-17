import json
import random

secret = random.randint(1, 30)
    attempts = 0

with open("score_list.txt","r") as score_file:
    a = score_file.read() #siempre es string cuando se lee a menos que se le pase una funcion
    score_list = json.loads(a) #transformamos en lista
    print("top scores:" + str(score_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

