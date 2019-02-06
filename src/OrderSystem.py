from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import gmtime, strftime
import random
import datetime
import pypyodbc
import traceback

class Application():

    root = Tk()
    custName = StringVar()
    Tax = DoubleVar()
    SubTotal = DoubleVar()
    TotalCost = DoubleVar()
    Discount = DoubleVar()
    DateOfOrder = StringVar()
    TimeOfOrder = StringVar()
    WorkerName = StringVar()
    root.geometry("1350x650+0+0")
    root.title("Online Ordering System")
    root.configure(background='black')
    storeLblService = []
    serviceCancelBtn = []
    storeOrder = []
    servicePrice = None
    

    #=========================================build system ui=========================================#

    Tops = Frame(root, width = 1350, height = 50, bd = 16, relief = "raise")
    LF = Frame(root, width = 700, height = 650, bd = 16, relief = "raise")
    RF = Frame(root, width = 600, height = 650, bd = 16, relief ="raise")
    lblInfor = Label(Tops, font = ('arial', 50, 'bold'), text= "Pinky Ordering Systems",
                         justify = "center", bd = 10, anchor = 'w')
##    LeftInsideLF = Frame(LF, width = 700, height = 100, bd = 8, relief = "raise")
    LeftInsideLFLF = Frame(LF, width = 700, height = 400, bd = 12, relief = "raise")
    ##        RightInsideLF = Frame(RF, width = 604, height = 200, bd = 8, relief = "raise")
    ##        RightInsideLF.pack(side = TOP)
    RightInsideLFLF = Frame(RF, width = 306, height = 400, bd = 8, relief = "raise")
    #RightInsideRFRF = Frame(RF, width = 300, height = 400, bd = 8, relief = "raise")

#============================================Bottom Left Frame =============================#
        
    lblWorkerName = Label(LeftInsideLFLF, font = ("arial", 14, "bold"), text = "Worker Name",
                            fg = "black", bd = 10, anchor = "w")
    lblPrice = Label(LeftInsideLFLF, font = ("arial", 14, "bold"), text = "Price",
                       fg = "black", bd = 20)
    lblService = Label(LeftInsideLFLF, font = ("arial", 14, "bold"), text = "Service",
                       fg = "black", bd = 20)
    lblPolish = Label(LeftInsideLFLF, font = ("arial", 14, "bold"), text = "Polish Code",
                      fg = "black", bd = 20)
    lblCust = Label(LeftInsideLFLF, font = ("arial", 14, "bold"), text = "Customer Name",
                    fg = "black", bd = 20)
    cmdService = ttk.Combobox(LeftInsideLFLF, font = ("arial", 10, "bold"), width = 32)
    cmdWorkerName = ttk.Combobox(LeftInsideLFLF, font = ("arial", 10, "bold"), width = 20)
    cmdPolish = ttk.Combobox(LeftInsideLFLF, font = ("arial", 10, "bold"), width = 20)

    txtCust = Entry(LeftInsideLFLF, font = ("arial", 12, "bold"), bd = 2, width = 20,
                    bg = "white", justify = "left", textvariable = custName)

#=============================================Right Frame ==========================#
    lblMethodOfPayment = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Method of\n Payment",
                                fg = "black", bd = 16, anchor = 'w')
    cmdMethondOfPayment = ttk.Combobox(RightInsideLFLF, font = ('arial', 10, 'bold'), width =12)
    lblDiscount = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Discount",
                                fg = "black", bd = 16, anchor = 'w')
    txtDiscount = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
                                bg = "white", justify = 'left', textvariable = Discount)
    lblTax = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Tax",
                                fg = "black", bd = 16, anchor = 'w')
    txtTax = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
                                bg = "white", justify = 'left', textvariable = Tax)
    lblSubTotal = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Sub Total   ",
                                fg = "black", bd = 16, anchor = 'w')
    txtSubTotal = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
                                bg = "white", justify = 'left', textvariable = SubTotal)
    lblTotalCost = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Total Cost",
                         fg = "black", bd = 16, anchor = 'w')
    txtTotalCost = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
                                bg = "white", justify = 'left', textvariable = TotalCost)

#========================================import pinky nail data============================#
    def pullData(cur, tableName):
        cur.execute("SELECT * FROM " + tableName);
        rawData = cur.fetchall()
        return rawData

    def buildConnection():
        pypyodbc.lowercase = False
        conn = pypyodbc.connect(
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
            r"Dbq=C:\Users\Admin\Documents\PinkyNailProgram\PinkyNailOrder.accdb;")
        cur = conn.cursor()
        serviceList = []
        workerList = []
        polishCodeList = []
        serviceData = app.pullData(cur, "SERVICE")
        workerData = app.pullData(cur, "EMPLOYEE")
        polishData = app.pullData(cur, "NAIL_POLISH")
        for row in range(len(serviceData)):
            serviceList.append([serviceData[row][1],serviceData[row][3]])
        for row in range(len(workerData)):
            if (workerData[row][2] == None):
                workerList.append(workerData[row][1] +" " + workerData[row][3])
            else:
                workerList.append(workerData[row][1] +" " + workerData[row][2] + " " + workerData[row][3])
        for row in range(len(polishData)):
            polishCodeList.append(polishData[row][0])
        print(polishCodeList)
        cur.close()
        conn.close()
        return serviceList, workerList, polishCodeList
    #========================================= Button Command =======================================
    def Exit():
        qExit = messagebox.askyesno("Pinky Ordering System", "Do you want to exit the system")
        if qExit > 0:
            app.root.destroy()
            return

    def displayPrice(services, cmdServices, LeftInsideLFLF):
        app.servicePrice = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'),
                         text = "$%2d" % int(services[cmdServices.current()][1]) , fg = "black", bd = 20)
        app.servicePrice.grid(row = 1, column = 3)

    def cancelService(storeLblService, labelName, labelPrice, labelWorker, cancelButton):
        print(app.storeOrder)
        row = storeLblService.index([labelName['text'], labelWorker['text'], labelPrice['text']])
        labelName.destroy()
        labelPrice.destroy()
        cancelButton.destroy()
        app.serviceCancelBtn.remove(cancelButton)
        app.storeOrder.remove([labelName, labelWorker, labelPrice])
        app.storeLblService.pop(row)
        for n in range(len(app.storeOrder)):
            app.storeOrder[n][0].grid_remove()
            app.storeOrder[n][1].grid_remove()
            app.storeOrder[n][2].grid_remove()
            app.storeOrder[n][3].grid_remove()
            app.storeOrder[n][4].grid_remove()
            app.storeOrder[n][5].grid_remove()
            app.storeOrder[n][0].grid(row = n + 2, pady=0, ipady=0, column = 0)
            app.storeOrder[n][1].grid(row = n + 2, pady=0, ipady=0, column = 1)
            app.storeOrder[n][2].grid(row = n + 2, pady=0, ipady=0, column = 2)
            app.storeOrder[n][0].grid(row = n + 2, pady=0, ipady=0, column = 3)
            app.storeOrder[n][1].grid(row = n + 2, pady=0, ipady=0, column = 4)
            app.storeOrder[n][2].grid(row = n + 2, pady=0, ipady=0, column = 5)
        for n in range(len(app.serviceCancelBtn)):
            app.serviceCancelBtn[n].grid_remove()
            app.serviceCancelBtn[n].grid(row = n + 2, pady=0, ipady=0, column = 0)
            
    def totalCost():
        app.totalCost = 0
        for i in app.storeLblService:
            print(i)
            app.totalCost = app.totalCost + int(i[2][1:])
        app.txtSubTotal.delete(0, END)
        app.txtSubTotal.insert(0, format(app.totalCost, '.2f'))
        app.SubTotal = app.totalCost
        app.Discount = app.txtDiscount.get()
        app.Tax = app.totalCost * .05
        app.txtTax.delete(0, END)
        app.txtTax.insert(0, format(app.Tax, '.2f'))
        app.totalCost = float(app.totalCost) + float(app.Tax) - float(app.Discount)
        app.txtTotalCost.delete(0, END)
        if (app.totalCost < 0):
            app.totalCost = 0
        app.txtTotalCost.insert(0, format(app.totalCost, '.2f'))

    def reset():
        for n in range(len(app.storeOrder)):
            app.storeOrder[n][0].grid_remove()
            app.storeOrder[n][1].grid_remove()
            app.storeOrder[n][2].grid_remove()
            app.storeOrder[n][3].grid_remove()
            app.storeOrder[n][4].grid_remove()
            app.storeOrder[n][5].grid_remove()
        for n in range(len(app.serviceCancelBtn)):
            app.serviceCancelBtn[n].grid_remove()
        del app.storeOrder[:]
        del app.storeLblService[:]
        app.servicePrice.grid_remove()
        app.txtSubTotal.delete(0, END)
        app.txtTax.delete(0, END)
        app.txtTotalCost.delete(0, END)
        app.txtDiscount.delete(0, END)
        app.cmdWorkerName.set("")
        app.cmdService.set("")
        app.cmdMethondOfPayment.set("")
        app.servicePrice.grid_remove()
          
    def submit():
        try:
            pypyodbc.lowercase = False
            conn = pypyodbc.connect(
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
                r"Dbq=C:\Users\Admin\Documents\PinkyNailProgram\PinkyNailOrder.accdb;")
            cur = conn.cursor()
            for service in app.storeLblService:
                cur.execute("SELECT ORDER_ID FROM `ORDER` ORDER BY ORDER_ID DESC")
                currentOrderID = cur.fetchone()
                if currentOrderID == None:
                    orderID = 0 + 1
                else:
                    orderID = int(currentOrderID[0]) + 1
                cur.execute("SELECT ID FROM SERVICE WHERE NAME = '"+service.get()+"'")
                serviceId = cur.fetchone()
                
                cur.execute("SELECT EMP_ID FROM EMPLOYEE WHERE = '"++"'")
                workerId = cur.fetchone()
                now = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                app.custName = app.txtCust.get().split()
                cur.execute("SELECT CUST_ID FROM CUSTOMER WHERE F_NAME = '" + app.custName[0]+ "' AND MI = '" + app.custName[1] + "' AND L_NAME = '" +
                                         app.custName[2] + "'")
                returnCust = cur.fetchone()
                if returnCust == None:
                    cur.execute("SELECT CUST_ID FROM CUSTOMER ORDER BY CUST_ID DESC")
                    returnCust = int(cur.fetchone()[0]) + 1
                cur.execute("SELECT TRANS_ID FROM TRANSACTIONS ORDER BY TRANS_ID DESC")
                currentTransId = cur.fetchone()
                if currentTransId == None:
                    transId = 0 + 1
                else:
                    transId = int(currentTransId[0]) + 1
                print(app.totalCost)
                print([orderID, now, str(app.WorkerName),str(app.storeLblService), str(app.storeLblWaxing),
                                  str(app.cmdMethondOfPayment.get()), str(app.Discount), str(app.Tax), str(app.SubTotal), app.totalCost])
                sql = "INSERT INTO `ORDER`(ORDER_ID,SERVICE_ID,CUST_ID, EMP_ID, APPO_ID, TRANS_ID, PRICE, ORDER_DATE) VALUES(?,?,?,?,?,?,?,?)"
                cur.execute(sql, [orderID, serviceId, returnCust, workerId, 'Null', transId, app.SubTotal, now])
                                  #str(app.cmdMethondOfPayment.get()), app.Discount, app.Tax, app.SubTotal, app.totalCost])
                conn.commit()
        except Exception as err:
            print(err)
        finally:
            cur.close()
            conn.close()
                
#================================================ Grid Frame function =============================================
    def frame(root, data):
        app.Tops.pack(side = TOP)
        app.LF.pack(side = LEFT)
        app.RF.pack(side = RIGHT)
        app.Tops.configure(background = 'black')
        app.LF.configure(background = 'black')
        app.RF.configure(background = 'black')
        
#        app.RightInsideRFRF.pack(side = RIGHT)
        app.RightInsideLFLF.pack(side = LEFT)
        app.LeftInsideLFLF.pack(side = LEFT)

        app.lblInfor.grid(row = 0, column = 0)

        app.bottomRightFrame(app.RightInsideLFLF)
        app.lftFrame(app.LeftInsideLFLF, data)

    def lftFrame(LeftInsideLFLF, data):
        serviceName = []
        for service in data[0]:
            serviceName.append(service[0])
        app.lblWorkerName.grid(row = 0, column = 2)
        app.lblPrice.grid(row = 0, column = 3)
        app.lblService.grid(row = 0, column = 0)
        app.lblPolish.grid(row = 0, column = 4)
        app.lblCust.grid(row = 0, column = 1)
        
        app.cmdWorkerName.grid(row = 1, column = 2)
        app.cmdWorkerName['value'] = data[1]
        app.cmdService.grid(row = 1, column = 0)
        app.cmdService.bind('<<ComboboxSelected>>', lambda event: app.displayPrice(data[0], app.cmdService, LeftInsideLFLF))        
        app.cmdService['value'] = serviceName
        app.cmdPolish.grid(row= 1, column = 4)
        app.cmdPolish['value'] = data[2]
        app.txtCust.grid(row = 1, column = 1)
        
        addBtn = Button(LeftInsideLFLF, pady = 0, bd = 8, fg = "black", font = ('arial', 14, 'bold'), width = 5,
                   text = "Add", bg = "white", command = lambda :
                           app.addService(LeftInsideLFLF, data[0])).grid(row = 1, column = 5)

#============================================Button LeftFrame Function ============================#
    def addService(LeftInsideLFLF, services):
        if (app.cmdWorkerName.get() != '' and app.cmdService.get() != ''):
            lblStoreService = Label(LeftInsideLFLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                     text = app.cmdService.get(), fg = "black", bd = 0, anchor = "w")
            lblStoreService.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 0)
            lblWrkAssign = Label(LeftInsideLFLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                             text = app.cmdWorkerName.get(), fg = "black", bd = 0, anchor = "w")
            lblWrkAssign.grid(row = len(app.storeLblService) + 2, pady = 0, ipady=0, column = 2)
            lblStoreCust = Label(LeftInsideLFLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                             text = app.txtCust.get() , fg = "black", bd = 5)
            lblStoreCust.grid(row = len(app.storeLblService)+2, pady = 0, ipady=0, column = 1)
            lblStorePrice = Label(LeftInsideLFLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                             text = "$%2d" % int(services[app.cmdService.current()][1]  ) , fg = "black", bd = 5)
            lblStorePrice.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 3)
            lblStorePolish = Label(LeftInsideLFLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                             text = app.cmdPolish.get() , fg = "black", bd = 5)
            lblStorePolish.grid(row = len(app.storeLblService) + 2, pady = 0, ipady=0, column =4)
            cancelButton = Button(LeftInsideLFLF, pady = 0, padx = 0, bd = 0, fg = "black", font = ('arial', 8, 'bold'), width = 0,
                   text = "X", bg = "white", command = lambda :
                   app.cancelService(app.storeLblService, lblStoreService, lblStorePrice, lblWrkAssign,
                                      app.serviceCancelBtn[app.serviceCancelBtn.index(cancelButton)]))
            cancelButton.grid(row = len(app.storeLblService) + 2, column = 5)
            app.storeOrder.append([lblStoreService, lblStoreCust, lblWrkAssign, lblStorePrice, lblStorePolish, cancelButton])
            print(app.storeOrder)

            app.storeLblService.append([lblStoreService['text'], lblWrkAssign['text'], lblStorePrice['text']])
            app.serviceCancelBtn.append(cancelButton)
        else:
            messagebox.showinfo("Warning", "Worker and Service can not be blank")

#=============================================Button Right Frame==============================================#
    def bottomRightFrame(RightInsideLFLF):
        app.lblMethodOfPayment.grid(row = 0, column = 0)
        app.cmdMethondOfPayment['value'] = (' ', 'Cash', 'Debit Card', 'Visa Card', 'Master Card')
        app.cmdMethondOfPayment.grid(row = 0, column = 1)
        app.lblDiscount.grid(row = 1, column = 0)
        app.txtDiscount.grid(row = 1, column = 1)
        app.lblTax.grid(row = 2, column = 0)
        app.txtTax.grid(row = 2, column = 1)
        app.lblSubTotal.grid(row = 3, column = 0)
        app.txtSubTotal.grid(row = 3, column = 1)
        app.lblTotalCost.grid(row = 4, column = 0)
        app.txtTotalCost.grid(row = 4, column = 1)
        btnTotalCost = Button(RightInsideLFLF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
                              text = "Total \nCost", bg = "white", command = app.totalCost).grid(row = 1, column = 2)
        btnReset = Button(RightInsideLFLF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
                              text = "Reset", bg = "white", command = app.reset).grid(row = 2, column = 2)
        btnSubmit = Button(RightInsideLFLF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
                              text = "Submit", bg = "white", command = app.submit).grid(row = 3, column = 2)
        btnExit = Button(RightInsideLFLF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
                              text = "Exit", bg = "white", command = app.Exit).grid(row = 4, column = 2)
#add an appointment function that process in the back end using cust id
    def main():
        data = app.buildConnection()
        Application.frame(Application.root, data)
        Application.root.update()
        Application.root.mainloop()

app = Application
app.main()
