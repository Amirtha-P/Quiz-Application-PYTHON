from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import socket
from datetime import date,timedelta
home=Tk()
home.title("Login")
home.geometry("800x800")
whitespace=" "
home.title(95*whitespace+"Welcome")
home.config(bg="violetred")
mainframe=Frame(home,bg="skyblue",relief=GROOVE,bd=15)
mainframe.place(x=10,y=10,width=780,height=780)
mainframe1=Frame(home,bg="violetred",relief=GROOVE,bd=20)
mainframe1.place(x=150,y=200,width=500,height=400)
label=Label(mainframe,text="WELCOME TO HOME PAGE",font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
label.pack(side=TOP,fill=X)
def exit():
    exit=messagebox.askyesno(" ","Do you want to exit")
    if exit>0:
        home.destroy()
        return
canvas1 = Canvas( mainframe1, width = 500,height = 500)
canvas1.pack(fill = "both", expand = True)
canvas1.create_text( 220, 50, text = "Click here to login",font=('TimesNewRoman','30'))
def signup():
    sup=Toplevel(home)
    sup.title("Login")
    home.withdraw()
    sup.config(bg="grey")
    sup.geometry("800x800")
    whitespace=" "
    sup.title(150*whitespace+"SIGN IN")
    signp=Label(sup,text="WELCOME TO SIGN-UP PAGE",font=("TimesNewRomans",20,"bold"),bg="blue",bd=10,fg="black")
    signp.pack(side=TOP,fill=X)
    def cpass():
        user=un1.get()
        passw=pw1.get()
        cpassw=cpw1.get()
        if passw==cpassw:
                    
            mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="Computernw")
            mysqlcon=mysqldb.cursor()
            mysqlcon.execute("insert into login(fullname,username,password,score) values(%s,%s,%s,0)",(full1.get(),un1.get(),cpw1.get()))
            mysqldb.commit()
            mysqldb.close()
            messagebox.showinfo("","Password and username created successfully")
        else:
            messagebox.showerror("","Incorrect password")
    fullname=Label(sup,text="Fullname",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
    fullname.place(x=100,y=100)
    full1=Entry(sup,width=20,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
    full1.place(x=300,y=100)
    un=Label(sup,text="username",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
    un.place(x=100,y=200)
    un1=Entry(sup,width=20,font=("TimesNewRomans",20),bg="white",fg="black",bd=4)
    un1.place(x=300,y=200)
    pw=Label(sup,text="password",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
    pw.place(x=100,y=270)
    pw1=Entry(sup,font=("TimesNewRomans",20,"bold"),show="*",bg="white",fg="black",bd=4)
    pw1.place(x=300,y=270)
    cpw=Label(sup,text="confirm",font=("TimesNewRomans",20,"bold"),bg="white",fg="black",bd=5)
    cpw.place(x=100,y=350)
    cpw1=Entry(sup,font=("TimesNewRomans",20,"bold"),show="*",bg="white",fg="black",bd=4)
    cpw1.place(x=300,y=350)
    sinb=Button(sup,text="OK",command=cpass,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
    sinb.place(x=150,y=420)
    close=Button(sup,text="close",command=main,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
    close.place(x=300,y=420)
    sup.mainloop()
def signin():
    sin=Toplevel(home)
    sin.title("Login")
    home.withdraw()
    sin.config(bg="pink")
    sin.geometry("800x800")
    whitespace=" "
    sin.title(150*whitespace+"SIGN IN")
    def sinb():
        if un1.get()=="" or pw1.get()=="":
            messagebox.showerror("","All fields are required")
        else:
            mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="Computernw")
            mysqlcon=mysqldb.cursor()
            mysqlcon.execute("Select * from login where username=%s and password=%s",(un1.get(),pw1.get()))
            row=mysqlcon.fetchone()
            if row==None:
                messagebox.showerror("","Invalid username or password")
            else:
                messagebox.showinfo("","valid")
                host = '127.0.0.1'
                port = 5000
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((host,port))
                def profile():
                    addi=Toplevel(sin)
                    addi.title("Login")
                    addi.config(bg="VioletRed")
                    mainframe1=Frame(addi,bg="lightblue",relief=GROOVE,bd=15)
                    mainframe1.place(x=10,y=10,width=780,height=780)
                    mainframe=Frame(mainframe1,bg="orange",relief=GROOVE,bd=15)
                    mainframe.place(x=10,y=10,width=730,height=730)
                    bg=ImageTk.PhotoImage(file=r"F:\downloads\image.Jpg")
                    bg_label=Label(mainframe,image=bg)
                    bg_label.place(x=0,y=0,relwidth=1,relheight=1)
                    label=Label(mainframe,text="WELCOME TO TECHNICAL QUIZ",font=("TimesNewRomans",20,"bold"),bg="white",bd=10,fg="RED")
                    label.pack(side=TOP,fill=X)
                    addi.geometry("800x800")
                    whitespace=" "
                    def start():
                        a="amir"
                        sup=Toplevel(addi)
                        addi.withdraw()
                        sup.config(bg="lightblue")
                        sup.title("Questions")
                        sup.config(bg="lightblue")
                        mainframe1=Frame(sup,bg="lightpink",relief=GROOVE,bd=15)
                        mainframe1.place(x=10,y=10,width=780,height=780)
                        maiframe=Frame(mainframe1,bg="lightblue",relief=GROOVE,bd=15)
                        maiframe.place(x=10,y=10,width=720,height=720)
                        sup.geometry("800x800")
                        whitespace=" "
                        bg=ImageTk.PhotoImage(file=r"F:\downloads\fourth design.Jpg")
                        bg_label=Label(maiframe,image=bg)
                        bg_label.place(x=0,y=0,relwidth=1,relheight=1)
                        label=Label(maiframe,text="QUESTIONS",font=("TimesNewRomans",20,"bold"),bg="grey",bd=10,fg="black")
                        label.pack(side=TOP,fill=X)
                        label1=Label(maiframe,text="1.What is pointers?",font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
                        label1.place(x=210,y=150)
                        n=IntVar()
                        b1=Radiobutton(maiframe,text="Stores the value of the variable",font=("TimesNewRomans",20),bg="white",variable=n,value=1)
                        b1.place(x=120,y=250)
                        b1=Radiobutton(maiframe,text="Stores the address of the variable",font=("TimesNewRomans",20),bg="white",variable=n,value=2)
                        b1.place(x=120,y=330)
                        b1=Radiobutton(maiframe,text="Stores the address of pointer variable",font=("TimesNewRomans",20),bg="white",variable=n,value=3)
                        b1.place(x=120,y=410)
                        def ok():
                            selection=n.get()
                            print(n.get())
                            selectio=str(selection)
                            s.send(selectio.encode())
                        sub=Button(maiframe,text="confirm",command=ok,font=("TimesNewRoman",20,"bold"))
                        sub.place(x=110,y=550)
                        nextb=Button(maiframe,text="next",command=nxt1,font=("TimesNewRoman",20,"bold"))
                        nextb.place(x=270,y=550)
                        sup.mainloop()
                    def nxt1():
                        sup=Toplevel(addi)
                        addi.withdraw()
                        sup.config(bg="lightblue")
                        sup.title("Questions")
                        sup.config(bg="lightblue")
                        mainframe1=Frame(sup,bg="lightpink",relief=GROOVE,bd=15)
                        mainframe1.place(x=10,y=10,width=780,height=780)
                        maiframe=Frame(mainframe1,bg="lightblue",relief=GROOVE,bd=15)
                        maiframe.place(x=10,y=10,width=720,height=720)
                        sup.geometry("800x800")
                        whitespace=" "
                        bg=ImageTk.PhotoImage(file=r"F:\downloads\fourth design.Jpg")
                        bg_label=Label(maiframe,image=bg)
                        bg_label.place(x=0,y=0,relwidth=1,relheight=1)
                        label=Label(maiframe,text="QUESTIONS",font=("TimesNewRomans",20,"bold"),bg="grey",bd=10,fg="black")
                        label.pack(side=TOP,fill=X)
                        n=IntVar()
                        label1=Label(maiframe,text="2.The pointer points to the deallocated memory is......",font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
                        label1.place(x=10,y=150)
                        b1=Radiobutton(maiframe,text="Dangling pointer",font=("TimesNewRomans",20),bg="white",variable=n,value=1)
                        b1.place(x=120,y=250)
                        b1=Radiobutton(maiframe,text="Null pointer",font=("TimesNewRomans",20),bg="white",variable=n,value=2)
                        b1.place(x=120,y=330)
                        b1=Radiobutton(maiframe,text="variable pointer",font=("TimesNewRomans",20),bg="white",variable=n,value=3)
                        b1.place(x=120,y=410)
                        def ok():
                            selection=n.get()
                            print(n.get())
                            selectio=str(selection)
                            s.send(selectio.encode())
                        sub=Button(maiframe,text="confirm",command=ok,font=("TimesNewRoman",20,"bold"))
                        sub.place(x=110,y=550)
                        nextb=Button(maiframe,text="next",command=nxt2,font=("TimesNewRoman",20,"bold"))
                        nextb.place(x=270,y=550)
                        sup.mainloop()
                    def nxt2():
                        sup=Toplevel(addi)
                        addi.withdraw()
                        sup.config(bg="lightblue")
                        sup.title("Questions")
                        sup.config(bg="lightblue")
                        mainframe1=Frame(sup,bg="lightpink",relief=GROOVE,bd=15)
                        mainframe1.place(x=10,y=10,width=780,height=780)
                        maiframe=Frame(mainframe1,bg="lightblue",relief=GROOVE,bd=15)
                        maiframe.place(x=10,y=10,width=720,height=720)
                        sup.geometry("800x800")
                        whitespace=" "
                        bg=ImageTk.PhotoImage(file=r"F:\downloads\fourth design.Jpg")
                        bg_label=Label(maiframe,image=bg)
                        bg_label.place(x=0,y=0,relwidth=1,relheight=1)
                        label=Label(maiframe,text="QUESTIONS",font=("TimesNewRomans",20,"bold"),bg="grey",bd=10,fg="black")
                        label.pack(side=TOP,fill=X)
                        n=IntVar()
                        label1=Label(maiframe,text="3.What is the complexity of enqueue operation: ",font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
                        label1.place(x=10,y=150)
                        b1=Radiobutton(maiframe,text="O(1)",font=("TimesNewRomans",20),bg="white",variable=n,value=1)
                        b1.place(x=120,y=250)
                        b1=Radiobutton(maiframe,text="O(n)",font=("TimesNewRomans",20),bg="white",variable=n,value=2)
                        b1.place(x=120,y=330)
                        b1=Radiobutton(maiframe,text="O(nlogn)",font=("TimesNewRomans",20),bg="white",variable=n,value=3)
                        b1.place(x=120,y=410)
                        def ok():
                            selection=n.get()
                            print(n.get())
                            selectio=str(selection)
                            s.send(selectio.encode())
                                
                        sub=Button(maiframe,text="confirm",command=ok,font=("TimesNewRoman",20,"bold"))
                        sub.place(x=110,y=550)
                        nextb=Button(maiframe,text="submit",command=submit,font=("TimesNewRoman",20,"bold"))
                        nextb.place(x=270,y=550)
                        sup.mainloop()
                    def submit():
                        sup=Toplevel(addi)
                        addi.withdraw()
                        sup.title("submit")
                        sup.geometry("900x800")
    
                        sup.config(bg="VioletRed")
                        mainfram1=Frame(sup,bg="lightblue",relief=GROOVE,bd=15)
                        mainfram1.place(x=10,y=10,width=900,height=780)
                        maifram=Frame(mainfram1,bg="orange",relief=GROOVE,bd=15)
                        maifram.place(x=10,y=10,width=900,height=730)
                        bg=ImageTk.PhotoImage(file=r"F:\downloads\img1.Jpg")
                        bg_labe=Label(maifram,image=bg)
                        bg_labe.place(x=0,y=0,relwidth=1,relheight=1)
                        label=Label(maifram,text="THANKYOU",font=("TimesNewRomans",20,"bold"),bg="white",bd=10,fg="RED")
                        label.pack(side=TOP,fill=X)
                        answer=""
                        def ok():
                            ans=s.recv(1024).decode()
                            answer=ans
                            print(answer)
                            l2.config(text=answer)
                            mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="Computernw")
                            mysqlcon=mysqldb.cursor()
                            mysqlcon.execute("update login set score=%s where username=%s",(answer,un1.get()))
                            mysqldb.commit()
                            mysqldb.close()
                            messagebox.showinfo("","success")
                        def display():
                            mysqldb=mysql.connector.connect(host="localhost",port=3306,username="root",password="amiramirtha",database="Computernw")
                            mysqlcon=mysqldb.cursor()
                            mysqlcon.execute("select fullname,score from login order by score desc ")
                            result=mysqlcon.fetchall()
                            print(result)
                            for i,(fullname,score) in enumerate(result,start=1):
                                tv.insert("","end",values=(fullname,score))

                            mysqldb.commit()
                            mysqldb.close()     
                        def quit1():
                            exit=messagebox.askyesno(" ","Do you want to exit")
                            if exit>0:
                                home.destroy()
                                return       
                               
                        sub=Button(maifram,text="Click",command=ok,font=("TimesNewRoman",20,"bold"))
                        sub.place(x=130,y=450)
                        quit=Button(maifram,text="Quit",command=quit1,font=("TimesNewRoman",20,"bold"))
                        quit.place(x=280,y=450)
                        l1=Label(maifram,text="Click to see the score ",font=("TimesNewRomans",20),bg="black",bd=10,fg="white")
                        l1.place(x=100,y=250)
                        l2=Label(maifram,text="Your score is",font=("TimesNewRomans",20),bg="black",bd=10,fg="green")
                        l2.place(x=150,y=350)
                        dis=Button(maifram,text="display",command=display,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                        dis.place(x=200,y=600)
                        frame=Frame(maifram,bg="skyblue",bd=5,relief=GROOVE)
                        frame.place(x=400,y=80,width=400,height=500)
                        scroll_y=Scrollbar(frame,orient=VERTICAL)
                        scroll_y.pack(side=RIGHT,fill=Y)
                        tv=ttk.Treeview(frame,column=("fullname","score"),yscrollcommand=scroll_y)
                        tv.heading("fullname",text="NAME")
                        tv.heading("score",text="SCORE")
                        tv["show"]="headings"
                        tv.column("fullname",width=20)
                        tv.column("score",width=80)
                        tv.pack(fill=BOTH,expand=1)
                        sup.mainloop()
                        # Create Canvas
                    canvas1 = Canvas( mainframe, width = 400,
                                         height = 400)
                          
                    canvas1.pack(fill = "both", expand = True)
                          
                        # Display image
                    canvas1.create_image( 0, 0, image = bg, 
                                             anchor = "nw")
                          
                        # Add Text
                    canvas1.create_text( 360, 250, text = "If you are ready",font=('TimesNewRoman','30','bold'))
                
                    canvas1.create_text( 360, 350, text = "then",font=('TimesNewRoman','30','bold'))
                
                    canvas1.create_text( 360, 450, text = "click the start button!!!",font=('TimesNewRoman','30','bold'))


                    start=Button(mainframe,text="start",command=start,font=("TimesNewRomans",20,"bold"),bd=10,fg="blue",bg="white")
                    start.place(x=300,y=600)
                    addi.mainloop()
                profile()
                s.close()
    signn=Label(sin,text="WELCOME TO SIGN-IN PAGE",font=("TimesNewRomans",20,"bold"),bg="blue",bd=10,fg="black")
    signn.pack(side=TOP,fill=X)
    un=Label(sin,text="username",font=("TimesNewRomans",20,"bold"),bg="lightblue",fg="black",bd=5)
    un.place(x=100,y=200)
    un1=Entry(sin,width=20,font=("TimesNewRomans",20),bg="lightblue",fg="black",bd=4)
    un1.place(x=300,y=200)
    pw=Label(sin,text="password",font=("TimesNewRomans",20,"bold"),bg="lightblue",fg="black",bd=5)
    pw.place(x=100,y=270)
    pw1=Entry(sin,font=("TimesNewRomans",20,"bold"),show="*",bg="lightblue",fg="black",bd=4)
    pw1.place(x=300,y=270)
    sinb=Button(sin,text="sign-in",command=sinb,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
    sinb.place(x=150,y=350)
    close=Button(sin,text="sign-out",command=main,font=("TimesNewRomans",20,"bold"),bd=10,fg="white",bg="black")
    close.place(x=300,y=350)
    sin.mainloop()
def main():
    ano=Toplevel(home)
    ano.title("Login")
    ano.geometry("800x800")
    whitespace=" "
    home.title(95*whitespace+"Welcome")
    home.config(bg="violetred")
    mainframe=Frame(ano,bg="skyblue",relief=GROOVE,bd=15)
    mainframe.place(x=10,y=10,width=780,height=780)
    mainframe1=Frame(ano,bg="violetred",relief=GROOVE,bd=20)
    mainframe1.place(x=150,y=200,width=500,height=400)
    label=Label(mainframe,text="WELCOME TO HOME PAGE",font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
    label.pack(side=TOP,fill=X)
    def exit():
        exit=messagebox.askyesno(" ","Do you want to exit")
        if exit>0:
            home.destroy()
            return
    canvas1 = Canvas( mainframe1, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_text( 220, 50, text = "Click here to login",font=('TimesNewRoman','30'))
    

    
    sign=Button(mainframe1,text="sign in",command=signin,font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
    sign.place(x="80",y="150")
    siup=Button(mainframe1,text="sign up",command=signup,font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
    siup.place(x="250",y="150")
    ex=Button(mainframe1,text="Exit",command=exit,font=("TimesNewRoman",20),bg="white",bd=10,fg="black")
    ex.place(x="170",y="270")
    ano.mainloop()

sign=Button(mainframe1,text="sign in",command=signin,font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
sign.place(x="80",y="150")
siup=Button(mainframe1,text="sign up",command=signup,font=("TimesNewRomans",20),bg="white",bd=10,fg="black")
siup.place(x="250",y="150")
ex=Button(mainframe1,text="Exit",command=exit,font=("TimesNewRoman",20),bg="white",bd=10,fg="black")
ex.place(x="170",y="270")
home.mainloop()

