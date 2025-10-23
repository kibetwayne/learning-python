from tkinter import *
window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=10, pady=10) #add space around every widget

def button_clicked():
    my_label.config(text=input.get()) # Another way to change the text

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="Another New Text") # Another way to change the text
my_label.config(padx=30, pady=30)

# my_label.pack() # Place the label on the window
# my_label.place(x=0, y=0)  # Place the label at an exact position
my_label.grid(column=0, row=0)

#button 1
button = Button(text="Click Me", command=button_clicked)

button.grid(column=1, row=1) 

#button 2
button2 = Button(text = 'button 2')
button2.grid(column=2, row=0)

#entry
input = Entry(width=50)
print(input.get()) # Gets the text in the entry
input.grid(column=3, row=3)







window.mainloop() # Keeps the window open until we close it manually
