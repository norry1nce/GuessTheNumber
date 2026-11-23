import random

def get_guess():
    return int(input("Guess your number: "))

def check_guess(guess, secret):
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    else:
        return "correct"

play = "yes"


while play == "yes":
    secret = random.randint(1,10)
    attempt = 1

    print("Welcome!")
    print("Take a guess between 1 to 10!")
    guess = get_guess()

    while guess != secret and attempt < 3:
       
       result = check_guess(guess, secret)

       if result == "high":
           print(f"Your guess was too high! Attempt {attempt} of 3!")
       elif result == "low":
           print(f"Your guess was too low! Attempt {attempt} of 3!")

       attempt += 1
       guess = get_guess()

    if guess == secret:
        print(f"Congratulations! You guessed the number! it was {secret}!")
    else:
        print(f"You ran out of attempt! You failed! It was {secret}")

    play = input("Play again? yes/no : ")
          

