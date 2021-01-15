from tkinter import *

root = Tk()
root.title('Welcome to Space Calamity!')
#root.iconbitmap('')

servip=StringVar()
servport=StringVar()

#Create widgets
frame0 = LabelFrame(root, padx=10, pady=10)
frame1 = LabelFrame(root, padx=10, pady=10)
label0 = Label(frame0, text="Server IP:", anchor="e", justify=RIGHT)
label1 = Label(frame0, text="Server Port:", anchor="e", justify=RIGHT)
entry0 = Entry(frame0, width=15)
entry1 = Entry(frame0, width=7)
entry0.insert(0, "0.0.0.0")
entry1.insert(0, "#####")

label2 = Label(frame1, text="Username:", anchor="e", justify=RIGHT)
label3 = Label(frame1, text="Password:", anchor="e", justify=RIGHT)
entry2 = Entry(frame1, width=15)
entry3 = Entry(frame1, width=15, show='*')

button0 = Button(root, text='Enter')

#Orient widgets
frame0.grid(row=0, column=0)
label0.grid(row=0, column=0)
label1.grid(row=1, column=0)
entry0.grid(row=0, column=1)
entry1.grid(row=1, column=1)

frame1.grid(row=1, column=0)
label2.grid(row=0, column=0)
label3.grid(row=1, column=0)
entry2.grid(row=0, column=1)
entry3.grid(row=1, column=1)

button0.grid(row=2, column=0)

root.mainloop()
