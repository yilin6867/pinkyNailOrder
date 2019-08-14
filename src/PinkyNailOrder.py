import tkinter as tk
import mysql.connector
from AddCustFrame import AddCustFrame
from tkinter import ttk

class PinkyNailOrder:
    def __init__(self, root):
        #declare system variable
        self.root = root
        #Create Meau bar
        menuBar= tk.Menu(self.root)
        self.root.config(menu=menuBar)
        custMenu = tk.Menu(menuBar, tearoff=0)
        custMenu.add_command(label='New Customer', command=lambda:self.show_frame(AddCustFrame))
        custMenu.add_command(label='Delete Customer', command=lambda:DelCust(self))
        menuBar.add_cascade(label='Customer', menu=custMenu)
        self.custFrame = CustFrame(self, self.root)
        self.frames = {}

        for F in (CustFrame, AddCustFrame):

            frame = F(self, self.root)

            self.frames[F] = frame

        self.show_frame(CustFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.getFrame().tkraise()
        
    def order(self, parent, root):
        self.calOrdFrame = CalOrdFrame(parent, root)
        
class CustFrame: 
    def __init__(self, parent, root):
        self.parent = parent
        #design config values
        self.lblYaxis=50
        self.defFont=('arial', 12)
        #declare variable to store value
##        self.custId = tk.StringVar()
##        self.custFN = tk.StringVar()
##        self.custLN = tk.StringVar()
##        self.custTele = tk.StringVar()
        #Create customer frame 
        self.custFrame = tk.Frame(root, background=dbg) #create the pane
        self.custFrame.place(width=600,height=600, x=0,y=0)
##        #create instruction
##        self.lblInstr = tk.Label(self.custFrame, font=('arial', 15),
##                            text='Please enter the customer information in the '+
##                            'following entry', bg=dbg)
##        self.lblInstr.place(height=25,width=580,x=0,y=10)
##        #create id entry
##        idValid = (root.register(self.idValidate),
##                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
####        self.lblID = tk.Label(self.custFrame, font=self.defFont,
####                         text='ID', bg=dbg)
####        self.lblID.place(height=20,width=20,x=25,y=lblYaxis)
####        
####        self.idEntry = tk.Entry(self.custFrame, font=self.defFont, bg=dbg, justify='left',textvariable=self.custId
####                                , validate='key', validatecommand=idValid)
####        self.idEntry.place(height=25,width=50,x=120,y=lblYaxis)
####        self.lblYaxis=self.lblYaxis+30
##        #create telephone last four digit
##        # valid percent substitutions (from the Tk entry man page)
##        # note: you only have to register the ones you need; this
##        # example registers them all for illustrative purposes
##        #
##        # %d = Type of action (1=insert, 0=delete, -1 for others)
##        # %i = index of char string to be inserted/deleted, or -1
##        # %P = value of the entry if the edit is allowed
##        # %s = value of entry prior to editing
##        # %S = the text string being inserted or deleted, if any
##        # %v = the type of validation that is currently set
##        # %V = the type of validation that triggered the callback
##        #      (key, focusin, focusout, forced)
##        # %W = the tk name of the widget
##        
##        teleValid = (root.register(self.teleValidate),
##                    '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
##        self.lblTele = tk.Label(self.custFrame, font=self.defFont, text='Telephone',
##                                bg=dbg)
##        self.lblTele.place(height=20,width=90,x=20,y=self.lblYaxis)
##        self.teleEntry = tk.Entry(self.custFrame, font=self.defFont, justify='left'
##                                  , bg=dbg, textvariable=self.custTele, validate='key'
##                                  , validatecommand=teleValid)
##        self.teleEntry.place(height=25,width=130,x=120,y=self.lblYaxis)
##        self.lblYaxis=self.lblYaxis+30
##
##        #create first name entry
##        nameValid = (root.register(self.nameValidate),
##                     '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
##        self.lblCustFN = tk.Label(self.custFrame, font=self.defFont
##                                  , text='First Name', bg=dbg)
##        self.lblCustFN.place(height=20,width=90,x=22,y=self.lblYaxis)
##        self.custFNentry = tk.Entry(self.custFrame, font=self.defFont, bg=dbg, justify='left',
##                        textvariable=self.custFN, validate='key', validatecommand=nameValid)
##        self.custFNentry.place(height=25,width=130,x=120,y=self.lblYaxis)
##        self.lblYaxis=self.lblYaxis+30
##
##        #create last name entry
##        self.lblCustLN = tk.Label(self.custFrame, font=self.defFont, text='Last Name',
##                             justify='left',bg=dbg)
##        self.lblCustLN.place(height=20,width=90,x=22,y=self.lblYaxis)
##        self.custLNentry = tk.Entry(self.custFrame, font=self.defFont, bg=dbg, justify='left',
##                        textvariable=self.custLN, validate='key', validatecommand=nameValid)
##        self.custLNentry.place(height=25,width=130,x=120,y=self.lblYaxis)
##        self.lblYaxis=self.lblYaxis+30
##
##        #create gender entry
##        self.lblCustGender= tk.Label(self.custFrame, font=self.defFont, text='Gender',
##                                     justify='left',bg=dbg)
##        self.lblCustGender.place(height=20,width=60,x=22,y=self.lblYaxis)
##        self.cmdCustGender= ttk.Combobox(self.custFrame, font=('arial', 12), justify='left')
##        self.cmdCustGender['value']=['Male', 'Female', 'Other', 'Nondisclosure']
##        self.cmdCustGender.place(height=25,width=130,x=120,y=self.lblYaxis)
##        self.lblYaxis=self.lblYaxis+40
##        #create buttons
##        self.btnSearch = tk.Button(self.custFrame, font=self.defFont, text='Search', justify='left',
##                                   command=lambda:self.searchCust)
##        self.btnSearch.place(height=30, width=60, x=50, y=self.lblYaxis)
##        self.btnOrder = tk.Button(self.custFrame, font=self.defFont, text='Order', justify='left',
##                                 command=lambda:parent.order(self, root))
##        self.btnOrder.place(height=30, width=60, x=150, y=self.lblYaxis)

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
        if text.isalpha():
            return True
        else:
            return False
    def getFrame(self):
        return self.custFrame

class DelCust:
    def __init__(self, parent):
        self.root = tk.Tk()
        self.parent=parent
        self.addCustFrame = tk.Frame(self.root, background=dbg)
        self.addCustFrame.place(width=600,height=200, x=0,y=0)
                                                    
if __name__ == "__main__":
    root = tk.Tk()
    dbg = 'white'
    #default value of the frame
    root.geometry("600x250+300+100")
    root.title("Online Ordering System")
    root.configure(background=dbg)
    app = PinkyNailOrder(root)
    root.mainloop()
