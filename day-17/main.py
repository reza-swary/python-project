from data import question_data
from question import Question
from quex import QuizBrain
qus_b =[]
for x in question_data:
    question_text = x["text"]
    question_answer= x["answer"]
    new_question = Question(question_text,question_answer)
    qus_b.append(new_question)

quiz = QuizBrain(qus_b)
while quiz.still_has_qus():
    quiz.next_qus()  