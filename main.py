from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for questions in question_data:
    new_q_answer = Question(questions["question"], questions["correct_answer"])
    question_bank.append(new_q_answer)



quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
