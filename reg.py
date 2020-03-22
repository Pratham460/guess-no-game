def buttonC():
   text_input1=txtd1.get()
   text_input2=txtd2.get()
   text_input4=txtd4.get()
   print(text_input1)
   print(text_input2)
   print(combo.get())
   print(text_input4)
   if var.get()==1:
       print('Male')
   else:
       print('Female')


import tkinter as tk
from tkinter.ttk import *

window=tk.Tk()
window.title("Student Registration Form")
window.geometry("500x500")

label1=tk.Label(window,text="Name")
label1.grid(row=1,column=1,padx=10,pady=10)

label1=tk.Label(window,text="PRN")
label1.grid(row=2,column=1,padx=10,pady=10)

label1=tk.Label(window,text="College")
label1.grid(row=3,column=1,padx=10,pady=10)

label1=tk.Label(window,text="Dept")
label1.grid(row=4,column=1,padx=10,pady=10)

label1=tk.Label(window,text="Gender")
label1.grid(row=5,column=1,padx=3,pady=10)

text_input1=tk.StringVar()
txtd1=tk.Entry(bd=2,font=("arial",10),textvariable=text_input1,bg="white")
txtd1.grid(row=1,column=2,padx=10,pady=10)

text_input2=tk.IntVar()
txtd2=tk.Entry(bd=2,font=("arial",10),textvariable=text_input2,bg="white")
txtd2.grid(row=2,column=2,padx=10,pady=10)


text_input4=tk.StringVar()
txtd4=tk.Entry(bd=2,font=("arial",10),textvariable=text_input4,bg="white")
txtd4.grid(row=4,column=2,padx=10,pady=10)

var=tk.IntVar()
rad1=tk.Radiobutton(window,text='Male',variable=var,value=1)
rad1.grid(row=5,column=2)
rad2=tk.Radiobutton(window,text='Female',variable=var,value=2)
rad2.grid(row=5,column=3)

combo=Combobox(window)
combo['values']=('DY Patil','SIES GST','RAIT','VJTI')
combo.grid(row=3,column=2,padx=10,pady=10)



button=tk.Button(window,text='Submit',width=10,height=3,command=buttonC)
button.grid(row=6,column=2,padx=10,pady=20)
