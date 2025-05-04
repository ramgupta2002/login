from tkinter import *
from tkinter import ttk,messagebox
from tkinter import Frame
import pymysql


from PIL import Image, ImageTk

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registeration window")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.config(bg="white")
        
        self.bg_img = Image.open("bg2.WEBP")
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        # Create a label to display the background image
        bg_label = Label(self.root, image=self.bg_img)
        bg_label.place(x=250, y=0, relwidth=1, relheight=1)
        
        fg_img = Image.open("bg4.webp")
        self.fg_img = ImageTk.PhotoImage(fg_img)
        fg_label = Label(self.root, image=self.fg_img)
        fg_label.place(x=150, y=120, width=400, height=500)
        
        Frame1=Frame(self.root,bg="white")
        Frame1.place(x=550, y=120, width=800, height=500)
        #---------1
        title =Label(Frame1,text="REGISTER HERE", font=("times new roman", 20), bg="white",fg="green").place(x=50,y=30)
        
        f_name =Label(Frame1,text="First Name", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_fname.place(x=50,y=130, width=250)
        
        l_name =Label(Frame1,text="Last Name", font=("times new roman", 15), bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_lname.place(x=370,y=130, width=250)
        
        #--------------2
        
        contact =Label(Frame1,text="Contact No", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_contact.place(x=50,y=200, width=250)
        
        email=Label(Frame1,text=" Email", font=("times new roman", 15), bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_email.place(x=370,y=200, width=250)
        #---------------------3
        
        question =Label(Frame1,text="Security Question", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=240)
        self.cmd_quest=ttk.Combobox(Frame1,font=("times new roman", 13,),state='readonly',justify=CENTER)
        self.cmd_quest['values'] =("Select","Your First Pet Name ,","Your Birth Place","Your Best Friend Name")
        self.cmd_quest.place(x=50,y=270, width=250)
        self.cmd_quest.current(0)
        
        answer=Label(Frame1,text=" Answer", font=("times new roman", 15), bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_answer.place(x=370,y=270, width=250)
        
        #============4
        password =Label(Frame1,text="Password", font=("times new roman", 15), bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_password.place(x=50,y=340, width=250)
        
        cpassword=Label(Frame1,text=" Confirm password", font=("times new roman", 15), bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(Frame1,font=("times new roman", 15,),  bg="lightgray")
        self.txt_cpassword.place(x=370,y=340, width=250)
        
        #--------term -----
        self.var_chk=IntVar()
        chk=Checkbutton(Frame1,text="I Agree The Term & Condition",variable=self.var_chk,onvalue=1,offvalue=0, bg="white", font=("times new roman", 12)).place(x=50,y=380)
        
        image = Image.open("reg4.png")
        btn_img = ImageTk.PhotoImage(image)
        
        btn = Button(Frame1, image=btn_img,bd=0,cursor="hand2",command=self.register_data)
        btn.image = btn_img  # This line is necessary to prevent the image from being garbage collected
        btn.place(x=50, y=420)
        
        btn_login=Button(self.root,text="Sign In", font=("times new roman", 20),bd=0,cursor="hand2",command=self.login_window).place(x=270,y=569,width=180)
        
    def login_window(self):
        self.root.destroy()
        import login
 
    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)   
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmd_quest.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()==""or  self.txt_email.get()=="" or  self.cmd_quest.get()=="Select" or self.txt_answer.get()==""or self.txt_password.get()==""or self.txt_cpassword.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password and Confirm Passward should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Term & Condition",parent=self.root)  
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exist,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmd_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                 ))   
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
                    self.clear()         
            except Exception as es:
                    messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
    

               
            
           
        
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
