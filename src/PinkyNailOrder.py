import tkinter as tk
import mysql.connector
from tkinter import ttk

class PinkyNailOrder:
    def __init__(self, root):
        #declare system variable
        self.root = root
##        #Create Meau bar
##        menuBar= tk.Menu(self.root)
##        self.root.config(menu=menuBar)
##        custMenu = tk.Menu(menuBar, tearoff=0)
##        custMenu.add_command(label='New Customer', command=self.addCust)
##        custMenu.add_command(label='Delete Customer', command=self.delCust)
##        menuBar.add_cascade(label='Customer', menu=custMenu)
        self.custFrame = CustFrame(self, self.root)
        
    def order(self, parent, root):
        self.calOrdFrame = CalOrdFrame(parent, root)
        
class CustFrame: 
    def __init__(self, parent, root):
        self.parent = parent
        #declare variable to store value
        self.custId = tk.StringVar()
        self.custFN = tk.StringVar()
        self.custLN = tk.StringVar()
        self.custTele = tk.StringVar()
        #Create customer frame 
        self.custFrame = tk.Frame(root, background=dbg) #create the pane
        self.custFrame.place(width=600,height=600, x=0,y=0)
        #create instruction
        self.lblInstr = tk.Label(self.custFrame, font=('arial', 15),
                            text='Please enter the customer information in the '+
                            'following entry', bg=dbg)
        self.lblInstr.place(height=25,width=580,x=0,y=10)
        #create id entry
        idValid = (root.register(self.idValidate),
                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.lblID = tk.Label(self.custFrame, font=('arial', 12),
                         text='ID', bg=dbg)
        self.lblID.place(height=20,width=20,x=25,y=50)
        
        self.idEntry = tk.Entry(self.custFrame, font=('arial', 12), bg=dbg, justify='left',textvariable=self.custId
                                , validate='key', validatecommand=idValid)
        self.idEntry.place(height=25,width=50,x=120,y=50)
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

        teleValid = (root.register(self.teleValidate),
                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.lblTele = tk.Label(self.custFrame, font=('arial', 12), text='Telephone',
                                bg=dbg)
        self.lblTele.place(height=20,width=90,x=20,y=80)
        self.teleEntry = tk.Entry(self.custFrame, font=('arial', 12), justify='left'
                                  , bg=dbg, textvariable=self.custTele, validate='key'
                                  , validatecommand=teleValid)
        self.teleEntry.place(height=25,width=130,x=120,y=80)
        #create first name entry
        nameValid = (root.register(self.nameValidate),
                     '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.lblCustFN = tk.Label(self.custFrame, font = ('arial', 12)
                                  , text='First Name', bg=dbg)
        self.lblCustFN.place(height=20,width=90,x=22,y=110)
        self.custFNentry = tk.Entry(self.custFrame, font=('arial', 12), bg=dbg, justify='left',
                        textvariable=self.custFN, validate='key', validatecommand=nameValid)
        self.custFNentry.place(height=25,width=130,x=120,y=110)
        #create last name entry
        self.lblCustLN = tk.Label(self.custFrame, font=('arial', 12), text='Last Name',
                             justify='left',bg=dbg)
        self.lblCustLN.place(height=20,width=90,x=22,y=140)
        self.custLNentry = tk.Entry(self.custFrame, font=('arial', 12), bg=dbg, justify='left',
                        textvariable=self.custLN, validate='key', validatecommand=nameValid)
        self.custLNentry.place(height=25,width=130,x=120,y=140)
        #create buttons
        self.btnAdd = tk.Button(self.custFrame, font=('arial', 12), text='Add', justify='left',
                                command=lambda:self.addCust)
        self.btnAdd.place(height=30, width=60, x=150, y=170)
        self.btnDel = tk.Button(self.custFrame, font=('arial', 12), text='Delete', justify='left',
                                command=lambda:self.delCust)
        self.btnDel.place(height=30, width=60, x=250, y=170)
        self.btnOrder = tk.Button(self.custFrame, font=('arial', 12), text='Order', justify='left',
                                 command=lambda:parent.order(self, root))
        self.btnOrder.place(height=30, width=60, x=350, y=170)

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
            if (len(value_if_allowed) <= 9):
                return True
            else:
                return False
        except ValueError:
            return False
    def nameValidate(self, action, index, value_if_allowed, prior_value, text,
                 validation_type, trigger_type, widget_name):
        if text.isalpha():
            return True
        else:
            return False

    def addCust(self):
        return None
    def delCust(self):
        return None

class CalOrdFrame:
    def __init__(self, parent, root):
        self.parent=parent
        self.calOrdFrame = tk.Frame(root, background=dbg)
        self.calOrdFrame.place(width=600,height=200, x=0,y=0)
        self.lblInstr = tk.Label(self.calOrdFrame, font=('arial', 15, 'bold'),
                            text='Please select customer service in the entry below',
                                 bg=dbg, justify='left')
        self.lblInstr.place(height=25,width=500,x=0,y=10)

        self.lblType = tk.Label(self.calOrdFrame, font=('arial', 12),
                                 text='Service Type', bg=dbg)
        self.lblType.place(height=20,width=100,x=25,y=50)
        self.type = ttk.Combobox(self.calOrdFrame, font=('arial', 12), width=30,justify='left')
        self.type['value']=self.getService('TYPE')
        self.type.bind('<<ComboboxSelected>>'
                       , lambda event: self.updateSName(event, self.type.get()))
        self.type.place(height=25, width=300, x=135, y=50)
        
        self.lblName = tk.Label(self.calOrdFrame, font=('arial', 12),
                                text='Service Name', bg=dbg)
        self.lblName.place(height=20, width=105, x=25, y=85)
        self.name = ttk.Combobox(self.calOrdFrame, font=('arial', 12), width=100, justify='left')
        self.name.place(height=25, width=300, x=135, y=85)

        self.lblWorker = tk.Label(self.calOrdFrame, font=('arial', 12)
                                  , text='Worker Name', bg=dbg)

    def getService(self, keyword, where='WHERE 1 =1'):
        mysqlDB = mysql.connector.connect(
            host='localhost',
            user='kjgmk',
            passwd='Mysql@yilin@6867',
            database='catolog'
        )
        mycursor = mysqlDB.cursor()
        print(where)
        mycursor.execute('SELECT DISTINCT '+ keyword +' FROM SERVICE '
                         + where)
        table = mycursor.fetchall()
        myresult =[]
        for row in table:
            for col in row:
                myresult.append(col)
        print(myresult)
        return myresult
    def updateSName(self, event, where):
        self.name['value']=self.getService('NAME', "WHERE TYPE = '" + where+"'")
                                                          
if __name__ == "__main__":
    root = tk.Tk()
    dbg = 'white'
    #default value of the frame
    root.geometry("600x250+300+100")
    root.title("Online Ordering System")
    root.configure(background=dbg)
    app = PinkyNailOrder(root)
    root.mainloop()
