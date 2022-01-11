def order_fun():
    size = input("size? S, M, L: ")
    add_pep = input("peperoni? Y or N: ")
    cheese = input("cheese? Y or N: ")
    price = 0
    if add_pep == "Y":
        price = 2
    if size == "S":
        price += 15
    elif size == "M":
        price += 6
    else:
        price += 11
    if cheese == "Y":
        price += 1
    print(f"bill : ${price}")
    
def love_score():
    name = input("Name1: ")
    name += input("Name2: ")
    name = name.lower()
    score1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
    score2 = name.count("l") + name.count("v") + name.count("o") + name.count("e")
    print(f"Score: {score1}{score2}")
    
arg = input("what to run? P for pizza, L for love score, ")
if arg == "P":
    order_fun()
elif arg == "L":
    love_score()


        