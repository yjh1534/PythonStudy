from random import random
import random
import art
from data import data
from os import system

#name, follower_count, description, country
def choose_data(input):
    new_data = random.choice(input)
    input.remove(new_data)
    return new_data

def compare_follower(choosen, another):
    if choosen['follower_count'] > another['follower_count']:
        return True
    return False

def compareinfo(a, b):
    system('cls')
    print(art.logo)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}.")

compareA = choose_data(data)
compareB = choose_data(data)
score = 0
left_data = len(data)
while True:

    compareinfo(compareA, compareB)
    print(len(data))
    print(left_data)
    user_choice = input("Who has more followers? 'A' or 'B': ")
    if user_choice == 'A':
        result = compare_follower(compareA, compareB)
    else:
        result = compare_follower(compareB, compareA)
        compareA = compareB
        
    if not result:
        break
    score += 1
    left_data -= 1
    if left_data == -1:
        break
    compareB = choose_data(data)


system('cls')
print(art.logo)
if left_data > -1:
    print(f"Sorry, that's wrong, Final Score: {score}")
else:
    print(f"Congratulation! Perfect Guess!! Final Score: {score}")
    