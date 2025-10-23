from tkinter import *
window = Tk()
window.title('My first GUI program')
window.minsize(width=650, height=500)

#label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # Place the label on the window

my_label["text"] = "New Text" # Change the text of the label
my_label.config(text="Another New Text") # Another way to change the text

#button
def button_clicked():
    my_label.config(text=input.get()) # Another way to change the text
    
button = Button(text="Click Me", command=button_clicked)
button.pack() # Place the button on the window  

#entry
input = Entry(width=50)
input.pack() 
input.insert(END, string="Some text to start") # Add some text to begin with

def clear_text(event):
    """Deletes the initial text when the widget is left-clicked."""
    if input.get() == "Some text to start":
        input.delete(0, END)
        
input.bind("<Button-1>", clear_text)  # Bind left-click to clear_text function 

#text
text = Text(height=5, width=30) # Create a text box
text.pack()
text.focus()  # Place cursor in the text box
text.insert(END, "Example of multi-line text entry.") # Add some text to begin with
print(text.get('1.0', END)) # Get current value in text box from line 1, character 0 to end

#spinbox
def spinbox_used():
    print(spinbox.get()) # Gets the current value of the spinbox.
    
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale
def scale_used(value):
    print(value) # Gets the current value of the scale.
    
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack() 

#checkbox
def checkbox_used():
    print(checked_state.get()) # Prints 1 if checked, 0 if not checked.
    
checked_state = IntVar() # Create an integer variable to hold the state of the checkbox
checkbox = Checkbutton(text="Is On?", variable=checked_state,command=checkbox_used)
checkbox.pack()

#radiobutton
def radio_used():
    print(radio_state.get()) # Prints the selected radio button value.
    
radio_state = IntVar() # Create an integer variable to hold the state of the radiobuttons
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) # Gets the current selection from the listbox.
    
listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Cherry", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item) # Insert each fruit into the listbox
    
listbox.bind("<<ListboxSelect>>", listbox_used) # Bind the listbox selection event to the listbox_used function
listbox.pack()


window.mainloop() # Keeps the window open until we close it manually        