import tkinter as tk
import math

def calculate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        result_label.config(text="Error: " + str(e))
    except Exception as e:
        result_label.config(text="An error occurred: " + str(e))

# Create main window
root = tk.Tk()
root.title(" Advanced Calculator")

# Function to handle button click events
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            result_label.config(text="Result: " + str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            result_label.config(text="An error occurred: " + str(e))
    elif text == "C":
        entry.delete(0, tk.END)
        result_label.config(text="")
    elif text == "DEL":
        entry.delete(len(entry.get()) - 1)
    else:
        entry.insert(tk.END, text)

# Create entry field
entry = tk.Entry(root, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Create buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("=", 5, 3),
    ("DEL", 6, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)
    button.bind("<Button-1>", button_click)

# Create result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

# Run the GUI loop
root.mainloop()

