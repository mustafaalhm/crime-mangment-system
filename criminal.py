
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import db
from tkinter import messagebox
import validate_inputs

class criminal:
    

    def __init__(self,root):
        
        self.root =root
        self.root.geometry("1530x790+100+100")
        self.root.title("Criminal Mangement System")
        self.root.config(bg="light grey")
        self.root.resizable(False,False)
        
        # ================VARAIBLES============================
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_criminal_name=StringVar()
        self.var_nickname=StringVar()
        self.var_father_name=StringVar()
        self.var_arrest_date=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupuation=StringVar()
        self.var_birth_mark=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_crime_type=StringVar()

        self.var_search_by=StringVar()
        self.var_search_txt=StringVar()


        frame_main =Frame(root,width=1530,height=790,bg="red")
        frame_main.pack(fill=BOTH,expand=True)
        # ==================GUI SETUP=========================

        lbl_title = Label(frame_main,text="CRIMINAL MANGMENT SYSTEM",font=("arial",18,"bold"),bg="black")
        lbl_title.place(x=0,y=0,width=1530,height=60)

        img_logo =Image.open('images/lgog.jpeg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(frame_main,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=60,height=50)
        # =============image frame=============================
        image_frame =Frame(frame_main,bd=2,relief=RIDGE,bg='white')
        image_frame.place(x=0,y=60,width=1530,height=130)

        # ist
        img1 =Image.open('images/im1.jpeg')
        img1=img1.resize((540,160),Image.ANTIALIAS)

        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 =Label(image_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)
        # ist2
        img2 =Image.open('images/img3.jpeg')
        img2=img2.resize((540,160),Image.ANTIALIAS)

        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 =Label(image_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)
        # ist3
        img3 =Image.open('images/im2.jpeg')
        img3=img3.resize((580,160),Image.ANTIALIAS)

        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 =Label(image_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

       
        # ============================MAIN FRAME ============================
        main_frame= Frame(frame_main,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=190,width=1510,height=560)
        # ============================UPPER FRAME=============================
        top_frame= LabelFrame(main_frame,text="Criminal Information",font=("arial",17,"bold"),bd=2,relief=RIDGE,fg="red",bg='white')
        top_frame.place(x=10,y=10,width=1480,height=270)
        
        # ============================dOWN FRAME=============================
        down_frame= LabelFrame(main_frame,text="Criminal Information Table",font=("arial",17,"bold"),bd=2,relief=RIDGE,fg="red",bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        # ============================SEARCH IN dOWN FRAME=============================
        search_frame= LabelFrame(down_frame,text="Search Criminal Record",font=("arial",12,"bold"),bd=2,relief=RIDGE,fg="red",bg='white')
        search_frame.place(x=3,y=0,width=1470,height=60)
        
      
    #    ======================LABELS & ENTRY BOXES ==========================================
        
       
        # ----------CASE ID---------------
        case_id =Label(top_frame,text="CaseID:",font=("arail",11,"bold"),bg="white",fg="black")
        case_id.grid(row=0,column=0,padx=4,pady=7,sticky=W)

        caseEntry =Entry(top_frame,textvariable=self.var_case_id,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        caseEntry.grid(row=0,column=1,padx=4,pady=7,sticky=W)

        # ----------CRIMINAL NO---------------
        lbl_criminal_no =Label(top_frame,text="Criminal_NO:",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_criminal_no.grid(row=0,column=2,padx=4,pady=7,sticky=W)

        txt_criminal_no =Entry(top_frame,textvariable=self.var_criminal_no,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_criminal_no.grid(row=0,column=3,padx=4,pady=7,sticky=W)
        # ---------- CRIME TYPE---------------
        lbl_crime_type =Label(top_frame,text="Crime Type",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_crime_type.grid(row=0,column=4,padx=4,pady=7,sticky=W)

        txt_crime_type =Entry(top_frame,textvariable=self.var_crime_type,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_crime_type.grid(row=0,column=5,padx=4,pady=7,sticky=W)
        # ----------CRIMINAL NAME---------------
        lbl_criminal_name =Label(top_frame,text="Criminal_Name:",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_criminal_name.grid(row=1,column=0,padx=4,pady=7,sticky=W)

        txt_criminal_name =Entry(top_frame,textvariable=self.var_criminal_name,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_criminal_name.grid(row=1,column=1,padx=4,pady=7,sticky=W)
        
        # ----------NICKNAME---------------
        lbl_nickname =Label(top_frame,text="NickName:",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_nickname.grid(row=1,column=2,padx=4,pady=7,sticky=W)

        txt_nickname =Entry(top_frame,textvariable=self.var_nickname,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_nickname.grid(row=1,column=3,padx=4,pady=7,sticky=W)

        
        # ---------- FATHER NAME---------------
        lbl_father_name =Label(top_frame,text="Father Name",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_father_name.grid(row=1,column=4,padx=4,pady=7,sticky=W)

        txt_father_name =Entry(top_frame,textvariable=self.var_father_name,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_father_name.grid(row=1,column=5,padx=4,pady=7,sticky=W)

        # ----------ARREST DATE---------------
        lbl_arrest_date =Label(top_frame,text="Arrest Date:",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_arrest_date.grid(row=2,column=0,padx=4,pady=7,sticky=W)

        txt_arrest_Date =Entry(top_frame,textvariable=self.var_arrest_date,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_arrest_Date.grid(row=2,column=1,padx=4,pady=7,sticky=W)
        # ---------- DATE OF CRIME---------------
        lbl_date_of_crime =Label(top_frame,text="Date Of Crime",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_date_of_crime.grid(row=2,column=2,padx=4,pady=7,sticky=W)

        txt_date_of_crime =Entry(top_frame,textvariable=self.var_date_of_crime,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_date_of_crime.grid(row=2,column=3,padx=4,pady=7,sticky=W)
        # ---------- ADDRESS---------------
        lbl_address =Label(top_frame,text="Address",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_address.grid(row=3,column=0,padx=4,pady=7,sticky=W)

        txt_address =Entry(top_frame,textvariable=self.var_address,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_address.grid(row=3,column=1,padx=4,pady=7,sticky=W)

        # ---------- AGE---------------
        lbl_age =Label(top_frame,text="Age",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_age.grid(row=3,column=2,padx=4,pady=7,sticky=W)

        txt_age =Entry(top_frame,textvariable=self.var_age,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_age.grid(row=3,column=3,padx=4,pady=7,sticky=W)
        # ---------- OCCUPUTION---------------
        lbl_occupution =Label(top_frame,text="Occupution",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_occupution.grid(row=4,column=0,padx=4,pady=7,sticky=W)

        txt_occupution =Entry(top_frame,textvariable=self.var_occupuation,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_occupution.grid(row=4,column=1,padx=4,pady=7,sticky=W)
        # ---------- BIRTH MARK---------------
        lbl_birth_mark =Label(top_frame,text="Birth Mark",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_birth_mark.grid(row=4,column=2,padx=4,pady=7,sticky=W)

        txt_birth_mark =Entry(top_frame,textvariable=self.var_birth_mark,width=22,font=("arail",11,"bold"),bg="white",fg="black")
        txt_birth_mark.grid(row=4,column=3,padx=4,pady=7,sticky=W)
        # ===============GENDER==================================

        lbl_gender =Label(top_frame,text="Gender",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_gender.grid(row=2,column=4,padx=4,pady=7,sticky=W)
        # ------radio frame gender--------
        radio_frame_gender=Frame(top_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_gender.place(x=855,y=80,width=230,height=30)

        male =Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arail",11,"bold"),bg="white",fg="black",border=0,highlightbackground="white",
        activebackground="white",activeforeground="black")
        male.grid(row=0,column=0,padx=2,sticky=W)
        self.var_gender.set("male")

        female =Radiobutton(radio_frame_gender,variable=self.var_gender,text='Femal',value='female',font=("arail",11,"bold"),bg="white",fg="black",border=0,highlightbackground="white",indicatoron=1,
        activebackground="white",activeforeground="black",takefocus="no")
        female.grid(row=0,column=1,padx=2,sticky=W)
        self.var_gender.set("female")
        # ---------- WANTED---------------
        lbl_wanted =Label(top_frame,text="Wanted",font=("arail",11,"bold"),bg="white",fg="black")
        lbl_wanted.grid(row=3,column=4,padx=4,pady=7,sticky=W)

         # ------radio frame wanted--------
        radio_frame_wanted=Frame(top_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_wanted.place(x=855,y=120,width=230,height=30)

        yes_wanted =Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=("arail",11,"bold"),bg="white",fg="black",border=0,highlightbackground="white",
        activebackground="white",activeforeground="black")
        yes_wanted.grid(row=0,column=0,padx=2,sticky=W)
        self.var_wanted.set("yes")
        not_wanted =Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=("arail",11,"bold"),bg="white",fg="black",border=0,highlightbackground="white",
        activebackground="white",activeforeground="black")
        not_wanted.grid(row=0,column=1,padx=2,sticky=W)
        self.var_wanted.set("no")
       
        # ================Buttons =================================
        btn_frame=Frame(top_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=190,width=620,height=40)
       

        # ----add Button --------------
        btn_add=Button(btn_frame,text="Save",font=("arial",11,"bold"),width=14,bg="blue",fg="white",command=self.add_criminal)
        btn_add.grid(row=0 ,column=0,padx=3,pady=3)
        # ----update Button --------------
        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),width=14,bg="blue",fg="white",command=self.update_criminal)
        btn_update.grid(row=0 ,column=1,padx=3,pady=3)
        # ----delete Button --------------
        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),width=14,bg="blue",fg="white",command=self.delete_record)
        btn_delete.grid(row=0 ,column=2,padx=3,pady=3)
        # ----clear Button --------------
        btn_clear=Button(btn_frame,text="Clear",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_clear.grid(row=0 ,column=3,padx=3,pady=3)


        # ===========top area right background===================
        img_crime =Image.open('images/thief.jpeg')
        img_crime =img_crime.resize((370,225),Image.ANTIALIAS)

        self.photo_crime = ImageTk.PhotoImage(img_crime)

        theif_lbl=Label(top_frame,image=self.photo_crime,padx=10)
        theif_lbl.place(x=1100,y=0,width=370,height=225)
    # ==================search frame Elements===============================
        lbl_search_by =Label(search_frame,text="Search By:",font=("arail",11,"bold"),bg="red",fg="black")
        lbl_search_by.grid(row=0,column=0,padx=4,pady=7,sticky=W)

        search_box =ttk.Combobox(search_frame,textvariable=self.var_search_by,font=("arail",12,"bold"),width=18,state="readonly")
        search_box['values']=("Selecet Options","Case_id","Criminal_No","Criminal_Name")
        search_box.current(0)
        search_box.grid(row=0,column=1,padx=5,sticky=W)

        txt_search =Entry(search_frame,textvariable=self.var_search_txt,width=18,font=("arail",11,"bold"),bg="white",fg="black")
        txt_search.grid(row=0,column=2,padx=4,pady=7,sticky=W)

        # ----search Button --------------
        btn_search=Button(search_frame,text="Search",font=("arial",11,"bold"),width=14,bg="blue",fg="white",command=self.search_data)
        btn_search.grid(row=0 ,column=3,padx=3,pady=3)
        # ----all Button --------------
        btn_show_all=Button(search_frame,text="Show All",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_show_all.grid(row=0 ,column=4,padx=3,pady=3)
       
        lbl_agency = Label(search_frame,text="NATIONAL CRIME AGENCY",font=("arial",24,"bold"),fg="blue",bg="white")
        lbl_agency.grid(row=0,column=6,padx=150)

        # =====================table down frame===========================================
        table_frame =Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       
        self.criminal_table = ttk.Treeview(table_frame,columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
         
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        # =====================treeview table========================
        self.criminal_table.heading('1',text="CaseId")
        self.criminal_table.heading('2',text="CrimeNo")
        self.criminal_table.heading('3',text="Crime Type")
        self.criminal_table.heading('4',text="Criminal Name")
        self.criminal_table.heading('5',text="NickName")
        self.criminal_table.heading('6',text="Father Name")
        self.criminal_table.heading('7',text="ArrestDate")
        self.criminal_table.heading('8',text="CrimeOfDate")
        self.criminal_table.heading('9',text="Address")
        self.criminal_table.heading('10',text="Age")
        self.criminal_table.heading('11',text="Occupuation")
        self.criminal_table.heading('12',text="Birth Mark")
        self.criminal_table.heading('13',text="Gender")
        self.criminal_table.heading('14',text="Wanted")


        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table['show']='headings'


    # ========================data base function==========
        self.get_criminal_data()
#    ==================add function=======================
    def add_criminal(self):
        
        validate_ok= validate_inputs.validate_input_length(self.var_criminal_no.get(),self.var_crime_type.get(),self.var_criminal_name.get(),self.var_nickname.get()
            ,self.var_father_name.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),
            self.var_occupuation.get(),self.var_birth_mark.get(),self.var_gender.get(),self.var_wanted.get())
        
        database="criminal.db"
        dataset=(self.var_criminal_no.get(),self.var_crime_type.get(),self.var_criminal_name.get(),self.var_nickname.get()
        ,self.var_father_name.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),
        self.var_occupuation.get(),self.var_birth_mark.get(),self.var_gender.get(),self.var_wanted.get())
         
        try:
            conn= db.create_connection(database)

            with conn:
                db.insert_data(conn, dataset)
                messagebox.showinfo(title="Success",message="Criminal recorded record has been added")

                self.get_criminal_data()
        except Exception as e:
            messagebox.showerror(title="Faild",message=f'Due To {str(e)}')
    # ===============================================update date ===========
    def update_criminal(self):
        ID= self.var_case_id.get()
        validate_ok= validate_inputs.validate_input_length(self.var_criminal_no.get(),self.var_crime_type.get(),self.var_criminal_name.get(),self.var_nickname.get()
            ,self.var_father_name.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),
            self.var_occupuation.get(),self.var_birth_mark.get(),self.var_gender.get(),self.var_wanted.get())
        
        database="criminal.db"
        dataset=(self.var_criminal_no.get(),self.var_crime_type.get(),self.var_criminal_name.get(),self.var_nickname.get()
            ,self.var_father_name.get(),self.var_arrest_date.get(),self.var_date_of_crime.get(),self.var_address.get(),self.var_age.get(),
            self.var_occupuation.get(),self.var_birth_mark.get(),self.var_gender.get(),self.var_wanted.get())
        try:
            conn= db.create_connection(database)
    #       
            with conn:
                db.update_data(conn,dataset,ID)
                messagebox.showinfo(title="Success",message="Criminal recorded updated successfully")
        
                self.get_criminal_data()
        except Exception as e:
            messagebox.showerror(title="Faild",message=f'Due To {str(e)}')

    # ============Delete function=================
    def delete_record(self):
        Id= self.var_case_id.get()
        database ="criminal.db"
        is_ok =messagebox.askokcancel(title=f'Delete {self.var_criminal_name.get()}',message=f'Are yo sure you want to delete {self.var_criminal_name.get()} record')
        if is_ok:
            try:
                conn= db.create_connection(database)
                with conn:
                    db.delete_data(conn,Id)
                    messagebox.showinfo(title="Success",message="Criminal recorded Deleted successfully")
                self.get_criminal_data()
            except Exception as e:
                  messagebox.showerror(title="Faild",message=f'Due To {str(e)}')

    # =============get data from database function========================
    def get_criminal_data(self):
        try:
            database="criminal.db"
            conn=db.create_connection(database)
            with conn:
                my_data=db.get_data(conn)
                if len(my_data)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in my_data:
                        self.criminal_table.insert("",END,values=i)
                
        except Exception as e:
              print(e)
        
    # =============get data cursor treeview ===========
    # =============search options======================
    def search_data(self):
        if self.var_search_txt.get()=="":
            messagebox.showerror(title="error",message='all fields are required')
        else:
            database= "criminal.db"
            conn =db.create_connection(database)
            try:
                with conn:
                    my_data=db.search_data(conn,self.var_search_by.get(),self.var_search_txt.get())
                    if len(my_data) !=0:
                        self.criminal_table.delete(*self.criminal_table.get_children())
                        for i in my_data:
                            self.criminal_table.insert("",END,values=i)
                    else:
                        messagebox.showinfo(title="Not Found",message=f'the:{self.var_search_by.get()} {self.var_search_txt.get()} not found')
            except Exception as e:
                    messagebox.showerror(title="Faild",message=f'Due To {str(e)}')
    def get_cursor(self,event=""):
        cursor_row = self.criminal_table.focus()
        content= self.criminal_table.item(cursor_row)
        data =content["values"]
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_crime_type.set(data[2])
        self.var_criminal_name.set(data[3])
        self.var_nickname.set(data[4])
        self.var_father_name.set(data[5])
        self.var_arrest_date.set(data[6])
        self.var_date_of_crime.set(data[7])
        self.var_address.set(data[8])
        self.var_age.set(data[9])
        self.var_occupuation.set(data[10])
        self.var_birth_mark.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])
        
       
       
    
        
        
        
       
       
    
if __name__=="__main__":
    root=Tk()
    obj=criminal(root)
    root.mainloop()