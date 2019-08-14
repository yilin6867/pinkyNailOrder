class CalOrdFrame:
    def __init__(self, parent, root):
        self.parent=parent
        self.calOrdFrame = tk.Frame(root, background=dbg)
        self.calOrdFrame.place(width=600,height=200, x=0,y=0)
        self.lblsService = []
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
        self.btnAdd = tk.Button(self.calOrdFrame, font=('arial', 12), text='Add',
                                command=lambda:self.storeService(self.name.get()))
        self.btnAdd.place(height=30, width=60, x = 450, y =80)
        
    def getService(self, column, where='WHERE 1 = 1'):
        mysqlDB = mysql.connector.connect(
            host='localhost',
            user='kjgmk',
            passwd='Mysql@yilin@6867',
            database='catolog'
        )
        mycursor = mysqlDB.cursor()
        stmt = 'SELECT DISTINCT `'+ column +'` FROM SERVICE ' + where
        print(stmt)
        mycursor.execute(stmt)
        table = mycursor.fetchall()
        myresult =[]
        for row in table:
            for col in row:
                myresult.append(col)
        print(myresult)
        mysqlDB.close()
        return myresult
    def updateSName(self, event, keyword):
        self.name['value']=self.getService('NAME', "WHERE TYPE = '" + keyword+"'")

    def storeService(self, serviceName):
        index = len(self.lblsService)
        yAxisAdd = index*20
        self.calOrdFrame.update()
        if (130+yAxisAdd >= self.calOrdFrame.winfo_width()):
            self.parent.configure(width=self.calOrdFrame.winfo_width()+50)
        lblService = tk.Label(self.calOrdFrame, font=('arial', 12), text=serviceName
                              , bg=dbg, justify='left')
        lblService.place(height= 20, width = 300, x = 135, y = 130+yAxisAdd)
        lblButton = tk.Button(self.calOrdFrame, font=('arial', 12), text='X'
                              , bg = dbg, bd = 0, command=lambda:self.removeService(index))
        lblButton.place(height=20, width=30, x=450, y=130+yAxisAdd)
        self.lblsService.append([lblService, lblButton])
    def removeService(self, index):
        self.lblsService[index][0].place_forget()
        self.lblsService[index][1].place_forget()
        del self.lblsService[index]
