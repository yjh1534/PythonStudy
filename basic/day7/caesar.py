#'A' unicode : 65
#'z' unicode : 97
def encrypt(text, n):
    for i in range(len(text)):
        if text[i].isupper():
            text[i] = chr((ord(text[i]) + n - 65) % 26 + 65)
        elif text[i].islower():
            text[i] = chr((ord(text[i]) + n - 97) % 26 + 97)
    print("result: " + ''.join(text))
    
def decrypt(text, n):
    for i in range(len(text)):
        if text[i].isupper():
            text[i] = chr((ord(text[i]) - n - 65) % 26 + 65)
        elif text[i].islower():
            text[i] = chr((ord(text[i]) - n - 97) % 26 + 97)
    print("result: " + ''.join(text))
            
        
while True:
    task = input("Type 'encode' to encrypt, 'decode' to decrypt: ")
    target = input("Type your Message: ")
    n_shift = int(input("Type your shift number: "))
    target = list(target)
    if task == "encode":
        encrypt(target, n_shift)
    else:
        decrypt(target, n_shift)
    if input("continue?: ") == "no":
        break