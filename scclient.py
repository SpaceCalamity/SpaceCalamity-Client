from tkinter import *
import tkinter.scrolledtext as st

root = Tk()

#Button action function
def myClick():
    myLabel1 = Label(root, text="")
    myLabel1 = Label(root, text=myEntry.get())
    myLabel1.grid(row=2, column=0)

#Create frames
frame0 = LabelFrame(root) 
frame1 = LabelFrame(frame0, text="Main Console", padx=10, pady=10) 
frame2 = LabelFrame(frame0, text="Status", padx=10, pady=10) 

#Create scrolled text widgets
text_area1 = st.ScrolledText(frame1, width=40, height=10)
text_area1.insert(INSERT, "SHOW ME WHAT YOU GOT CAPTAIN") 
text_area1.configure(state='disabled')
text_area2 = st.ScrolledText(frame2, width=40, height=10)
text_area2.insert(INSERT, "SHIP'S FINE") 
text_area2.configure(state='disabled')



#Create other widgets
myButton = Button(root, text="Enter", command=myClick)
myEntry = Entry(root, width=50)

#Orient widgets
#myButton.grid(row=1, column=1)
frame0.grid(row=0, column=0, columnspan=2)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
myButton.grid(row=1, column=1)
myEntry.grid(row=1, column=0)
text_area1.pack()
text_area2.pack()

#Run window
root.mainloop()

