from tkinter import *
import tkinter.messagebox

from numpy import var
root=Tk()
root.title('tic tac toe game')
bclick=True
flag=0
playerA=StringVar()
playerB=StringVar()
playerA_name=Entry(root,textvariable=playerA,bd=5)
playerB_name=Entry(root,textvariable=playerB,bd=5)
playerA_name.grid(row=1,column=1,columnspan=8)
playerB_name.grid(row=2,column=1,columnspan=8)

def buttonclick(button):
    global bclick,flag
    if(button['text']==' ' and bclick==True):
        button['text']='X'
        bclick=False
        flag=flag+1
        checkForWin()
    if(button['text']==' ' and bclick==False):
        button['text']='O'
        bclick=True
        flag=flag+1
        checkForWin()

def disableButtons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def checkForWin():
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
    button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
    button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
    button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
    button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
    button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
    button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
    button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
        disableButtons()
        tkinter.messagebox.showinfo('tic tac toe',playerA.get()+' wins')
    if(button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or
    button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
    button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
    button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
    button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
    button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
    button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
    button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        disableButtons()
        tkinter.messagebox.showinfo('tic tac toe',playerB.get()+' wins')
    if(flag==9):
        tkinter.messagebox.showinfo('tic tac toe','Its a tie')



label1=Label(root,text='Player 1:',font='Times 20 bold',bg='white',fg='black',height=1,width=8)
label1.grid(row=1,column=0)
label2=Label(root,text='Player 2:',font='Times 20 bold',bg='white',fg='black',height=1,width=8)
label2.grid(row=2,column=0)

button1=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button1))
button1.grid(row=3,column=0)
button2=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button2))
button2.grid(row=3,column=1)
button3=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button3))
button3.grid(row=3,column=2)
button4=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button4))
button4.grid(row=4,column=0)
button5=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button5))
button5.grid(row=4,column=1)
button6=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button6))
button6.grid(row=4,column=2)
button7=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button7))
button7.grid(row=5,column=0)
button8=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button8))
button8.grid(row=5,column=1)
button9=Button(root,text=' ',font='Times 20 bold',bg='grey',fg='white',height=4,width=8,command=lambda:buttonclick(button9))
button9.grid(row=5,column=2)

root.mainloop()