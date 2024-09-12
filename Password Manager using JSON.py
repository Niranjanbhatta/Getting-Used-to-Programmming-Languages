from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import choice, randint, shuffle
import pyperclip
import json

# Function to generate password
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)  # Clear previous password
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy password to clipboard

# Function to save data
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# Function to find password
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# UI setup
window = Tk()
window.title("Password Manager")
window.geometry("500x400")
window.config(bg="#2c3e50")

# Custom Style for Buttons and Entry
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10, "bold"), background="#16a085", foreground="white")
style.map("TButton", background=[('active', '#1abc9c')])

style.configure("TEntry", foreground="#ecf0f1", fieldbackground="#34495e", font=("Helvetica", 12))

# Canvas (dynamic background)
canvas = Canvas(window, width=500, height=200, bg="#2c3e50", highlightthickness=0)
canvas.create_text(250, 100, text="Secure Password Manager", fill="#ecf0f1", font=("Helvetica", 20, "bold"))
canvas.grid(row=0, column=0, columnspan=3, pady=20)

# Labels
website_label = Label(text="Website:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 10, "bold"))
website_label.grid(row=1, column=0, padx=10, pady=5)
email_label = Label(text="Email/Username:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 10, "bold"))
email_label.grid(row=2, column=0, padx=10, pady=5)
password_label = Label(text="Password:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 10, "bold"))
password_label.grid(row=3, column=0, padx=10, pady=5)

# Entry fields with modern style
website_entry = ttk.Entry(window, width=35, style="TEntry")
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = ttk.Entry(window, width=35, style="TEntry")
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "niranjan@gmail.com")

password_entry = ttk.Entry(window, width=21, style="TEntry")
password_entry.grid(row=3, column=1, pady=5)

# Button hover effect
def on_enter(e):
    e.widget['background'] = '#1abc9c'

def on_leave(e):
    e.widget['background'] = '#16a085'

# Function to create rounded buttons
def create_rounded_button(text, command, row, column, col_span):
    btn = Button(window, text=text, command=command, bg="#16a085", fg="white", font=("Helvetica", 10, "bold"), bd=0, relief="flat")
    btn.grid(row=row, column=column, columnspan=col_span, pady=10, padx=10)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Create rounded buttons using grid
create_rounded_button("Search", find_password, 4, 0, 1)
create_rounded_button("Generate Password", generate_password, 4, 1, 1)
create_rounded_button("Add", save, 4, 2, 1)

window.mainloop()
