import random

NUMBER = random.randint(1,100)

def guessresult(guess):
    if guess > NUMBER:
        print("Too high")
        return False
    elif guess < NUMBER:
        print("Too low")
        return False
    else:
        print("You are Correct!!")
        return True

attempt = 10
if input("Choose difficulty. 'easy' or 'hard'? : ") == "hard":
    attempt = 5
while attempt > 0 :
    print(f"{attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guessresult(guess):
        break
    attempt -= 1
if attempt == 0:
    print("You lose!!")
    