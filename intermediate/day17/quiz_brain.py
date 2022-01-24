import question_model


class QuizBrain:
    def __init__(self):
        self.point = 0
        self.level = 0
        self.bank = question_model.quiz_bank()
        self.banksize = self.bank.get_size()
        
    def ask_quest(self, index):
        quest = self.bank.get_quiz(index)
        if quest.get_answer():
            self.point += 1
        self.level += 1
        print(f"Your current score: {self.point}/{self.level}\n\n")
    
    def run_quiz(self):
        while self.level < self.banksize:
            self.ask_quest(self.level)
        print("You've completed the Quiz")
        print(f"Score: {self.point}/{self.level}")

