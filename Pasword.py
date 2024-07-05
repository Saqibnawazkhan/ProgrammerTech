import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = "Strong"
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    password_label.config(text=password)

def clear_fields():
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_label.config(text="")

window = tk.Tk()
window.title("Digital Theme Password Generator")


bg_color = "gray"
fg_color = "white"
highlight_color = "#FFFFFF"
font_family = "Consolas"

window.configure(bg=bg_color)


name_label = tk.Label(window, text="Enter user name:", bg=bg_color, fg=highlight_color, font=(font_family, 12))
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')

name_entry = tk.Entry(window, bg=fg_color, fg=bg_color, font=(font_family, 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

length_label = tk.Label(window, text="Enter password length:", bg=bg_color, fg=highlight_color, font=(font_family, 12))
length_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')

length_entry = tk.Entry(window, bg=fg_color, fg=bg_color, font=(font_family, 12))
length_entry.grid(row=1, column=1, padx=5, pady=5)


generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg=highlight_color, fg=bg_color, font=(font_family, 12))
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

clear_button = tk.Button(window, text="Clear Fields", command=clear_fields, bg=highlight_color, fg=bg_color, font=(font_family, 12))
clear_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


password_label = tk.Label(window, text="", bg=bg_color, fg=highlight_color, font=(font_family, 12))
password_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
