import random
from card import card
from player import player
from os import system


def initiate():
    tmp = []
    value_list = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    pattern_list = ['S','D','H','C']
    for pattern in pattern_list:
        for value in value_list:
            tmp.append(card(pattern, value))
    return tmp

def printgameInfo(df, user):
    system('cls')
    print(f"Dealer's first card: {df}\n")
    print(f"You have {user.printCards()}\n")
    if user.getScore() > 21:
        print("You Busted!")
        return 'B'
    next_action = input("Get another Card? 'Y' or 'N': ")
    return next_action

def drawcard(d, p):
    #같은 카드가 두번 뽑히지 않도록 뽑힌 카드는 덱에서 제거
    newcard = random.choice(d)
    d.remove(newcard)
    p.addcard(newcard)


while True:
    #한게임을 시작할때마다 덱을 초기화
    deck = initiate()
    user = player()
    dealer = player()
    drawcard(deck, user)
    drawcard(deck, dealer)
    dealers_first = dealer.printCards()
    drawcard(deck, user)
    drawcard(deck, dealer)
    while True:
        action = printgameInfo(dealers_first, user)
        if action == 'Y':
            drawcard(deck, user)
        else:
            break
    if action == 'B':
        print("You are busted!!")
    else:
        print(f"dealer have {dealer.printCards()}")
        if dealer.getScore() < 17:
            print("dealer's point is less than 17, get another card")
            drawcard(deck, dealer)
            print(f"dealer have {dealer.printCards()}")
        userscore = user.getScore()
        dealerscore = dealer.getScore()
        print(f"user: {userscore} VS dealer: {dealerscore}")
        if dealerscore > 21:
            print("You Win!!")
        elif userscore > dealerscore:
            print("You Win!!")
        elif userscore == dealerscore:
            print("Draw!!")
        else:
            print("You Lose!!")
    if input("Play another game? Y or N: ") == 'N':
        break