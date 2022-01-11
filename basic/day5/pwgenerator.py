import random
#유니코드 33부터 '!'
#숫자 : (48, 57), cha[0]
#알파벳 : (65, 90) or (97, 122), cha[1]
#특수문자 : extra, cha[2]
cha = [[],[],[]]

for i in range(33, 127):
    if i in range(48, 57):
        cha[0].append(chr(i))
    elif i in range(65, 90) or i in range(97, 122):
        cha[1].append(chr(i))
    else:
        cha[2].append(chr(i))

pwlen = int(input("how many letters?: "))
symbols = int(input("how many symbols?: "))
numbers = int(input("how many numbers?: "))
pw = []
for i in range(pwlen):
    pw.append(random.choice(cha[1]))
for i in range(symbols):
    pw.append(random.choice(cha[2]))
for i in range(numbers):
    pw.append(random.choice(cha[0]))
random.shuffle(pw)

result = ""
for c in pw:
    result += c
print(f"Result: {result}")
