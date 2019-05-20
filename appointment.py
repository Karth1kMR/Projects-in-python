from tkinter import *
import sqlite3
import tkinter.messagebox
 # connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

ids = []

def app(old):
    
    root3= Tk()
    
    class Application:
        def __init__(self,master):
            self.master=master

            #creating the frames in the master
            self.left=Frame(master,width=1000,height=720,bg='#D8BFD8')
            self.left.pack(side=LEFT)
        
            self.right=Frame(master,width=1200,height=720)
            self.right.pack(side=LEFT)


            #labels for the window
            self.heading=Label(self.left,text="AR Hospital Appointment",font=('arial 40 bold'),fg='black',bg='#D8BFD8')
            self.heading.place(x=120,y=0)

            #Patient's name
            self.name=Label(self.left,text="Patient's name",font=('arial 18 bold'),fg='black',bg='#D8BFD8')
            self.name.place(x=200,y=100)

            #age
            self.age=Label(self.left,text="Age",font=('arial 18 bold'),fg='black',bg='#D8BFD8')
            self.age.place(x=200,y=140)

            #gender
            self.gender=Label(self.left,text="Gender",font=('arial 18 bold'),fg='black',bg='#D8BFD8')
            self.gender.place(x=200,y=180)

            #location
            self.location=Label(self.left,text="Location",font=('arial 18 bold'),fg='black',bg='#D8BFD8')
            self.location.place(x=200,y=220)

            #appointment time
            self.time=Label(self.left,text="Appointment time",font=('arial 18 bold'),fg='black',bg='#D8BFD8')
            self.time.place(x=200,y=260)

            #phone
            self.time=Label(self.left,text="Phone Number",font=('arial 18 bold'),fg='black',bg='#D8BFD8')
            self.time.place(x=200,y=300)

            #entries for labels
            self.name_ent=Entry(self.left,width=30)
            self.name_ent.place(x=500,y=105)

            self.age_ent=Entry(self.left,width=30)
            self.age_ent.place(x=500,y=145)

        
            self.gender_ent=Entry(self.left,width=30)
            self.gender_ent.place(x=500,y=185)

            self.location_ent=Entry(self.left,width=30)
            self.location_ent.place(x=500,y=225)

            self.time_ent=Entry(self.left,width=30)
            self.time_ent.place(x=500,y=265)

            self.phone_ent=Entry(self.left,width=30)
            self.phone_ent.place(x=500,y=305)

            #submit button
            self.submit=Button(self.left,text="Add Appointment",width=20,height=2,bg='steelblue',command=self.add_appointment)
            self.submit.place(x=375,y=360)
            
            #clear button
            self.clear=Button(self.left,text="Clear all",width=6,height=1,command=self.clear_all)
            self.clear.place(x=650,y=365)
            
            sql2 = "SELECT ID FROM appointments "
            self.result = c.execute(sql2)
            for self.row in self.result:
                self.id = self.row[0]
                ids.append(self.id)
            
            self.new = sorted(ids)
            self.final_id = self.new[len(ids)-1]
            #displaying logs
            self.box=Text(self.right,width=50,height=40)
            self.box.place(x=20,y=30)
            self.box.insert(END,"Total Appointments till now : "+str(self.final_id))
            
        def clear_all(self):
            self.name_ent.delete(0,END)
            self.age_ent.delete(0,END)
            self.gender_ent.delete(0,END)
            self.location_ent.delete(0,END)
            self.time_ent.delete(0,END)
            self.phone_ent.delete(0,END)
        
            #getting number of appointments fixed to view in log
           
            
        
        
        def add_appointment(self):
            #getting user inputs
            self.val1=self.name_ent.get()
            self.val2=self.age_ent.get()
            self.val3=self.gender_ent.get()
            self.val4=self.location_ent.get()
            self.val5=self.time_ent.get()
            self.val6=self.phone_ent.get()
            #checking if the user input is empty
            if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' :
                tkinter.messagebox.showinfo("Warning","Please fill the required field")
            else:
                sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
                c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )
            
            self.box.insert(END,'\n'+'Appointment fixed for '+str(self.val1)+' at '+str(self.val5))
            
            

#creating the object

    b=Application(root3)


#resolution of the window
    root3.geometry("1600x720+0+0")

#end of the loop
    root3.mainloop()
