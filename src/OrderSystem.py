from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import gmtime, strftime
import os, sys
import random
import datetime
import pypyodbc
import traceback
from CreateToolTip import CreateToolTip

class Application():

    root = Tk()
    custFName = StringVar()
    custMI = StringVar()
    custLName = StringVar()
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
    storeLblOrder = []
    servicePrice = None
    

    #=========================================build system ui=========================================#

    Tops = Frame(root, width = 1350, height = 50, bd = 16, relief = "raise")
    LF = Frame(root, width = 700, height = 150, bd = 16, relief = "raise")
#    RF = Frame(root, width = 600, height = 650, bd = 16, relief ="raise")
    lblInfor = Label(Tops, font = ('arial', 50, 'bold'), text= "Pinky Ordering Systems",
                         justify = "center", bd = 10, anchor = 'w')
    InsideLF = Frame(LF, width = 700, height = 200, bd = 12, relief = "raise")
#    InsideRF = Frame(RF, width = 306, height = 400, bd = 8, relief = "raise")

#============================================Bottom Left Frame =============================#
        
    lblWorkerName = Label(InsideLF, font = ("arial", 14, "bold"), text = "Worker",
                            fg = "black", bd = 10, anchor = "w")
    lblPrice = Label(InsideLF, font = ("arial", 14, "bold"), text = "Price",
                       fg = "black", bd = 20)
    lblService = Label(InsideLF, font = ("arial", 14, "bold"), text = "Service",
                       fg = "black", bd = 20)
    lblPolish = Label(InsideLF, font = ("arial", 14, "bold"), text = "Polish Code",
                      fg = "black", bd = 20)
    lblCustFN = Label(InsideLF, font = ("arial", 14, "bold"), text = "Customer\nFirst Name",
                    fg = "black", bd = 20)
    lblCustMI = Label(InsideLF, font = ("arial", 14, "bold"), text = "Customer\nMI",
                fg = "black", bd = 20)
    lblCustLN = Label(InsideLF, font = ("arial", 14, "bold"), text = "Customer\nLast Name",
            fg = "black", bd = 20)
    
    cmdService = ttk.Combobox(InsideLF, font = ("arial", 10, "bold"), width = 30, justify = 'center')
    cmdWorkerName = ttk.Combobox(InsideLF, font = ("arial", 10, "bold"), width = 15, justify = 'center')
    cmdPolish = ttk.Combobox(InsideLF, font = ("arial", 10, "bold"), width = 5, justify = 'center')

    custFName.set("Anonymous")
    custMI.set("Anonymous")
    custLName.set("Anonymous")
    txtCustFN = Entry(InsideLF, font = ("arial", 12, "bold"), bd = 2, width = 20,
                    bg = "white", justify = "left", textvariable = custFName)
    txtCustMI = Entry(InsideLF, font = ("arial", 12, "bold"), bd = 2, width = 20,
                    bg = "white", justify = "left", textvariable = custMI)
    txtCustLN = Entry(InsideLF, font = ("arial", 12, "bold"), bd = 2, width = 20,
                    bg = "white", justify = "left", textvariable = custLName)
    #custNameTootTip = CreateToolTip(txtCustFN, "Enter First Name MI Last Name")

#=============================================Right Frame ==========================#
##    lblMethodOfPayment = Label(InsideRF, font = ('arial', 12, 'bold'), text = "Method of\n Payment",
##                                fg = "black", bd = 16, anchor = 'w')
##    cmdMethondOfPayment = ttk.Combobox(InsideRF, font = ('arial', 10, 'bold'), width =12)
##    lblDiscount = Label(InsideRF, font = ('arial', 12, 'bold'), text = "Discount",
##                                fg = "black", bd = 16, anchor = 'w')
##    txtDiscount = Entry(InsideRF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
##                                bg = "white", justify = 'left', textvariable = Discount)
##    lblTax = Label(InsideRF, font = ('arial', 12, 'bold'), text = "Tax",
##                                fg = "black", bd = 16, anchor = 'w')
##    txtTax = Entry(InsideRF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
##                                bg = "white", justify = 'left', textvariable = Tax)
##    lblSubTotal = Label(InsideRF, font = ('arial', 12, 'bold'), text = "Sub Total   ",
##                                fg = "black", bd = 16, anchor = 'w')
##    txtSubTotal = Entry(InsideRF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
##                                bg = "white", justify = 'left', textvariable = SubTotal)
##    lblTotalCost = Label(InsideRF, font = ('arial', 12, 'bold'), text = "Total Cost",
##                         fg = "black", bd = 16, anchor = 'w')
##    txtTotalCost = Entry(InsideRF, font = ('arial', 12, 'bold'), bd = 16, width = 6,
##                                bg = "white", justify = 'left', textvariable = TotalCost)

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
        cur.close()
        conn.close()
        return serviceList, workerList, polishCodeList
    #========================================= Button Command =======================================
    def Exit():
        qExit = messagebox.askyesno("Pinky Ordering System", "Do you want to exit the system")
        if qExit > 0:
            app.root.destroy()
            return

    def displayPrice(services, cmdServices, InsideLF):
        app.servicePrice = Label(InsideLF, font = ('arial', 14, 'bold'),
                         text = "$%2d" % int(services[cmdServices.current()][1]) , fg = "black", bd = 20)
        app.servicePrice.grid(row = 1, column = 6)

    def cancelService(storeLblService, lblList):
        for n in range(len(app.storeLblOrder)):   
            app.storeLblOrder[n][0].grid_remove()
            app.storeLblOrder[n][1].grid_remove()
            app.storeLblOrder[n][2].grid_remove()
            app.storeLblOrder[n][3].grid_remove()
            app.storeLblOrder[n][4].grid_remove()
            app.storeLblOrder[n][5].grid_remove()
            app.storeLblOrder[n][6].grid_remove()
        for n in range(len(app.serviceCancelBtn)):
            app.serviceCancelBtn[n].grid_remove()
        row = app.storeLblService.index(lblList)
        del app.storeLblService[row]
        del app.storeLblOrder[row]
        del app.serviceCancelBtn[row]
        for n in range(len(app.storeLblOrder)):
            app.storeLblOrder[n][0].grid(row = n + 2, pady=0, ipady=0, column = 0)
            app.storeLblOrder[n][1].grid(row = n + 2, pady=0, ipady=0, column = 1)
            app.storeLblOrder[n][2].grid(row = n + 2, pady=0, ipady=0, column = 2)
            app.storeLblOrder[n][3].grid(row = n + 2, pady=0, ipady=0, column = 3)
            app.storeLblOrder[n][4].grid(row = n + 2, pady=0, ipady=0, column = 4)
            app.storeLblOrder[n][5].grid(row = n + 2, pady=0, ipady=0, column = 5)
            app.storeLblOrder[n][6].grid(row = n + 2, pady=0, ipady=0, column = 6)
        for n in range(len(app.serviceCancelBtn)):
            app.serviceCancelBtn[n].grid(row = n + 2, pady=0, ipady=0, column = 7)
            
##    def calTotalCost():
##        app.totalCost = 0
##        for i in app.storeLblService:
##            print(i)    
##            app.totalCost = app.totalCost + int(i[6][1:])
##        app.txtSubTotal.delete(0, END)
##        app.txtSubTotal.insert(0, format(app.totalCost, '.2f'))
##        app.SubTotal = app.totalCost
##        app.Discount = app.txtDiscount.get()
##        app.Tax = app.totalCost * .05
##        app.txtTax.delete(0, END)
##        app.txtTax.insert(0, format(app.Tax, '.2f'))
##        app.totalCost = float(app.totalCost) + float(app.Tax) - float(app.Discount)
##        app.txtTotalCost.delete(0, END)
##        if (app.totalCost < 0):
##            app.totalCost = 0
##        app.txtTotalCost.insert(0, format(app.totalCost, '.2f'))

    def reset():
        for n in range(len(app.storeLblOrder)):
            app.storeLblOrder[n][0].grid_remove()
            app.storeLblOrder[n][1].grid_remove()
            app.storeLblOrder[n][2].grid_remove()
            app.storeLblOrder[n][3].grid_remove()
            app.storeLblOrder[n][4].grid_remove()
            app.storeLblOrder[n][5].grid_remove()
        for n in range(len(app.serviceCancelBtn)):
            app.serviceCancelBtn[n].grid_remove()
        del app.storeLblOrder[:]
        del app.storeLblService[:]
        app.servicePrice.grid_remove()
        app.txtSubTotal.delete(0, END)
        app.txtTax.delete(0, END)
        app.txtTotalCost.delete(0, END)
        app.txtDiscount.delete(0, END)
        app.cmdWorkerName.set("")
        app.cmdService.set("")
        app.cmdMethondOfPayment.set("")
        app.cmdPolish.set("")
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
                cur.execute("SELECT ID FROM SERVICE WHERE NAME = '"+service[3] +"'")
                serviceId = cur.fetchone()

                empName = service[4].split()
                if (len(empName) == 2):
                    empName.insert(1, " ")
                cur.execute("SELECT EMP_ID FROM EMPLOYEE WHERE F_NAME = '"+ empName[0] +"' AND MI = '" + empName[1] + "' AND L_NAME = '" + empName[2] + "'")
                workerId = cur.fetchone()
                now = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                
                cur.execute("SELECT CUST_ID FROM CUSTOMER WHERE F_NAME = '" + service[0]+ "' AND MI = '" + service[1] + "' AND L_NAME = '" + service[2] + "'")
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
                sql = "INSERT INTO `ORDER`(ORDER_ID,SERVICE_ID,CUST_ID, EMP_ID, APPO_ID, TRANS_ID, PRICE, ORDER_DATE) VALUES(?,?,?,?,?,?,?,?)"
                print([orderID, serviceId, returnCust, workerId, 'Null', transId, service[6], now])
                cur.execute(sql, [orderID, serviceId, returnCust, workerId, 'Null', transId, service[6], now])
                                  #str(app.cmdMethondOfPayment.get()), app.Discount, app.Tax, app.SubTotal, app.totalCost])
                conn.commit()
        except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(err)
        finally:
            cur.close()
            conn.close()
                
#================================================ Grid Frame function =============================================
    def frame(root, data):
        app.Tops.pack(side = TOP)
        app.LF.pack(side = TOP)
#        app.RF.pack(side = RIGHT)
        app.Tops.configure(background = 'black')
        app.LF.configure(background = 'black')
#        app.RF.configure(background = 'black')
        
#        app.InsideRF.pack(side = RIGHT)
#        app.InsideRF.pack(side = TOP)
        app.InsideLF.pack(side = TOP)

        app.lblInfor.grid(row = 0, column = 0)

#        app.bottomRightFrame(app.InsideRF)
        app.lftFrame(app.InsideLF, data)

    def lftFrame(InsideLF, data):
        serviceName = []
        for service in data[0]:
            serviceName.append(service[0])

        app.lblCustFN.grid(row = 0, column = 0)
        app.lblCustMI.grid(row = 0, column = 1)
        app.lblCustLN.grid(row = 0, column = 2)
        app.lblService.grid(row = 0, column = 3)
        app.lblWorkerName.grid(row = 0, column = 4)
        app.lblPolish.grid(row = 0, column = 5)
        app.lblPrice.grid(row = 0, column = 6)

        

        app.txtCustFN.grid(row = 1, column = 0)
        app.txtCustMI.grid(row = 1, column = 1)
        app.txtCustLN.grid(row = 1, column = 2)        
        app.cmdService.grid(row = 1, column = 3)
        app.cmdService.bind('<<ComboboxSelected>>', lambda event: app.displayPrice(data[0], app.cmdService, InsideLF))        
        app.cmdService['value'] = serviceName
        app.cmdWorkerName.grid(row = 1, column = 4)
        app.cmdWorkerName['value'] = data[1]
        app.cmdPolish.grid(row= 1, column = 5)
        app.cmdPolish['value'] = data[2]

        btnSubmit = Button(InsideLF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
            text = "Submit", bg = "white", command = app.submit).grid(row = 0, column = 7)
        btnAdd = Button(InsideLF, pady = 0, bd = 8, fg = "black", font = ('arial', 14, 'bold'), width = 5,
            text = "Add", bg = "white", command = lambda :
                   app.addService(InsideLF, data[0])).grid(row = 1, column = 7)

#============================================Button LeftFrame Function ============================#
    def addService(InsideLF, services):
        if (app.cmdWorkerName.get() != '' and app.cmdService.get() != ''):
            if (len(app.storeLblService) + 2 < 12):
                lblCustFNAdd = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                 text = app.txtCustFN.get() , fg = "black", bd = 5, anchor=W, justify=LEFT)
                lblCustFNAdd.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 0)
                lblCustMIAdd = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                 text = app.txtCustMI.get() , fg = "black", bd = 5, anchor=W, justify=LEFT)
                lblCustMIAdd.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 1)
                lblCustLNadd = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                 text = app.txtCustLN.get() , fg = "black", bd = 5, anchor=W, justify=LEFT)
                lblCustLNadd.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 2)
                lblServiceAdd = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                         text = app.cmdService.get(), fg = "black", bd = 0, anchor = "w")
                lblServiceAdd.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 3)
                lblWrkAssign = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                 text = app.cmdWorkerName.get(), fg = "black", bd = 0, anchor = "w")
                lblWrkAssign.grid(row = len(app.storeLblService) + 2, pady = 0, ipady=0, column = 4)
                lblPolishUse = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                 text = app.cmdPolish.get() , fg = "black", bd = 5)
                lblPolishUse.grid(row = len(app.storeLblService) + 2, pady = 0, ipady=0, column =5)
                lblPriceAdd = Label(InsideLF, highlightthickness=0, borderwidth=0, pady=0, font = ('arial', 12, 'bold'),
                                 text = "$%2d" % int(services[app.cmdService.current()][1]  ) , fg = "black", bd = 5)
                lblPriceAdd.grid(row = len(app.storeLblService) + 2, pady=0, ipady=0, column = 6)
                cancelButton = Button(InsideLF, pady = 0, padx = 0, bd = 0, fg = "black", font = ('arial', 8, 'bold'), width = 0,
                       text = "X", bg = "white", command = lambda :
                       app.cancelService(app.storeLblService, [
                                           lblServiceAdd['text'], lblCustFNAdd['text'], lblCustMIAdd['text'], lblCustLNadd['text'], lblWrkAssign['text']
                                            , lblPolishUse['text'], lblPriceAdd['text']
                                        ]))
                cancelButton.grid(row = len(app.storeLblService) + 2, column = 7)
                app.storeLblOrder.append([lblCustFNAdd, lblCustMIAdd, lblCustLNadd, lblServiceAdd, lblWrkAssign, lblPolishUse, lblPriceAdd])

                app.storeLblService.append([
                    lblServiceAdd['text'], lblCustFNAdd['text'], lblCustMIAdd['text'], lblCustLNadd['text'], lblWrkAssign['text'], lblPolishUse['text']
                    , lblPriceAdd['text']
                    ])
                app.serviceCancelBtn.append(cancelButton)
            else:
                messagebox.showinfo('Error', 'Maxiumum Order per transaction have been exceed')
        else:
            messagebox.showinfo("Warning", "Worker and Service can not be blank")

#=============================================Button Right Frame==============================================#
##    def bottomRightFrame(InsideRF):
##        app.lblMethodOfPayment.grid(row = 0, column = 0)
##        app.cmdMethondOfPayment['value'] = (' ', 'Cash', 'Debit Card', 'Visa Card', 'Master Card')
##        app.cmdMethondOfPayment.grid(row = 0, column = 1)
##        app.lblDiscount.grid(row = 1, column = 0)
##        app.txtDiscount.grid(row = 1, column = 1)
##        app.lblTax.grid(row = 2, column = 0)
##        app.txtTax.grid(row = 2, column = 1)
##        app.lblSubTotal.grid(row = 3, column = 0)
##        app.txtSubTotal.grid(row = 3, column = 1)
##        app.lblTotalCost.grid(row = 4, column = 0)
##        app.txtTotalCost.grid(row = 4, column = 1)
##        btnReset = Button(InsideRF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
##                              text = "Reset", bg = "white", command = app.reset).grid(row = 2, column = 2)
##        btnSubmit = Button(InsideRF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
##                              text = "Submit", bg = "white", command = app.submit).grid(row = 3, column = 2)
##        btnExit = Button(InsideRF, pady = 8, bd = 8, fg = "black", font = ('arial', 12, 'bold'), width = 6,
##                              text = "Exit", bg = "white", command = app.Exit).grid(row = 4, column = 2)
#add an appointment function that process in the back end using cust id
    def main():
        data = app.buildConnection()
        Application.frame(Application.root, data)
        Application.root.update()
        Application.root.mainloop()

app = Application
app.main()
