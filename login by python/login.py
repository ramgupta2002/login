from tkinter import *
from tkinter import ttk,messagebox
from tkinter import Frame
from register import Register
import pymysql
class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        
        left_frame = Frame(root, bg="#08A3D2", width=600, height=480)
        right_frame = Frame(root, bg="#031F3C", width=600, height=480)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        right_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        
        #=======
        login_frame=Frame(self.root,bg="White")
        login_frame.place(x=300, y=120, height=500, width=800)
        
        title = Label(login_frame, text="LOGIN HERE", font=("Times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=60)
        
        email= Label(login_frame, text="EMAIL ADDRESS", font=("Times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=160)
        self.txt_email= Entry(login_frame,font=("Times new roman", 15,), bg="lightgray")
        self.txt_email.place(x=250, y=190,width=350,height=35)
        
        pass_= Label(login_frame, text="PASSWORD", font=("Times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=260)
        self.txt_pass_= Entry(login_frame,font=("Times new roman", 15,), bg="lightgray")
        self.txt_pass_.place(x=250, y=290,width=350,height=35)
        
        btn_reg = Button(login_frame, text="Register new Account?", font=("times new roman ",14), bg="white",cursor="hand2", bd=0, fg="#800857",command=self.register_window).place(x=250, y=330)
        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman ",14), bg="white",cursor="hand2", bd=0, fg="red",command=self.forget_password_window).place(x=450, y=330)
        btn_login = Button(login_frame, text="Login", font=("Times new roman ",20), fg="white", bg="#800857",cursor="hand2",command=self.login).place(x=250, y=380,width=180,height=40)
        
    def reset(self):
        self.cmd_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)
    
    def forget_password(self):
        if  self.cmd_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmd_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Please Select the correct Security Question/ Enter Answer",parent=self.root2)
                     
                else:   
                     cur.execute("update  employee set password=%s where email=%s" ,(self.txt_new_pass.get(),self.txt_email.get()))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Your Password has been reset,Pleace login with new password",parent=self.root2)
                     
                     self.reset()
                     self.root2.destroy()
                    
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
            
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email to reset your password",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s ",(self.txt_email.get()))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Please enter the valid email to reset your password",parent=self.root)
                     
                else:
                    
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x495+480+150")
                    self.root.config(bg="White")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t = Label(self.root2,text="Forget Password", font=("Times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10,relwidth=1)
            
                    question =Label(self.root2,text="Security Question", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=100)
                    self.cmd_quest=ttk.Combobox(self.root2,font=("times new roman", 13,),state='readonly',justify=CENTER)
                    self.cmd_quest['values'] =("Select","Your First Pet Name ,","Your Birth Place","Your Best Friend Name")
                    self.cmd_quest.place(x=50,y=130, width=250)
                    self.cmd_quest.current(0)
            
                    answer=Label(self.root2,text=" Answer", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman", 15,),  bg="lightgray")
                    self.txt_answer.place(x=50,y=210, width=250)
            
                    new_password=Label(self.root2,text="New_Password", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman", 15,),  bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290, width=250)
            
                    btn_chages_password=Button(self.root2,text="Reset Password", bg="green", fg="white", font=("times new roman", 15),command=self.forget_password).place(x=90,y=340)
                
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
            
   
        
        
        
        
    def register_window(self):
        self.root.destroy()
        root = Tk()  # Create a new Tk instance for the register window
        obj = Register(root)  # Create an instance of the Register class
        root.mainloop()
        
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required ",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(), self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invaled USERNAME & PASSWORD ",parent=self.root)
                     
                else:
                    messagebox.showinfo("Success","Welcome ",parent=self.root) 
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
                
            
        
        
        
root=Tk()
obj = login_window(root)
root.mainloop()

