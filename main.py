import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in data.sorular:
    question_text = question["text"]
    question_answers = question["answers"]
    question_correct_answer = question["correct_answer"]
    new_question = Question(question_text, question_answers, question_correct_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
