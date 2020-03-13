def btnClick(num):
   global op
 
   op=op+str(num)
   text_input.set(op)
   

def btnC():
    global op
    op=" "
    text_input.set("  ")

def checkC():
    global chances
    text_input=txtd.get()
    if int(text_input) > int(picked) :
       messagebox.showinfo('Message','Number is too large')
       chances=chances-1
       txt="Chances remaining :" +str(chances)
       label.configure(text=txt)
       btnC()
      


    elif int(text_input) < int(picked):
       messagebox.showinfo('Message','Number is too small')
       chances=chances - 1
       txt="Chances remaining :" +str(chances)
       label.configure(text=txt)
       btnC()

    elif int(text_input) in numbers:
       label.configure(text=txt)
    
    else:
       messagebox.showinfo('Message','Perfect Number')
   

    if chances == 0:
      
       messagebox.showinfo('Message','You Loose\nThe number was '+str(picked))
       window.destroy()

    
      
        
import random



picked=random.randrange(0,99)
        

import tkinter as tk
from tkinter import messagebox


window=tk.Tk()
window.configure(bg="orange")

window.geometry("600x500")
op=" "
chances=7



b0=tk.Button(window,bd=5,text="0",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(0))
b0.grid(row=5,column=2)
        
b1=tk.Button(window,bd=5,text="1",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(1))
b1.grid(row=2,column=1)

b2=tk.Button(window,bd=5,text="2",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(2))
b2.grid(row=2,column=2)

b3=tk.Button(window,bd=5,text="3",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(3))
b3.grid(row=2,column=3)

b4=tk.Button(window,bd=5,text="4",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(4))
b4.grid(row=3,column=1)

b5=tk.Button(window,bd=5,text="5",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(5))
b5.grid(row=3,column=2)

b6=tk.Button(window,bd=5,text="6",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(6))
b6.grid(row=3,column=3)

b7=tk.Button(window,bd=5,text="7",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(7))
b7.grid(row=4,column=1)

b8=tk.Button(window,bd=5,text="8",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(8))
b8.grid(row=4,column=2)

b9=tk.Button(window,bd=5,text="9",height=3,width=7,bg="light blue",fg="red",command=lambda:btnClick(9))
b9.grid(row=4,column=3)

text_input=tk.StringVar()
txtd=tk.Entry(bd=4,font=("arial",18,"bold"),textvariable=text_input,bg="white")
txtd.grid(row=1,column=0)



b11=tk.Button(window,bd=8,text="Submit",bg="light green",fg="red",font=("arial",12),height=3,width=10,command=checkC)
b11.grid(row=6,column=0)

bc=tk.Button(bd=8,text="C",bg="light green",fg="red",font=("arial",12,"bold"),width=8,height=2,command=btnC)
bc.grid(row=7,column=0)

label=tk.Label(window,text="Total chances are: 7",fg="purple",font=("arial",17))
label.grid(row=8,column=0)

label=tk.Label(window,text="Guess the number",fg="purple",font=("arial",17))
label.grid(row=0,column=0)



window.mainloop()
