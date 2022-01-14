#Caculator using Dictionary

from os import add_dll_directory
import os

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : devide,
}
os.system('cls')
n1 = 0
n2 = 0
restarted = True
while True:
    if restarted:
        os.system('cls')
        n1 = float(input("First Number: "))
        restarted = False
    operator = input("Operation?: ")
    n2 = float(input("Second Number: "))
    n1 = operations[operator](n1, n2)
    print(f"Result is {n1}")
    if input("Y to more calculate with result or N to restart ") == 'N':
        restarted = True
        