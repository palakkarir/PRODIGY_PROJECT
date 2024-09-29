import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_character_criteria = re.search(r'[@$!%*?&]', password) is not None

    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_character_criteria
    ])

    if strength_score == 5:
        strength = "Very Strong"
        feedback = "Great job! Your password is very strong."
    elif strength_score == 4:
        strength = "Strong"
        feedback = "Your password is strong, but consider adding more complexity."
    elif strength_score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Try to include Numbers,Symbols,characters."
    elif strength_score == 2:
        strength = "Weak"
        feedback = "Your password is weak. Include more character types."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. Please choose a more secure password."

    return strength, feedback

def check_password():
    password = entry_password.get()
    strength, feedback = assess_password_strength(password)
    
    messagebox.showinfo("Password Strength", f"Password Strength: {strength}\n{feedback}")

# window
root = tk.Tk()
root.title("Password Complexity Checker")

# widgets
label_instruction = tk.Label(root, text="Enter your password:")
label_instruction.pack(pady=10)

entry_password = tk.Entry(root, show='*', width=30)
entry_password.pack(pady=5)

button_check = tk.Button(root, text="Check Password Strength", command=check_password)
button_check.pack(pady=20)

# GUI event loop
root.mainloop()
