from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    text = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),

        }

    }
    save_p = messagebox.askyesno(
        title="password manager", message="do you want to save your password")
    if save_p:
        try:
            with open("passwords.json") as data:
                new_text = json.load(data)
                new_text.update(text)
                print(new_text)
            with open("passwords.json", "w")as data:
                json.dump(new_text, data)
        except:
            with open("passwords.json", "w")as data:
                json.dump(text, data)
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manger")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_name = Label(text="website:")
website_name.grid(column=0, row=1)

email_name = Label(text="Email/Username:")
email_name.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

click1 = Button(text="Generate Password", border=1, command=generator)
click1.grid(column=2, row=3)

click2 = Button(text="Add", pady=0, width=34, border=1, height=1, command=save)
click2.grid(column=1, row=4, columnspan=2)


window.mainloop()
