from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer1 = None
timer_is_on = True
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global timer_is_on
    timer_is_on = True
    window.after_cancel(timer1)
    canvas.itemconfig(timer_text, text=f"00:00")
    title.config(text="Timer", fg=GREEN)
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_butten():
    if timer_is_on:
        global reps
        reps = 0
        start_timer()


def start_timer():
    global reps
    reps += 1
    if reps > 8:
        pass
    elif reps % 2 != 0:
        timer(0, 25)
        title.config(text=f"Work Time", fg=RED)
    elif reps == 8:
        timer(0, LONG_BREAK_MIN)
        title.config(text=f"Long Break", fg=PINK)
    elif reps % 2 == 0:
        timer(0, SHORT_BREAK_MIN)
        title.config(text=f"Short Break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer(second, min1):
    global timer_is_on
    timer_is_on = False
    if min1 < 10 and second < 10:
        canvas.itemconfig(timer_text, text=f"0{min1}:0{second}")
    elif min1 < 10:
        canvas.itemconfig(timer_text, text=f"0{min1}:{second}")
    elif second < 10:
        canvas.itemconfig(timer_text, text=f"{min1}:0{second}")
    else:
        canvas.itemconfig(timer_text, text=f"{min1}:{second}")
    if second > 0:
        global timer1
        timer1 = window.after(1000, timer, second-1, min1)
    elif min1 > 0:
        second = 60
        timer(second, min1-1)
    elif min1 == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔️"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)


title = Label(text="timer", fg=GREEN, font=(FONT_NAME, 50))
title.config(bg=YELLOW)
title.grid(column=1, row=0)
window.title("tomato")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
button1 = Button(text="reset", command=reset)
button1.grid(column=3, row=3)
button1.config(border=0)

button2 = Button(text="start", command=start_butten)
button2.config(border=0)
button2.grid(column=0, row=3,)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)


window.mainloop()
