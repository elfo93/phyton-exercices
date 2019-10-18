import json #converti en lista
import random #libreria de numeros
import datetime #libreria de tiempo

secret = random.randint(1, 30)
attempts = 0


with open("score_list.txt","r") as score_file:
    a = score_file.read() #siempre es string cuando se lee a menos que se le pase una funcion
    score_list = json.loads(a) #transformamos en lista
    score_list.sort() #ordenar la lista
    print("top scores:" + str(score_list[3:]))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        current_time = str(datetime.datetime.now())  # nos devuelve el dato en formato datetime
        score_data = {"attempts": attempts, "date": current_time}
        #score_list.append(attempts) #append es para añadir un elemento mas a la lista (el nº de intentos)
        print(current_time)
        score_list.append(score_data)

        with open("score_list.txt","w") as score_file: #abrimos la lista en modo escritura
            #b = json.dumps(score_list) #pasamos la lista a string
            b = json.dumps(score_list)
            score_file.write(b)
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
