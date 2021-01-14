from tkinter import *
import tkinter.scrolledtext as st

root = Tk()

#Button action function
def myClick():
    myLabel1 = Label(root, text="")
    myLabel1 = Label(root, text=myEntry.get())
    myLabel1.grid(row=2, column=0)

root.geometry("800x800")

#Create scrolled text widget
text_area = st.ScrolledText(width=40, height=10)

#Create a label widget
#myLabel1 = Label(root)
myButton = Button(root, text="Enter", command=myClick)
myEntry = Entry(root)

#Orient widgets
#myLabel1.grid(row=0, column=0)
myButton.grid(row=1, column=1)
myEntry.grid(row=1, column=0)
text_area.grid(row=0, column=0)

#Run window
root.mainloop()

