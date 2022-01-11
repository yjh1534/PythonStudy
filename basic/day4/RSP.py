import random

# rock = 0
# scissors = 1
# paper = 2
cases = ["rock", "scissors", "paper"]
choice = int(input("r: 0, s: 1, p: 2 "))
computer = random.randint(0, 2)
print(f"{cases[choice]} VS {cases[computer]}\n")
result = choice - computer
if result == 0:
    print("DRAW")
elif result == 2 or result == -1:
    print("You Win")
else:
    print("You Lose")