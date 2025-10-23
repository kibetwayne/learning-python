from tkinter import *
window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=10, pady=10) #add space around every widget

def miles_to_km():
    miles = entry.get()
    miles_float = float(miles)
    km  = round(miles_float * 1.60934, 2)
    result_label.config(text=f'{km}')
    
def clear(event):
    """Deletes the initial text when the widget is left-clicked."""
    if entry.get() == '0':
        entry.delete(0, END)
        

entry = Entry()
entry.insert(END, string="0") # Add some text to begin with
entry.grid(column=1, row=0, padx=10, pady=10)

miles_label = Label(text = 'Miles' )
miles_label.grid(column=2, row=0, padx=10, pady=10)

equal_label = Label(text = 'is equal to' )
equal_label.grid(column=0, row=1, padx=10, pady=10)

result_label = Label(text = '0')
result_label.grid(column=1, row=1, padx=10, pady=10)

km_label = Label(text = 'Km')
km_label.grid(column=2, row=1, padx=10, pady=10)

calc_button = Button(text = 'Calculate', command=miles_to_km)
calc_button.grid(column=1, row=2, padx=10, pady=10)

entry.bind("<Button-1>", clear)  # Bind left-click to clear_text function 






window.mainloop()   