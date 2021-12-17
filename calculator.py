import tkinter as tkt
from tkinter import *
t=tkt.Tk()

equation=StringVar()
expression=""
entry=Entry(t,font=("times new roman",15),width=35,justify='right',textvariable=equation)
entry.place(x=25,y=35)
def btn_click(num):
   global expression
   expression=expression+str(num)
   equation.set(expression)
def all_clear():
    global expression
    expression=""
    equation.set(expression)
def cal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("wrong")
        expression = ""



t.title("calculator")
t.geometry("500x500")
bc=Button(t,text='close',bd='5',command=t.destroy)
bc.pack(side='bottom')
b1=Button(t,text='1',bd='3',padx=15,pady=15,command=lambda:btn_click(1))
b1.place(x=50,y=100)
b2=Button(t,text='2',bd='3',padx=15,pady=15,command=lambda:btn_click(2))
b2.place(x=100,y=100)
b3=Button(t,text='3',bd='3',padx=15,pady='15',command=lambda:btn_click(3))
b3.place(x=150,y=100)
b4=Button(t,text='4',bd='3',padx=15,pady='15',command=lambda:btn_click(4))
b4.place(x=50,y=155)
b5=Button(t,text='5',bd='3',padx=15,pady='15',command=lambda:btn_click(5))
b5.place(x=100,y=155)
b6=Button(t,text='6',bd='3',padx=15,pady='15',command=lambda:btn_click(6))
b6.place(x=150,y=155)
b7=Button(t,text='7',bd='3',padx=15,pady='15',command=lambda:btn_click(7))
b7.place(x=50,y=210)
b8=Button(t,text='8',bd='3',padx=15,pady='15',command=lambda:btn_click(8))
b8.place(x=100,y=210)
b9=Button(t,text='9',bd='3',padx=15,pady='15',command=lambda:btn_click(9))
b9.place(x=150,y=210)
bdel=Button(t,text='del',bd='3',padx=10,pady='15',command=lambda:btn_click())
bdel.place(x=50,y=265)

b0=Button(t,text='0',bd='3',padx=15,pady='15',command=lambda:btn_click(0))
b0.place(x=100,y=265)
bp=Button(t,text='+',bd='3',padx=14.2,pady='15',command=lambda:btn_click("+"))
bp.place(x=200,y=100)
bs=Button(t,text='-',bd='3',padx=16,pady='15',command=lambda:btn_click("-"))
bs.place(x=200,y=155)
bm=Button(t,text='*',bd='3',padx=16,pady='15',command=lambda:btn_click("*"))
bm.place(x=200,y=210)
bd=Button(t,text='/',bd='3',padx=16,pady='15',command=lambda:btn_click("/"))
bd.place(x=200,y=265)
bmo=Button(t,text='%',bd='3',padx=13,pady='15',command=lambda:btn_click("%"))
bmo.place(x=150,y=265)
be=Button(t,text='=',bd='3',padx=40,pady='15',command=lambda:cal())
be.place(x=150,y=320)
bclr=Button(t,text='clear',bd='3',padx=31,pady='15',command=lambda:all_clear())
bclr.place(x=50,y=320)








t.mainloop()