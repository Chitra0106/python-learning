from ChallengeData import questions_data
from Class_Challenge import question
from Quizbrain import Quizbrain

question_bank=[]
for que in questions_data:
    QueText = que["text"]
    QueAnswer = que["answer"]
    new_question = question(QueText, QueAnswer)
    question_bank.append(new_question)
#for q in question_bank:
    #q.display()

quiz = Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
