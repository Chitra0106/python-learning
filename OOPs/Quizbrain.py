from operator import truediv


class Quizbrain:
    def __init__(self,questions_list):
        self.que_num = 0
        self.score = 0
        self.questions_list =questions_list

    def still_has_question(self):
        return self.que_num < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.que_num]
        self.que_num += 1
        user_answer = input(f"{ self.que_num}: {current_question.text} (True/False)")
        correct_answer = current_question.answer
        self.check_answer(user_answer,correct_answer)
    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got Correct")
            self.score += 1
        else: print("Better Luck Next time")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.que_num}")
        print("\n")





