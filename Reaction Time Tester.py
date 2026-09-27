import tkinter as tk
import time
import random

time_taken = 0
game_active = True
valid_click = False
start_time = 0
test_running = False

root = tk.Tk()
root.title("Reaction Time Tester")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

task_bar_height = 50
window_height = screen_height - task_bar_height

root.geometry(f"{screen_width}x{window_height}+0+0")

title = tk.Label(root, text="REACTION TIME TESTER", font=("Arial", 40))
title.pack()

instructions = tk.Label(root, text="Click when the text changes!\nThe text will change between 1 to 5 seconds!", font=("Arial", 20))
instructions.pack(pady=20)

def start_test():
    global start_time, valid_click, test_running
    valid_click = False
    test_running = True
    start_button.config(state="disabled")
    the_button.config(state="normal")
    wait_time = random.randint(1, 5)
    instructions.config(text="Get ready...")
    root.after(wait_time * 1000, show_click_button)

def show_click_button():
    global start_time, valid_click
    if test_running:
        start_time = time.time()
        valid_click = True
        instructions.config(text="CLICK NOW!")

def end_test():
    global valid_click, test_running
    if not test_running:
        return  # Ignore clicks if test isn't running

    test_running = False
    the_button.config(state="disabled")

    if valid_click:
        reaction_time = time.time() - start_time
        instructions.config(text=f"Your reaction time was {reaction_time:.4f} seconds!")
        valid_click = False
        start_button.config(state="normal")
        start_button.config(text="Try Again")
    else:
        instructions.config(text="Too early! You must wait for the signal.")
        valid_click = False
        start_button.config(state="normal")
        start_button.config(text="Try Again")

start_button = tk.Button(root, text="Start", font=("Arial", 20), height=3, width=10, command=start_test)
start_button.pack(pady=20)

the_button = tk.Button(root, text="CLICK ME", font=("Arial", 20), height=15, width=30, state="disabled", command=end_test)
the_button.pack(pady=20)

root.mainloop()
