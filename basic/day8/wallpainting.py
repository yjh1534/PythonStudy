import math

def paints(h, w, c):
    return math.ceil(h * w / c)


height = int(input("height: "))
width = int(input("width: "))
coverage = 5

print(f"Need {paints(height, width, coverage)} cans of paint")