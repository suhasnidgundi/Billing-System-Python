from tkinter import*
from tkinter import messagebox
import random, math, os         
from plyer import notification

class Shop:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("| Billing Software | By Suhas Nidgundi |")
        self.root.resizable(True, True)
        # self.root.wm_iconbitmap("images//Shop.ico")
        self.root.config(bg="grey")

        bg_color = "#074463"
        title = Label(self.root,  text="Billing Software - | By Suhas Nidgundi |", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("calibri", 30, "bold")).pack(side=TOP, fill=X)

        # =================== All Variable ======================= #
        # =================== Cosmetics ======================= #
        self.b1 = IntVar()
        self.b2 = IntVar()
        self.b3 = IntVar()
        self.b4 = IntVar()
        self.b5 = IntVar()
        self.b6 = IntVar()

        # =================== Grocery ======================= #
        self.g1 = IntVar()
        self.g2 = IntVar()
        self.g3 = IntVar()
        self.g4 = IntVar()
        self.g5 = IntVar()
        self.g6 = IntVar()

        # =================== Cold Drinks ======================= #
        self.d1 = IntVar()
        self.d2 = IntVar()
        self.d3 = IntVar()
        self.d4 = IntVar()
        self.d5 = IntVar()
        self.d6 = IntVar()

        # =================== Customer Detail ======================= #
        self.c_name = StringVar()
        self.c_phone = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # =================== Total Product & Tax Variable ======================= #
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()


        # =================== Customer Detail Frame ======================= #
        F1 = LabelFrame(self.root, text="Customer Details", relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, pady=2)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="consolos 15 bold", bd=7, relief=RIDGE).grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=15, textvariable=self.c_phone, font="consolos 15 bold", bd=7, relief=RIDGE).grid(row=0, column=3, padx=10, pady=5)

        c_bill_lbl = Label(F1, text="Bill Number.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="consolos 15 bold", bd=7, relief=RIDGE).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search", command=self.find_bill, bg="white", fg="black", width=10, bd=7, relief=RIDGE, font="arial 12 bold", cursor="hand2").grid(row=0, column=6, padx=10, pady=10)
        
        # =================== Cosmetics Frame ======================= #
        F2 = LabelFrame(self.root, text="Cosmetics", bd=6, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, pady=2)
        F2.place(x=5, y=180, width=325, height=380)

        c1_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F2, width=10, textvariable=self.b1, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F2, width=10, textvariable=self.b2, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F2, width=10, textvariable=self.b3, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lbl = Label(F2, text="Hair Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F2, width=10, textvariable=self.b4, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lbl = Label(F2, text="Hair Shampoo", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F2, width=10, textvariable=self.b5, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lbl = Label(F2, text="Body Loshan", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F2, width=10, textvariable=self.b6, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)
        
        # =================== Grocery Frame ======================= #
        F3 = LabelFrame(self.root, text="Grocery", bd=6, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, pady=2)
        F3.place(x=335, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.g1, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.g2, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.g3, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.g4, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.g5, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.g6, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # =================== Cold Drink Frame ======================= #
        F4 = LabelFrame(self.root, text="Cold Drink", bd=6, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, pady=2)
        F4.place(x=665, y=180, width=325, height=380)

        d1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        d1_txt = Entry(F4, width=10, textvariable=self.d1, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        d2_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        d2_txt = Entry(F4, width=10, textvariable=self.d2, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        d3_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        d3_txt = Entry(F4, width=10, textvariable=self.d3, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        d4_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        d4_txt = Entry(F4, width=10, textvariable=self.d4, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        d5_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        d5_txt = Entry(F4, width=10, textvariable=self.d5, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        d6_lbl = Label(F4, text="Red Bull", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        d6_txt = Entry(F4, width=10, textvariable=self.d6, font="consolos 16 bold", bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # =================== Bill Area Frame ======================= #
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=995, y=180, width=360, height=380)
        bill_title = Label(F5, text="Bill Area", font="calibri 15 bold", bd=5, relief=SUNKEN).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        # =================== Bill Area Frame ======================= #
        F6 = LabelFrame(self.root, text="Bill Menu", bd=8, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color, pady=2)
        F6.place(x=0, y=560, relwidth=1, height=140)

        p1_lbl = Label(F6, text="Total Cosmetic Price", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=0, column=0, padx=20, pady=1, sticky="w")
        p1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="consolos 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        p2_lbl = Label(F6, text="Total Grocery Price", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        p2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="consolos 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        p3_lbl = Label(F6, text="Total Cold Drink Price", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        p3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="consolos 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        t1_lbl = Label(F6, text="Cosmetic Tax", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        t1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="consolos 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        t2_lbl = Label(F6, text="Grocery Tax", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        t2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="consolos 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        t3_lbl = Label(F6, text="Cold Drink Tax", font=("times new roman", 14, "bold"), bg=bg_color, fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        t3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="consolos 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)
        
        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=800, width=540, height=105)

        total_btn = Button(btn_F, text="Total", command=self.total, bg="#0875B7", fg="white", pady=15, font="arial 15 bold", relief=RIDGE, cursor="hand2", width=8, bd=3).grid(row=0, column=0, padx=10, pady=10)
        Gbill_btn = Button(btn_F, text="Gbill", command=self.bill_area, bg="#0875B7", fg="white", pady=15, font="arial 15 bold", relief=RIDGE, cursor="hand2", width=8, bd=3).grid(row=0, column=1, padx=10, pady=10)
        Clear_btn = Button(btn_F, text="Clear", bg="#0875B7", command=self.clear, fg="white", pady=15, font="arial 15 bold", relief=RIDGE, cursor="hand2", width=8, bd=3).grid(row=0, column=2, padx=10, pady=10)
        Exit_btn = Button(btn_F, text="Exit", bg="#0875B7", fg="white", pady=15, font="arial 15 bold", relief=RIDGE, cursor="hand2", command=self.Exit, width=8, bd=3).grid(row=0, column=3, padx=10, pady=10)

    def clear(self):
        op = messagebox.askyesno("!!! CLEAR !!!", "!!! *** DO YOU WANT TO CLEAR DATA *** !!!")
        if op>0:
            # =================== All Variable ======================= #
            # =================== Cosmetics ======================= #
            self.b1.set(0)
            self.b2.set(0)
            self.b3.set(0)
            self.b4.set(0)
            self.b5.set(0)
            self.b6.set(0)

            # =================== Grocery ======================= #
            self.g1.set(0)
            self.g2.set(0)
            self.g3.set(0)
            self.g4.set(0)
            self.g5.set(0)
            self.g6.set(0)

            # =================== Cold Drinks ======================= #
            self.d1.set(0)
            self.d2.set(0)
            self.d3.set(0)
            self.d4.set(0)
            self.d5.set(0)
            self.d6.set(0)

            # =================== Customer Detail ======================= #
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")

            # =================== Total Product & Tax Variable ======================= #
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            self.txtarea.delete('1.0', END)


    def Exit(self):
        op = messagebox.askyesno("!!! EXIT !!!", "!!! *** DO YOU REALY WANT TO CLOSE *** !!!")
        if op>0:
            self.root.destroy()
            notification.notify( 

                title = "THANK YOU", 
                message="Thank you for taking the time to share your experience with Us!" , 
                app_name = "BILLING SOFTWARE - | BY SUHAS NIDGUNDI |",
                app_icon = "images\\Shop.ico",
                ticker = "| BY SUHAS NIDGUNDI |",
                timeout=10

            )

    def total(self):
        # =================== Cosmetic Frame ======================= #
        self.c_s_p = self.b1.get()*40
        self.c_fc_p = self.b2.get()*40
        self.c_fw_p = self.b3.get()*40
        self.c_ho_p = self.b4.get()*40
        self.c_hs_p = self.b5.get()*40
        self.c_b_p = self.b6.get()*40

        self.total_cosmetic_price = float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_ho_p+
            self.c_hs_p+
            self.c_b_p
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05), 2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        # =================== Grocery Frame ======================= #
        self.g_r_p = self.g1.get()*40
        self.g_fo_p = self.g2.get()*40
        self.g_d_p = self.g3.get()*40
        self.g_w_p = self.g4.get()*40
        self.g_s_p = self.g5.get()*40
        self.g_t_p = self.g6.get()*40

        self.total_grocery_price = float(
            self.g_r_p+
            self.g_fo_p+
            self.g_d_p+
            self.g_w_p+
            self.g_s_p+
            self.g_t_p
        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.05), 2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        # =================== Cold Drink Frame ======================= #
        self.d_m_p = self.d1.get()*40
        self.d_f_p = self.d2.get()*40
        self.d_t_p = self.d3.get()*40
        self.d_l_p = self.d4.get()*40
        self.d_s_p = self.d5.get()*40
        self.d_rb_p = self.d6.get()*40

        self.total_cold_drink_price = float(
            self.d_m_p+
            self.d_f_p+
            self.d_t_p+
            self.d_l_p+
            self.d_s_p+
            self.d_rb_p
        )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax = round((self.total_cold_drink_price*0.05), 2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill = float(
            self.total_cosmetic_price+
            self.total_grocery_price+
            self.total_cold_drink_price+
            self.c_tax+
            self.g_tax+
            self.d_tax
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome To Suveesoft Retail\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}\n")
        self.txtarea.insert(END, "=======================================")
        self.txtarea.insert(END, "\n Products\t\tQTY\t\tPrice\n")
        self.txtarea.insert(END, "=======================================")

    def bill_area(self):
        if self.grocery_price.get()=="Rs. 0.0" or self.cold_drink_price.get()=="Rs. 0.0" or self.cosmetic_price.get()=="Rs. 0.0":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** PLEASE PURCHASE A PRODUCT *** !!!")

        elif self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** CUSTOMER DETAILS ARE MUST *** !!!")

        elif self.grocery_price.get()=="" or self.cold_drink_price.get()=="" or self.cosmetic_price.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** PLEASE PURCHASE A PRODUCT *** !!!")

        else:
            self.welcome_bill()
            # =================== Cosmetic Function ======================= #
            if self.b1.get()!=0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t{self.b1.get()}\t\t{self.c_s_p}")
            if self.b2.get()!=0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.b2.get()}\t\t{self.c_fc_p}")
            if self.b3.get()!=0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.b3.get()}\t\t{self.c_fw_p}")
            if self.b4.get()!=0:
                self.txtarea.insert(END, f"\n Hair Oil\t\t{self.b4.get()}\t\t{self.c_ho_p}")
            if self.b5.get()!=0:
                self.txtarea.insert(END, f"\n Hair Shampoo\t\t{self.b5.get()}\t\t{self.c_hs_p}")
            if self.b6.get()!=0:
                self.txtarea.insert(END, f"\n Body Loshan\t\t{self.b6.get()}\t\t{self.c_b_p}")

            # =================== Grocery Function ======================= #
            if self.g1.get()!=0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.g1.get()}\t\t{self.g_r_p}")
            if self.g2.get()!=0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.g2.get()}\t\t{self.g_fo_p}")
            if self.g3.get()!=0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.g3.get()}\t\t{self.g_d_p}")
            if self.g4.get()!=0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.g4.get()}\t\t{self.g_w_p}")
            if self.g5.get()!=0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.g5.get()}\t\t{self.g_s_p}")
            if self.g6.get()!=0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.g6.get()}\t\t{self.g_t_p}")

            # =================== Cold Drink Function ======================= #
            if self.d1.get()!=0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.d1.get()}\t\t{self.d_m_p}")
            if self.d2.get()!=0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.d2.get()}\t\t{self.d_f_p}")
            if self.d3.get()!=0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.d3.get()}\t\t{self.d_t_p}")
            if self.d4.get()!=0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.d4.get()}\t\t{self.d_l_p}")
            if self.d5.get()!=0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.d5.get()}\t\t{self.d_s_p}")
            if self.d6.get()!=0:
                self.txtarea.insert(END, f"\n Red Bull\t\t{self.d6.get()}\t\t{self.d_rb_p}")

            self.txtarea.insert(END, "\n---------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END, "\n---------------------------------------")
            self.txtarea.insert(END, f"\n Total Bill : \t\t\t{self.Total_bill}")
            self.txtarea.insert(END, "\n---------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("!!! SAVE BILL !!!", "DO YOU WANT TO SAVE BILL ?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close
            messagebox.showinfo("!!! SAVED !!!", f"BILL NO : {self.bill_no.get()} SAVED SUCCESSFULLY")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"

        if present=="no":
            messagebox.showerror("!!! ERROR 404 !!!", f"!!! *** INVAILD BILL NO : {self.search_bill.get()} *** !!!")

root = Tk()
obj = Shop(root)
root.mainloop() 