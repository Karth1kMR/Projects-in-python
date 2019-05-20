from tkinter import *
import tkinter.messagebox
import appointment as appoint
import modify as m
class Home:
    def __init__(self,master):
        self.master=master
        self.left=Frame(self.master,width=1600,height=720,bg='lightblue')
        self.left.pack(side=LEFT)
        self.label_username=Label(self.master,text="SS Hospital",bg='lightblue',font=('arial 30 bold'))
        self.label_username.place(x=600,y=0)
        self.btn_add=Button(self.master,text="ADD Appointment",width=25,height=2,command=lambda:appoint.app(self.master))
        self.btn_add.place(x=600,y=450)
        self.btn_update=Button(self.master,text="Modify Record",width=25,height=2,command=lambda:m.modi(self.master))
        self.btn_update.place(x=600,y=500)

def home(old):
    old.destroy()
    root4=Tk()
    root4.title("Home page")
    b=Home(root4)
    root4.geometry("1600x720+0+0")
    root4.mainloop()