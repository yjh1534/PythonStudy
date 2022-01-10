print("welcome to the tip calculator.\n")
total = float(input("what was the total bill? "))
splits = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total = total * (100 + percentage) / 100
print("Each person should pay: $")
print(round(total / splits, 1))