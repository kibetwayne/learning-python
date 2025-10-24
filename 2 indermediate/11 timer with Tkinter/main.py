from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "green"
GREY = "#D3D3D3"
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


#! TIMER RESET 
def reset_timer():
    """Resets the timer to its initial state."""
    global reps
    window.after_cancel(timer) # Cancel the ongoing timer
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0
    
#! TIMER MECHANISM 
def start_timer():
    """Starts the timer mechanism."""
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
        
#! COUNTDOWN MECHANISM 
def count_down(count):
    """Counts down the time and updates the canvas text."""
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) 
    else:
        start_timer()
        if reps % 2 == 0:
            marks = ""
            work_sessions = math.floor(reps / 2) # Calculate completed work sessions
            for _ in range(work_sessions):
                marks += "✔️"
            check_marks.config(text=marks)
        
#! UI SETUP 
window = Tk()
window.title("Pomodoro")
window.config(padx=5, pady=5, bg=GREY)

title_label = Label(text="Timer", fg=GREEN, bg=GREY, font=(FONT, 20, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=360, height=360, bg=GREY, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 180, image=tomato_img)
timer_text = canvas.create_text(190, 200, text="00:00", fill="white", font=(FONT, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=GREY, font=(FONT, 20, "bold"))
check_marks.grid(column=1, row=3)
























window.mainloop()
