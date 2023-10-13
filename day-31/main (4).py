from pandas import *
from tkinter import *
from random import *
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = read_csv("words_to_learn.csv")
except:
    data = read_csv("french_words.csv")
finally:
    doc = data.to_dict(orient="records")


def next_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(doc)
    canvas.itemconfig(canvas_image, image=image_front)
    canvas.itemconfig(card_title, text="French", fill=BACKGROUND_COLOR)
    canvas.itemconfig(card_word, text=word["French"], fill=BACKGROUND_COLOR)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")


def know_card():
    doc.remove(word)
    data1 = DataFrame(doc)
    data1.to_csv("words_to_learn.csv", index=False)
    print(len(doc))
    next_word()


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)


image_right = PhotoImage(file="right.png")
image_wrong = PhotoImage(file="wrong.png")
image_back = PhotoImage(file="card_back.png")
image_front = PhotoImage(file="card_front.png")


canvas_image = canvas.create_image(400, 263, image=image_front)
card_title = canvas.create_text(
    400, 150, text=f"title", font=("Ariel", 50, "italic"))
card_word = canvas.create_text(
    400, 263, text=f"world", font=("Ariel", 100, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, flip_card)

button1 = Button(image=image_right)
button1.grid(column=1, row=1)
button1.config(border=0, highlightthickness=0, command=know_card)
button2 = Button(image=image_wrong)
button2.grid(column=0, row=1)
button2.config(border=0, highlightthickness=0, command=next_word)
next_word()

window.mainloop()
