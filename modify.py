from tkinter import *
import tkinter.messagebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
def modi(old):
    
    root2= Tk()
    class Modification:
        def __init__(self, master):
            self.master = master
            # heading label
            self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
            self.heading.place(x=400, y=0)

            # search criteria -->name 
            self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
            self.name.place(x=200, y=100)

            # entry for  the name
            self.namenet = Entry(master, width=30)
            self.namenet.place(x=475, y=105)
        
            # search button
            self.search = Button(master, text="Search", width=12, height=1, bg='steelblue',command=self.search_db)
            self.search.place(x=250, y=175)

            # update button
            self.update = Button(master, text="Update", width=12, height=1, bg='steelblue',command=self.update1_db)
            self.update.place(x=450, y=175)
        
            # button to delete
            self.delete = Button(self.master, text="Delete", width=12, height=1, bg='red', command=self.delete_db)
            self.delete.place(x=650, y=175)
            
            # button to clear
            self.clear = Button(self.master, text="Clear", width=12, height=1, command=self.clear_db)
            self.clear.place(x=670, y=100)
            
            
        
          
        #clear function
        def clear_db(self):
           
            self.namenet.delete(0,END)
            self.disp1.delete(0,END)

        #search function
        def search_db(self):
            self.input=self.namenet.get()
            self.disp1=" "
            self.disp2=""
            self.disp3=" "
            self.disp4=""
            self.disp5=" "
            self.disp6=""
            if self.input=='':
                tkinter.messagebox.showinfo("Warning","Please enter Patient's name to be searched")
            else:
                sql1 = "SELECT * FROM appointments WHERE name LIKE ?"
                self.res = c.execute(sql1, (self.input,))
                for self.row in self.res:
                    self.name1 = self.row[1]
                    self.age = self.row[2]
                    self.gender = self.row[3]
                    self.location = self.row[4]
                    self.time = self.row[6]
                    self.phone = self.row[5]
                #print(self.result)
                
                self.uname = Label(self.master, text="Patient's Name:", font=('arial 18 bold'))
                self.uname.place(x=0, y=240)
        
                self.uage = Label(self.master, text="Age:", font=('arial 18 bold'))
                self.uage.place(x=0, y=280)
        
                self.ugender = Label(self.master, text="Gender:", font=('arial 18 bold'))
                self.ugender.place(x=0, y=320)

                self.ulocation = Label(self.master, text="Location:", font=('arial 18 bold'))
                self.ulocation.place(x=0, y=360)

                self.utime = Label(self.master, text="Phone Number:", font=('arial 18 bold'))
                self.utime.place(x=0, y=400)

                self.uphone = Label(self.master, text="Appointment Time:", font=('arial 18 bold'))
                self.uphone.place(x=0, y=440)
        
                self.disp1 = Label(self.master, text=self.name1, font=('arial 18'))
                self.disp1.place(x=240, y=245) 
        
                self.disp2 = Label(self.master, text=self.age, font=('arial 18'))
                self.disp2.place(x=240, y=285)
        
                self.disp3 = Label(self.master, text=self.gender, font=('arial 18'))
                self.disp3.place(x=240, y=325)   
        
                self.disp4 = Label(self.master, text=self.location, font=('arial 18'))
                self.disp4.place(x=240, y=365) 
        
                self.disp5 = Label(self.master, text=self.time, font=('arial 18'))
                self.disp5.place(x=240, y=405)
        
                self.disp6 = Label(self.master, text=self.phone, font=('arial 18'))
                self.disp6.place(x=240, y=445)
        
                
                
                
            
        #update function
        def update1_db(self):
            self.input=self.namenet.get()
            if self.input=='':
                tkinter.messagebox.showinfo("Warning","Please enter Patient's name to update ")
            else:
                sql = "SELECT * FROM appointments WHERE name LIKE ?"
                self.res = c.execute(sql, (self.input,))
                for self.row in self.res:
                    self.name1 = self.row[1]
                    self.age = self.row[2]
                    self.gender = self.row[3]
                    self.location = self.row[4]
                    self.time = self.row[6]
                    self.phone = self.row[5]
        
                self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
                self.uname.place(x=650, y=240)
        
                self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
                self.uage.place(x=650, y=280)
        
                self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
                self.ugender.place(x=650, y=320)

                self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
                self.ulocation.place(x=650, y=360)

                self.utime = Label(self.master, text="Phone Number", font=('arial 18 bold'))
                self.utime.place(x=650, y=400)

                self.uphone = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
                self.uphone.place(x=650, y=440)
        
                # entries for each labels
                self.ent1 = Entry(self.master, width=30)
                self.ent1.place(x=1000, y=245)
                self.ent1.insert(END, str(self.name1))

                self.ent2 = Entry(self.master, width=30)
                self.ent2.place(x=1000, y=285)
                self.ent2.insert(END, str(self.age))

                self.ent3 = Entry(self.master, width=30)
                self.ent3.place(x=1000, y=325)
                self.ent3.insert(END, str(self.gender))

                self.ent4 = Entry(self.master, width=30)
                self.ent4.place(x=1000, y=365)
                self.ent4.insert(END, str(self.location))

                self.ent5 = Entry(self.master, width=30)
                self.ent5.place(x=1000, y=405)
                self.ent5.insert(END, str(self.phone))

                self.ent6 = Entry(self.master, width=30)
                self.ent6.place(x=1000, y=445)
                self.ent6.insert(END, str(self.time))
                

        
                # button to execute update
                self.update = Button(self.master, text="Submit", width=20, height=2, bg='lightblue',command=self.update_db)
                self.update.place(x=800, y=500)
        
    
        def update_db(self):
            # declaring the variables to update
            self.var1 = self.ent1.get() 
            self.var2 = self.ent2.get() 
            self.var3 = self.ent3.get() 
            self.var4 = self.ent4.get() 
            self.var5 = self.ent5.get()
            self.var6 = self.ent6.get()

            query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
            c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
            

        def delete_db(self):
            # delete the appointment
            self.input=self.namenet.get()
            if self.input=='':
                tkinter.messagebox.showinfo("Warning","Please enter Patient's name to delete the field")
            else:   
                
                sql2 = "DELETE FROM appointments WHERE name LIKE ?"
                c.execute(sql2, (self.namenet.get(),))
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Deleted Successfully")
                self.ent1.destroy()
                self.ent2.destroy()
                self.ent3.destroy()
                self.ent4.destroy()
                self.ent5.destroy()
                self.ent6.destroy()
    

    b = Modification(root2)
    root2.geometry("1600x720+0+0")
# root.resizable(False, False)
    root2.mainloop()
