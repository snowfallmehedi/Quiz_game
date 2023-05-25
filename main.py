from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    q = question["text"]
    a = question["answer"]
    new_question = Question(q, a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your Final Score is {quiz.final_score()}/{quiz.quiz_number}")
