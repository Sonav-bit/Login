from tkinter import*
root=Tk()
root.title('Login app')
root.geometry('400x400')
l1=Label(root,text='Enter your username')
l2=Label(root,text='Enter your email')
l3=Label(root,text='Enter your password')
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)

def greet():
    name=e1.get()
    message="Hey"+name+'Congrats'
    l4=Label(root,text=message)
    l4.grid(row=4,column=2)
b1=Button(root,text='Display',command=greet)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
b1.grid(row=3,column=2)
root.mainloop()