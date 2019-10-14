secret = 22
guess = None

while guess!=secret:
    guess = int(input("Guess the secret number : "))

    if guess == secret:
        print ("You guessed it - congratulations! It's number 22.")
        break
    elif guess> secret:
        print ("try something smaller")
    elif guess< secret:
        print ("try something bigger")



