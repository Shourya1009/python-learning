# digital_clock.py
import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # 24-hour format
    label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

# Create window
root = tk.Tk()
root.title("⏰ Digital Clock")
root.geometry("300x150")
root.resizable(False, False)

# Label for time
label = tk.Label(root, font=("Arial", 48), bg="black", fg="cyan")
label.pack(expand=True, fill="both")

update_time()
root.mainloop()
