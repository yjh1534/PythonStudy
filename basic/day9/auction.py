#day8 딕셔너리 이용한 경매프로그램 구현
import os

bidders = {}
finish = False
while not finish:
    name = input("What is your name?: ")
    bid = input("how much?: ")
    bidders[name] = int(bid)
    if input("Other bidders? Y or N: ") == 'N':
        finish = True
    os.system("cls")

winner = ''
highest = 0

for bidder in bidders:
    if bidders[bidder] > highest:
        winner = bidder
        highest = bidders[bidder]
print(f"winner is {winner} with ${highest}")