from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_b: QuizBrain):
        self.score = 0
        self.quiz = quiz_b
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("quiz brain")

        self.score_label = Label(
            text=f"score:{self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="start", fill=THEME_COLOR, font=("Arial", 15, "italic"))

        self.Image_true = PhotoImage(file="true.png")
        self.button = Button(image=self.Image_true, command=self.true_button)
        self.button.grid(column=0, row=2)
        self.button.config(highlightthickness=0)

        self.Image_false = PhotoImage(file="false.png")
        self.button = Button(image=self.Image_false, command=self.false_button)
        self.button.grid(column=1, row=2)
        self.get_next_qus()
        self.button.config(highlightthickness=0)

        self.window.mainloop()

    def get_next_qus(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="end")

    def true_button(self):
        answer = self.quiz.check_answer("true")
        self.give_feedback(answer)

    def false_button(self):
        answer = self.quiz.check_answer("false")

        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.score += 1
            self.score_label.config(text=f"score:{self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_qus)
