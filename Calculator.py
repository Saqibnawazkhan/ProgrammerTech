import tkinter as tk
from tkinter import messagebox

# Function to update the expression in the display
def update_expression(symbol):
    current_text = display.get()
    new_text = current_text + str(symbol)
    display.delete(0, tk.END)
    display.insert(0, new_text)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def evaluate_expression():
    try:
        current_text = display.get()
        result = eval(current_text)  # Evaluate the expression
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        clear_display()

# Create the main window
root = tk.Tk()
root.title("My 1st Calculator")
root.configure(bg='light blue')  # Set background color

# Create the display entry
display = tk.Entry(root, width=20, font=("Berlin Sans FB", 24), bd=0, bg='#E7E6E6', fg='black', insertbackground='white', justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Style settings
button_font = ("Berlin Sans FB", 18)
button_bg = 'White'
button_fg = 'black'
button_active_bg = 'orange'
button_active_fg = 'blue'

# Create the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: update_expression(x) if x not in ['C', '='] else clear_display() if x == 'C' else evaluate_expression()
    tk.Button(
        root, text=button, padx=20, pady=20, font=button_font, bg=button_bg, fg=button_fg,
        activebackground=button_active_bg, activeforeground=button_active_fg, command=action, bd=0
    ).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI event loop
root.mainloop()
