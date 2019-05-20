from tkinter import*
import tkinter.messagebox
import home as h

def login_new():
    root1=Tk()
    root1.title("Login")
    class Application:
        def __init__(self,master):
            self.master=master
        
            self.left=Frame(self.master,width=1600,height=720,bg='lightblue')
            self.left.pack(side=LEFT)
        
            self.label_username=Label(self.master,text="Login",bg='lightblue',font=('arial 30 bold'))
            self.label_username.place(x=600,y=100)
        
            self.label_username=Label(self.master,text="Username:",bg='lightblue',font=('arial 15 bold'))
            self.label_username.place(x=500,y=200)
        
            self.label_password=Label(self.master,text="Password:",bg='lightblue',font=('arial 15 bold'))
            self.label_password.place(x=500,y=250)
        
            self.ent1_user=Entry(self.master,width=30)
            self.ent1_user.place(x=650,y=205)
        
            self.ent2_pass=Entry(self.master,width=30,show="*")
            self.ent2_pass.place(x=650,y=255)
        
            self.btn_submit=Button(master,text="Login",width=10,height=1,command=lambda:self.login())
            self.btn_submit.place(x=600,y=300)
        
        def login(self):
        
                self.username = self.ent1_user.get()
                self.password = self.ent2_pass.get()
                if (self.username == 'admin' and self.password == 'admin'):
    
                        #root1.withdraw()
                        h.home(self.master)   

                else:
                        tkinter.messagebox.showerror('Alert', 'Invalid Login')
            
    
        
    b=Application(root1)        
    root1.geometry("1600x720+0+0")
    root1.mainloop()
login_new()