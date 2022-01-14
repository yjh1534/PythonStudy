def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    if number < 2:
        return False
    return True
        
    
    
n = int(input("Number: "))
if prime_checker(number = n):
    print(f"{n} is Prime Number")
else:
    print(f"{n} is not a Prime Number")