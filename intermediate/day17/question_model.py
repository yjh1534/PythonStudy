import random
from numpy import size
from data import question_data

class quiz:
    
    def __init__(self, q, a):
        self.question = q
        self.answer = a.lower()
    
        
    def get_answer(self):
        user_answer = input(f"{self.question} (True/False)?: ")
        user_answer = user_answer.lower()
        is_true = True
        if user_answer == self.answer:
            print("You got it right!")
        else:
            print("That's wrong")
            is_true = False
        print(f"The correct answer was: {self.answer}")
        return is_true
            


class quiz_bank:
    
    def __init__(self):
        random.shuffle(question_data)
        self.quiz_list = []
        self.listsize = 0
        for data in question_data:
            self.quiz_list.append(quiz(data["text"], data["answer"]))
            self.listsize += 1
            
    def get_quiz(self, index):
        return self.quiz_list[index]
    
    def get_size(self):
        return self.listsize
