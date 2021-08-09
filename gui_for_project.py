from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import mysql.connector


""" CONNECTING DATABASE TO PYTHON """
con=mysql.connector.connect(host='localhost',user='root',password='',database='htms')
cur=con.cursor()
print("Succesfull Entered in database")


""" CLASS HOTEL IN WHICH WE WRITTEN CODE """

class hotel:
    """ WINDOW OF PROJECT """ 
    def __init__(self,root):
        self.root=root
        self.root.title("Lodge Management system")
        self.root.geometry("1400x750+50+30")

        

        """ VARIABLES """
        self.cust_name=StringVar()
        self.cust_idproof=StringVar()
        self.cust_idproofno=IntVar()
        self.cust_days=IntVar()
        self.cust_city=StringVar()
        self.room_no=IntVar()
        self.cust_id=IntVar()
        self.payment_mode=StringVar()
        self.searchname=IntVar()
        """ ***************************************"""

        """ HEADING OF PROJECT """
        title=Label(self.root,text="LODGE MANAGEMENT SYSTEM",padx=10,pady=10,font=("arial",15,"bold"),bg='red').pack(fill=BOTH)

        """ CURRENT DATE TIME """
        dt=datetime.datetime.now()
        date=dt.strftime("%d %B %Y")
        time=dt.strftime("%H:%M:%S")
        dis_dt=Label(self.root,text="Date : "+date+"    "+"Time : "+time,font=("arial",15,"bold"),pady=5)
        dis_dt.pack()
        
        """ FIRST FRAME IN WHICH WE TAKE THE COUSTMER DETAILS WHICH CONTAINS LABEL , ENTRY AND BUTTONS """
        
        first_frame=Frame(self.root,bd=4,relief=GROOVE,bg="Orange")
        first_frame.place(x=10,y=90,width=450,height=650)


        label2=Label(first_frame,text="COUSTMER DETAILS",font=("arial",15,"bold"),bg="Orange")
        label2.place(x=90,y=40)


        label3=Label(first_frame,text="Coustmer_name :",bg="Orange",font=("arial",15))
        label3.place(x=15,y=110)

        e3=Entry(first_frame,width=35,borderwidth=4,textvariable=self.cust_name)
        e3.place(x=190,y=110)

        
        
        label4=Label(first_frame,bg="Orange",text="Coustmer_Idproof :",font=("arial",15))
        label4.place(x=15,y=170)

        select_box=ttk.Combobox(first_frame,font=("arial",15),textvariable=self.cust_idproof)
        select_box['values']=("Adhar Card","Driving License","Pan Card")
        select_box.place(x=190,y=170)


        label5=Label(first_frame,bg="Orange",text="Idproofnumber :",font=("arial",15))
        label5.place(x=15,y=230)

        e5=Entry(first_frame,width=35,borderwidth=4,textvariable=self.cust_idproofno)
        e5.place(x=190,y=230)


        label6=Label(first_frame,bg="Orange",text="Coustmer_days :",font=("arial",15))
        label6.place(x=15,y=290)


        e6=Entry(first_frame,width=35,borderwidth=4,textvariable=self.cust_days)
        e6.place(x=190,y=290)
                

        label7=Label(first_frame,bg="Orange",text="Coustmer_City :",font=("arial",15))
        label7.place(x=15,y=350)


        e7=Entry(first_frame,width=35,borderwidth=4,textvariable=self.cust_city)
        e7.place(x=190,y=350)
       
        
        label8=Label(first_frame,bg="Orange",text="Room_no :",font=("arial",15))
        label8.place(x=15,y=410)


        e8=Entry(first_frame,width=35,borderwidth=4,textvariable=self.room_no)
        e8.place(x=190,y=410)
       

        """ FIRST FRAME BUTTONS """        

        save_but=Button(first_frame,text="SAVE",width=10,font=("arial",13),command=self.insert)
        save_but.place(x=122,y=490)


        Avl_but=Button(first_frame,text="AVAILABLE",width=10,font=("arial",13),command=self.available)
        Avl_but.place(x=122,y=550)

        """ SECOND FRAME CONTAINS BUTTONS , DISPLAY PROPERTIES """

        second_frame=Frame(self.root,bd=4,relief=GROOVE,bg="Orange")
        second_frame.place(x=500,y=90,width=870,height=650)


        pay_but=Button(second_frame,text="PAYMENT",width=10,font=("arial",13),command=self.payment)
        pay_but.place(x=22,y=20)


        search_but=Button(second_frame,text="SEARCH",width=10,font=("arial",13),command=self.search_record)
        search_but.place(x=152,y=20)

        display_but=Button(second_frame,text="DISPLAY",width=10,font=("arial",13),command=self.display)
        display_but.place(x=432,y=20)

        History_but=Button(second_frame,text="HISTORY",width=10,font=("arial",13),command=self.history)
        History_but.place(x=572,y=20)

        entry9=Entry(second_frame,width=20,borderwidth=4,textvariable=self.searchname)
        entry9.place(x=262,y=20)

        
        """ THIRD FRAME TREE VIEW USED TO DISPLAY RECORDS FROM DATABASE IN ONE BY  ONE MANNER """
        
        third_frame=Frame(second_frame,bd=4,relief=RIDGE,bg="red")
        third_frame.place(x=15,y=100,width=830,height=530)

        """ SCROLL BAR USED TO SCROLL DOWN FOR MORE RECORDS """
        
        scroll_vertical=Scrollbar(third_frame,orient=VERTICAL)
        
        self.display_b=ttk.Treeview(third_frame,columns=("cust_id","cust_name","cust_idproof","cust_idproofno","cust_days","cust_time","cust_city","Room_no"),yscrollcommand=scroll_vertical.set)

        scroll_vertical.pack(side=RIGHT,fill=Y)
        
        scroll_vertical.config(command=self.display_b.yview)
        
        self.display_b.heading("cust_id",text="ID")
        self.display_b.heading("cust_name",text="NAME")
        self.display_b.heading("cust_idproof",text="ID_PROOF")
        self.display_b.heading("cust_idproofno",text="ID_PROOF_NO")
        self.display_b.heading("cust_days",text="DAYS")
        self.display_b.heading("cust_time",text="TIME")
        self.display_b.heading("cust_city",text="CITY")
        self.display_b.heading("Room_no",text="ROOM_NO")
        
        
        
        self.display_b['show']='headings'
        
        self.display_b.column("cust_id",width=100)
        self.display_b.column("cust_name",width=100)
        self.display_b.column("cust_idproof",width=100)
        self.display_b.column("cust_idproofno",width=100)
        self.display_b.column("cust_days",width=100)
        self.display_b.column("cust_time",width=100)
        self.display_b.column("cust_city",width=100)
        self.display_b.column("Room_no",width=100)
        self.display_b.pack(fill=BOTH,expand=1)
        
        return
    
    def display(self):

        """ DISPLAY ALL COUSTMERS RECORDS WHO PRESENT STAYING IN HOTEL """
        
        third_frame=Frame(self.root,bd=4,relief=RIDGE,bg="orange")
        third_frame.place(x=520,y=195,width=830,height=530)
        
        scroll_vertical=Scrollbar(third_frame,orient=VERTICAL)
        
        self.display_d=ttk.Treeview(third_frame,columns=("cust_id","cust_name","cust_idproof","cust_idproofno","cust_days","cust_time","cust_city","Room_no"),yscrollcommand=scroll_vertical.set)

        scroll_vertical.pack(side=RIGHT,fill=Y)
        
        scroll_vertical.config(command=self.display_d.yview)
        
    
        self.display_d.heading("cust_id",text="ID")
  
        self.display_d.heading("cust_name",text="NAME")
        self.display_d.heading("cust_idproof",text="ID_PROOF")
        self.display_d.heading("cust_idproofno",text="ID_PROOF_NO")
        self.display_d.heading("cust_days",text="DAYS")
        self.display_d.heading("cust_time",text="TIME")
        self.display_d.heading("cust_city",text="CITY")
        self.display_d.heading("Room_no",text="ROOM_NO")
        
        
        
        self.display_d['show']='headings'
        
        self.display_d.column("cust_id",width=100)
        self.display_d.column("cust_name",width=100)
        self.display_d.column("cust_idproof",width=100)
        self.display_d.column("cust_idproofno",width=100)
        self.display_d.column("cust_days",width=100)
        self.display_d.column("cust_time",width=100)
        self.display_d.column("cust_city",width=100)
        self.display_d.column("Room_no",width=100)
        self.display_d.pack(fill=BOTH,expand=1)
        
        
        
        cur=con.cursor()
        cur.execute("select coustmer.cust_id,coustmer.cust_name,coustmer.cust_idproof,coustmer.cust_idproofno,coustmer.cust_days,coustmer.cust_time,coustmer.cust_city,coustmer.room_no from coustmer inner join room on coustmer.room_no = room.room_no where room_available=0")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.display_d.delete(*self.display_d.get_children())
            for row in rows:
                self.display_d.insert('','end',values=row)
                
        return

    def insert(self):

        """ TAKES DETAILS ABOUT COUSTMERS AND SAVE IN DATABASE """

        if self.cust_name.get()== "" or self.cust_idproof.get() == "" or self.cust_idproofno.get()== 0 or self.cust_days.get()==0 or self.cust_city.get()== "" or self.room_no.get() == 0:
            messagebox.showerror("Error", "Some field is empty ")
        else:
        
            temp1="insert into coustmer(cust_name,cust_idproof,cust_idproofno,cust_days,cust_city,Room_no) values(%s,%s,%s,%s,%s,%s)"
            values=(self.cust_name.get(),self.cust_idproof.get(),self.cust_idproofno.get(),self.cust_days.get(),self.cust_city.get(),self.room_no.get())
            cur=con.cursor()
            cur.execute(temp1,values)
            con.commit()


            cur.execute("update room set room_available=0 where room_no={}".format(self.room_no.get()))
            con.commit()
            messagebox.askquestion("askquestion", "Details Are Correct ?")
            self.clear()
            return

    def available(self):

        """ DISPLAYS AVAILABLE ROOM IN DATABASE """
        
        fourth_frame=Frame(self.root,bd=4,relief=GROOVE,bg="orange")
        fourth_frame.place(x=520,y=195,width=830,height=530)
          
        scroll_vertical=Scrollbar(fourth_frame,orient=VERTICAL)
        
        self.display_avl=ttk.Treeview(fourth_frame,columns=("room_no","room_type","room_bed","room_cost","employee_id","floor_no"),yscrollcommand=scroll_vertical.set)

        scroll_vertical.pack(side=RIGHT,fill=Y)
        
        scroll_vertical.config(command=self.display_avl.yview)
        
        self.display_avl.heading("room_no",text="Room_no")
        self.display_avl.heading("room_type",text="Type")
        self.display_avl.heading("room_bed",text="Bed")
        self.display_avl.heading("room_cost",text="Cost")
        self.display_avl.heading("employee_id",text="Emp_id")
        self.display_avl.heading("floor_no",text="Floor")
        
        
        self.display_avl['show']='headings'
        
        self.display_avl.column("room_no",width=100)
        self.display_avl.column("room_type",width=100)
        self.display_avl.column("room_bed",width=100)
        self.display_avl.column("room_cost",width=100)
        self.display_avl.column("employee_id",width=100)
        self.display_avl.column("floor_no",width=100)
        
        self.display_avl.pack(fill=BOTH,expand=1)



        
        cur=con.cursor()
        cur.execute("select room_no,room_type,room_bed,room_cost,employee_id,floor_no from room where room_available = 1")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.display_avl.delete(*self.display_avl.get_children())
            for row in rows:
                self.display_avl.insert('','end',values=row)
        return

    def payment(self):

        """ OPENS WINDOW FOR PAYMENT WHERE WE CAN SERACH FOR PARTICULAR RECORD AND MAKE FURTHER PAYMENT OPERATIONS """

        top=Toplevel(self.root,bg="orange")
        top.geometry("450x620+60+150")
        
        label1=Label(top,text="PAYMENT DETAILS",font=("arial",15,"bold"),bg="Orange")
        label1.place(x=90,y=40)

        
        label2=Label(top,text="Customer Id : ",font=("arial",15,"bold"),bg="Orange")
        label2.place(x=15,y=110)

        entry1=Entry(top,width=35,borderwidth=4,textvariable=self.cust_id)
        entry1.place(x=190,y=110)

        search_but=Button(top,text="search",width=5,font=("arial",10),command=self.search)
        search_but.place(x=360,y=135)

        label3=Label(top,text="Payment Mode : ",font=("arial",15,"bold"),bg="Orange")
        label3.place(x=15,y=190)
        
        entry2=Entry(top,width=35,borderwidth=4,textvariable=self.payment_mode)
        entry2.place(x=190,y=190)

        label4=Label(top,text="Room no : ",font=("arial",15,"bold"),bg="Orange")
        label4.place(x=15,y=250)
        
        entry3=Entry(top,width=35,borderwidth=4,textvariable=self.room_no)
        entry3.place(x=190,y=250)


        p_but=Button(top,text="PAY",width=10,font=("arial",13),command=self.paymentmode)
        p_but.place(x=142,y=290)
        return



    def search(self):

        """  DISPLAY SEARCH RECORD WHILE PAYMENT """
        
        if self.cust_id.get()== 0:
            messagebox.showerror("Error", "Search field is empty ")
        else:
            fifth_frame=Frame(self.root,bd=4,relief=GROOVE,bg="orange")
            fifth_frame.place(x=520,y=195,width=830,height=530)
            self.display_sea=ttk.Treeview(fifth_frame,columns=("coustmer.cust_id","room.room_no","room.room_cost*coustmer.cust_days"))
        
            self.display_sea.heading("coustmer.cust_id",text=" ID")
            self.display_sea.heading("room.room_no",text="Room No")
            self.display_sea.heading("room.room_cost*coustmer.cust_days",text="Amount")
            self.display_sea['show']='headings'
            self.display_sea.column("coustmer.cust_id",width=100)
            self.display_sea.column("room.room_no",width=100)
            self.display_sea.column("room.room_cost*coustmer.cust_days",width=100)
            self.display_sea.pack(fill=BOTH,expand=1)


            cur=con.cursor()
            cur.execute("select coustmer.cust_id,room.room_no,room.room_cost*coustmer.cust_days from coustmer inner join room on coustmer.room_no=room.Room_no where coustmer.cust_id={}".format(self.cust_id.get()))
            rows=cur.fetchall()
            if(len(rows)!=0):
                self.display_sea.delete(*self.display_sea.get_children())
                for row in rows:
                    self.display_sea.insert('','end',values=row)
            return
            

        

        
    def paymentmode(self):

        """ PAYMENT OPERATIONS """

        if self.cust_id.get()== 0 or self.payment_mode.get() =="" or self.room_no.get()== 0:
            messagebox.showerror("Error", "Search field is empty ")
        else:
        
            self.status = "Paid"

            temp1="insert into payment(cust_id,payment_mode,status) values(%s,%s,%s)"
            values=(self.cust_id.get(),self.payment_mode.get(),self.status)
        
            cur=con.cursor()
            cur.execute(temp1,values)
            con.commit()
            cur.execute("update room set room_available=1 where room_no={}".format(self.room_no.get()))
            con.commit()

            messagebox.showinfo("showinfo", "Succesfully Amount Paid")
            return

    def history(self):

        """  DISPLAYS HISTORY OF THOSE COUSTMERS WHO HAVE LEFT HOTELS """
        
        top=Toplevel(self.root,bg="orange")
        top.geometry("1400x750+50+30")
        top.title("HISTORY")
        sixth_frame=Frame(top,bd=4,relief=GROOVE,bg="orange")
        sixth_frame.place(width=1400,height=750)

        self.display_his=ttk.Treeview(sixth_frame,columns=("coustmer.cust_id","coustmer.cust_name","coustmer.cust_idproof","coustmer.cust_idproofno","coustmer.cust_days","coustmer.cust_time","coustmer.cust_city","coustmer.room_no","payment.payment_mode","payment.paiddate","room.room_cost*coustmer.cust_days","payment.status"))
                        
        self.display_his.heading("coustmer.cust_id",text="ID")
        self.display_his.heading("coustmer.cust_name",text="NAME")
        self.display_his.heading("coustmer.cust_idproof",text="ID PROOF")
        self.display_his.heading("coustmer.cust_idproofno",text="ID PROOF NO")
        self.display_his.heading("coustmer.cust_days",text="DAYS")
        self.display_his.heading("coustmer.cust_time",text="CHECK IN ")
        self.display_his.heading("coustmer.cust_city",text="CITY")
        self.display_his.heading("coustmer.room_no",text="ROOM NO")
        self.display_his.heading("payment.payment_mode",text="PAYMENT MODE")
        self.display_his.heading("payment.paiddate",text="CHECK OUT ")
        self.display_his.heading("room.room_cost*coustmer.cust_days",text="AMOUNT")
        self.display_his.heading("payment.status",text="STATUS")

        self.display_his['show']='headings'
        self.display_his.column("coustmer.cust_id",width=50)
        self.display_his.column("coustmer.cust_name",width=100)
        self.display_his.column("coustmer.cust_idproof",width=100)
        self.display_his.column("coustmer.cust_idproofno",width=100)
        self.display_his.column("coustmer.cust_days",width=50)
        self.display_his.column("coustmer.cust_time",width=130)
        self.display_his.column("coustmer.cust_city",width=100)
        self.display_his.column("coustmer.room_no",width=50)
        self.display_his.column("payment.payment_mode",width=100)
        self.display_his.column("payment.paiddate",width=130)
        self.display_his.column("room.room_cost*coustmer.cust_days",width=50)
        self.display_his.column("payment.status",width=50)

        
        self.display_his.pack(fill=BOTH,expand=1)


        cur=con.cursor()
        cur.execute("select coustmer.cust_id,coustmer.cust_name,coustmer.cust_idproof,coustmer.cust_idproofno,coustmer.cust_days,coustmer.cust_time,coustmer.cust_city,coustmer.room_no,payment.payment_mode,payment.paiddate,room.room_cost*coustmer.cust_days,payment.status from coustmer inner join payment on payment.cust_id=coustmer.cust_id inner join room on coustmer.room_no = room.room_no where payment.status='paid' order by payment.paiddate desc ")
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.display_his.delete(*self.display_his.get_children())
            for row in rows:
                self.display_his.insert('','end',values=row)
        return

    def search_record(self):

        """ SEARCH WILL DISPLAY RECORDS FROM HISTORY """
        
        top1=Toplevel(self.root,bg="orange")
        top1.geometry("1400x750+50+30")
        top1.title("SEARCH RECORD")
        seventh_frame=Frame(top1,bd=4,relief=GROOVE,bg="orange")
        seventh_frame.place(width=1400,height=750)

        self.display_sr=ttk.Treeview(seventh_frame,columns=("coustmer.cust_id","coustmer.cust_name","coustmer.cust_idproof","coustmer.cust_idproofno","coustmer.cust_days","coustmer.cust_time","coustmer.cust_city","coustmer.room_no","payment.payment_mode","payment.paiddate","room.room_cost*coustmer.cust_days","payment.status"))
                        
        self.display_sr.heading("coustmer.cust_id",text="ID")
        self.display_sr.heading("coustmer.cust_name",text="NAME")
        self.display_sr.heading("coustmer.cust_idproof",text="ID PROOF")
        self.display_sr.heading("coustmer.cust_idproofno",text="ID PROOF NO")
        self.display_sr.heading("coustmer.cust_days",text="DAYS")
        self.display_sr.heading("coustmer.cust_time",text="CHECK IN ")
        self.display_sr.heading("coustmer.cust_city",text="CITY")
        self.display_sr.heading("coustmer.room_no",text="ROOM NO")
        self.display_sr.heading("payment.payment_mode",text="PAYMENT MODE")
        self.display_sr.heading("payment.paiddate",text="CHECK OUT ")
        self.display_sr.heading("room.room_cost*coustmer.cust_days",text="AMOUNT")
        self.display_sr.heading("payment.status",text="STATUS")

        self.display_sr['show']='headings'
        self.display_sr.column("coustmer.cust_id",width=50)
        self.display_sr.column("coustmer.cust_name",width=100)
        self.display_sr.column("coustmer.cust_idproof",width=100)
        self.display_sr.column("coustmer.cust_idproofno",width=100)
        self.display_sr.column("coustmer.cust_days",width=50)
        self.display_sr.column("coustmer.cust_time",width=130)
        self.display_sr.column("coustmer.cust_city",width=100)
        self.display_sr.column("coustmer.room_no",width=50)
        self.display_sr.column("payment.payment_mode",width=100)
        self.display_sr.column("payment.paiddate",width=130)
        self.display_sr.column("room.room_cost*coustmer.cust_days",width=50)
        self.display_sr.column("payment.status",width=50)

        
        self.display_sr.pack(fill=BOTH,expand=1)


        cur=con.cursor()
        cur.execute("select coustmer.cust_id,coustmer.cust_name,coustmer.cust_idproof,coustmer.cust_idproofno,coustmer.cust_days,coustmer.cust_time,coustmer.cust_city,coustmer.room_no,payment.payment_mode,payment.paiddate,room.room_cost*coustmer.cust_days,payment.status from coustmer inner join payment on payment.cust_id=coustmer.cust_id inner join room on coustmer.room_no = room.room_no where payment.status='paid' and coustmer.cust_id = {}".format(self.searchname.get()))
        rows=cur.fetchall()
        if(len(rows)!=0):
            self.display_sr.delete(*self.display_sr.get_children())
            for row in rows:
                self.display_sr.insert('','end',values=row)
        return

    def clear(self):

        self.cust_name.set("")
        self.cust_idproof.set("")
        self.cust_idproofno.set("")
        self.cust_days.set("")
        self.cust_city.set("")
        self.room_no.set("")
        
        
        
root=Tk()

obj1=hotel(root)
root.mainloop()


