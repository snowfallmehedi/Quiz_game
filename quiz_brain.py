class QuizBrain:

    def __init__(self, q_list):
        self.quiz_number = 0
        self.quiz_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.quiz_number < len(self.quiz_list)

    def next_question(self):
        current_question = self.quiz_list[self.quiz_number]
        answer = input(f"Q. {self.quiz_number+1}. {current_question.text} ? (True/False)?")
        self.quiz_number += 1
        self.check_answer(current_question.answer, answer)

    def check_answer(self, correct_answer, answer):
        if answer.lower() == correct_answer.lower():
            print("You got it Right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.quiz_number}")
        else:
            print("Your Answer is Wrong!")
            print(f"Your score is {self.score}/{self.quiz_number}")
        print(f"The correct answer is {correct_answer}\n")

    def final_score(self):
        return self.score


