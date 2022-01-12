import random
import word
import ui

global target, cur_state, length


def check(c):
    global target, cur_state, length
    result = False
    temp = list(cur_state)
    for i in range(0, length) :
        if target[i] == c:
            temp[i] = c;
            result = True
    if result:
        cur_state = ''.join(temp)
    return result


while True:
    target = random.choice(word.word_list)
    cur_state = '_'*len(target)
    target = ' '.join(target)
    cur_state = ' '.join(cur_state)
    wrong_count = 0
    length = len(target)
    while wrong_count < 6:
        ui.redraw(wrong_count)
        print(cur_state)
        print(f"\n Chances : {6 - wrong_count}")
        choice = input("Guess a letter: ")
        if not check(choice):
            wrong_count += 1
        elif cur_state == target:
            break 
    ui.redraw(wrong_count)
    print(f"the answer is: {target}")
    if wrong_count < 5:
        if_continue = input("Success! replay? Y or N: ")
    else:
        if_continue = input("FAIL! Replay? Y or N: ")
        
    if if_continue == 'N':
        break
        
    wrong_count = 0