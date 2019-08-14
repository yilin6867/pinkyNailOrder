import tkinter as tk
import mysql.connector
from tkinter import ttk

dbg='white'

class AddCustFrame: 
    def __init__(self, parent, root):
        self.root = root
        self.parent = parent
        #design config values
        self.lblYaxis=50
        self.defFont=('arial', 12)
        #declare variable to store value
        self.custFN = tk.StringVar()
        self.custLN = tk.StringVar()
        self.custTele = tk.StringVar()
        #Create customer frame 
        self.addCustFrame = tk.Frame(self.root, background=dbg) #create the pane
        self.addCustFrame.place(width=600,height=600, x=0,y=0)
        #create instruction
        self.lblInstr = tk.Label(self.addCustFrame, font=('arial', 15),
                            text='Please enter the customer information in the '+
                            'following entry', bg=dbg)
        self.lblInstr.place(height=25,width=580,x=0,y=10)
        #create id entry
        idValid = (self.root.register(self.idValidate),
                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
##        self.lblID = tk.Label(self.addCustFrame, font=self.defFont,
##                         text='ID', bg=dbg)
##        self.lblID.place(height=20,width=20,x=25,y=lblYaxis)
##        
##        self.idEntry = tk.Entry(self.addCustFrame, font=self.defFont, bg=dbg, justify='left',textvariable=self.custId
##                                , validate='key', validatecommand=idValid)
##        self.idEntry.place(height=25,width=50,x=120,y=lblYaxis)
##        self.lblYaxis=self.lblYaxis+30
        #create telephone last four digit
        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget
        
        teleValid = (self.root.register(self.teleValidate),
                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.lblTele = tk.Label(self.addCustFrame, font=self.defFont, text='Telephone',
                                bg=dbg)
        self.lblTele.place(height=20,width=90,x=20,y=self.lblYaxis)
        self.teleEntry = tk.Entry(self.addCustFrame, font=self.defFont, justify='left'
                                  , bg=dbg, textvariable=self.custTele, validate='key'
                                  , validatecommand=teleValid)
        self.teleEntry.place(height=25,width=130,x=120,y=self.lblYaxis)
        self.lblYaxis=self.lblYaxis+30

        #create first name entry
        nameValid = (self.root.register(self.nameValidate),
                     '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.lblCustFN = tk.Label(self.addCustFrame, font=self.defFont
                                  , text='First Name', bg=dbg)
        self.lblCustFN.place(height=20,width=90,x=22,y=self.lblYaxis)
        self.custFNentry = tk.Entry(self.addCustFrame, font=self.defFont, bg=dbg, justify='left',
                        textvariable=self.custFN, validate='key', validatecommand=nameValid)
        self.custFNentry.place(height=25,width=130,x=120,y=self.lblYaxis)
        self.lblYaxis=self.lblYaxis+30

        #create last name entry
        self.lblCustLN = tk.Label(self.addCustFrame, font=self.defFont, text='Last Name',
                             justify='left',bg=dbg)
        self.lblCustLN.place(height=20,width=90,x=22,y=self.lblYaxis)
        self.custLNentry = tk.Entry(self.addCustFrame, font=self.defFont, bg=dbg, justify='left',
                        textvariable=self.custLN, validate='key', validatecommand=nameValid)
        self.custLNentry.place(height=25,width=130,x=120,y=self.lblYaxis)
        self.lblYaxis=self.lblYaxis+30

        #create gender entry
        self.lblCustGender= tk.Label(self.addCustFrame, font=self.defFont, text='Gender',
                                     justify='left',bg=dbg)
        self.lblCustGender.place(height=20,width=60,x=22,y=self.lblYaxis)
        self.cmdCustGender= ttk.Combobox(self.addCustFrame, font=('arial', 12), justify='left')
        self.cmdCustGender['value']=['Male', 'Female', 'Other', 'Nondisclosure']
        self.cmdCustGender.place(height=25,width=130,x=120,y=self.lblYaxis)
        self.lblYaxis=self.lblYaxis+40
        #create buttons
        self.btnAdd = tk.Button(self.addCustFrame, font=self.defFont, text='Add', justify='left',
                                command=lambda:self.addCust())
        self.btnAdd.place(height=30, width=60, x=50, y=self.lblYaxis)
        self.btnReset = tk.Button(self.addCustFrame, font=self.defFont, text='Reset', justify='left',
                                   command=lambda:self.reset)
        self.btnReset.place(height=30, width=60, x=150, y=self.lblYaxis)
        self.btnCancel = tk.Button(self.addCustFrame, font=self.defFont, text='Cancel', justify='left',
                                 command=lambda:parent.order(self, self.root))
        self.btnCancel.place(height=30, width=60, x=250, y=self.lblYaxis)

    def idValidate(self, action, index, value_if_allowed, prior_value, text,
                 validation_type, trigger_type, widget_name):
        try:
            int(text)
            if len(value_if_allowed) <=4:
                return True
            else:
                return False
        except ValueError:
            return False
    def teleValidate(self, action, index, value_if_allowed, prior_value, text,
                 validation_type, trigger_type, widget_name):
        try:
            int(text)
            if (len(value_if_allowed) <= 10):
                return True
            else:
                return False
        except ValueError:
            return False
    def nameValidate(self, action, index, value_if_allowed, prior_value, text,
                 validation_type, trigger_type, widget_name):
        if text.isalpha() or text == ' ':
            return True
        else:
            return False
        
    def addCust(self):
        print(self.custTele.get())
        if self.custTele.get() == '' or self.custFN.get() == '' or self.custLN.get() == '':
            return None
        if self.cmdCustGender.get() == 'Male':
            gender = 'M'
        elif self.cmdCustGender.get() == 'Female':
            gender = 'F'
        elif self.cmdCustGender.get() == 'Other':
            gender = 'O'
        else:
            gender = 'N'
        ################# Create a database connection ##################
        try:
            mysqlDB = mysql.connector.connect(
                host='localhost',
                user='kjgmk',
                passwd='Mysql@yilin@6867',
                database='order_transaction'
            )
            mycursor = mysqlDB.cursor() ##create a cursor to point to the table
            stmt = 'INSERT INTO customer (CUST_ID, F_NAME, L_NAME, GENDER) VALUES(%s,%s,%s,%s); COMMIT;'
            val = (self.custTele.get(), self.custFN.get(), self.custLN.get(), gender)
            print(val)
            print('Start inserting')
            mycursor.execute(stmt, val)
            print('Insert finished')
            mycursor.close()
            mysqlDB.close()
        except:
            print('Error in insert into table')

    def getFrame(self):
        return self.addCustFrame
