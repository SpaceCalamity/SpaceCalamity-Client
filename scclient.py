from tkinter import *

root = Tk()

#Button action function
def myClick():
    myLabel1 = Label(root, text="")
    myLabel1 = Label(root, text=myEntry.get())
    myLabel1.grid(row=0, column=0)

root.geometry("800x800")

#Create scrolled text widget
text_area = ScrolledText(win, wrap=tk.WORD, width=40, height=10, font=("Times New Roman"))

#Create a label widget
myLabel1 = Label(root)
myButton = Button(root, text="Enter", command=myClick)
myEntry = Entry(root)




#Orient widgets
myLabel1.grid(row=0, column=0)
myButton.grid(row=1, column=1)
myEntry.grid(row=1, column=0)

#Run window
root.mainloop()

