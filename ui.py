from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 14, "italic")


class QuizUI:
    # quiz_brain: QuizBrain quiere decir que solo aceptara objetos tipo QuizBrain.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        right_button = PhotoImage(file="images/true.png")
        wrong_button = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, highlightthickness=0, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Place holder",
                                                     font=QUESTION_FONT,
                                                     width=275,
                                                     justify="center",
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.right_button = Button(image=right_button, highlightthickness=0, command=self.right_choice)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_button, highlightthickness=0, command=self.wrong_choice)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def right_choice(self):
        if self.quiz.still_has_questions():
            answer = self.quiz.check_answer("True")
            self.score += answer
            self.score_label.config(text=f"Score: {self.score}")

            self.give_feedback(answer)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You scored {self.score} points.\nCongratulations!")

    def wrong_choice(self):
        if self.quiz.still_has_questions():
            answer = self.quiz.check_answer("False")
            self.score += answer
            self.score_label.config(text=f"Score: {self.score}")

            self.give_feedback(answer)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You scored {self.score} points.\nCongratulations!")

    def give_feedback(self, answer):
        if answer == 1:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)


