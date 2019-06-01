import tkinter as tk

class PinkyNailOrder:
    def __init__(self, root):
        #declare system variable
        self.root = root
        self.custId = tk.StringVar()
        self.custFN = tk.StringVar()
        self.custLN = tk.StringVar()
        #Create Meau bar
        menu= tk.Menu(self.root)
        self.root.config(menu=menu)
        newCust = tk.Menu(menu)
        newCust.add_command(label='New Customer', command=self.addCust)
        menu.add_cascade(label='Edit', menu=newCust)
        self.CustFrame()
        
    def CustFrame(self): #change it to class
        #Create customer frame 
        Frame = tk.Frame(self.root, background=dbg) #create the pane
        custFrame.place(width=600,height=200, x=0,y=0)
        #create instruction
        lblInstr = tk.Label(custFrame, font=('arial', 15, 'bold'),
                            text='Please Enter the customer information in the '+
                            'follow enter', bg=dbg)
        lblInstr.place(height=20,width=580,x=0,y=10)
        #create id
        lblID = tk.Label(custFrame, font=('arial', 12, 'bold'),
                         text='ID', bg=dbg)
        lblID.place(height=20,width=20,x=25,y=40)
        
        idEntry = tk.Entry(custFrame, font=('arial', 12), bg=dbg, justify='left',
                        textvariable=self.custId)
        idEntry.place(height=25,width=40,x=45,y=40)
        #create first name
        lblCustFN = tk.Label(custFrame, font = ('arial', 12, 'bold'), text='First Name',
                             justify='left',bg=dbg)
        lblCustFN.place(height=20,width=90,x=100,y=40)
        custFNentry = tk.Entry(custFrame, font=('arial', 12), bg=dbg, justify='left',
                        textvariable=self.custFN)
        custFNentry.place(height=25,width=130,x=190,y=40)
        #create last name
        lblCustLN = tk.Label(custFrame, font=('arial', 12, 'bold'), text='Last Name',
                             justify='left',bg=dbg)
        lblCustLN.place(height=20,width=90,x=330,y=40)
        custLNentry = tk.Entry(custFrame, font=('arial', 12), bg=dbg, justify='left',
                        textvariable=self.custLN)
        custLNentry.place(height=25,width=130,x=420,y=40)

    def addCust(self):
        return None
if __name__ == "__main__":
    root = tk.Tk()
    dbg = 'white'
    #default value of the frame
    root.geometry("600x200+300+100")
    root.title("Online Ordering System")
    root.configure(background=dbg)
    app = PinkyNailOrder(root)
    root.mainloop()
