from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
#instance of quiz_brain.py
Quiz = QuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print(f"you've completed the quiz\nyour final score was: {Quiz.score}/{Quiz.question_number}")
    