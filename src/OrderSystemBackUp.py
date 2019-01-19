from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import pypyodbc


#========================================import pinky nail order data============================#
def pullData(cur, tableName):
    cur.execute("SELECT COUNT (*) FROM " + tableName)
    rowCount = cur.fetchone()[0]
    cur.execute("SELECT * FROM " + tableName);
    nameArray = ["" for _ in range(rowCount + 1)]
    priceArray = ["0" for _ in range(rowCount + 1)]
    i = 1
    while True:
        row = cur.fetchone()
        if row is None:
            break
        nameArray[i] = row.get("Name")
        priceArray[i] = row.get("Price")
        i = i + 1
    return nameArray, priceArray

def buildConnection():
    pypyodbc.lowercase = False
    conn = pypyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
        r"Dbq=C:\Users\Admin\Documents\PinkyNailOrder.accdb;")
    cur = conn.cursor()
    manicurePedicure = pullData(cur, "ManicurePedicure")
    waxing = pullData(cur, "Waxing")
    ##print(manicurePedicure)
    ##print(waxing)
    cur.close()
    conn.close()
    return manicurePedicure, waxing

#=========================================build system ui=========================================#
def Exit():
    qExit = messagebox.askyesno("Pinky Ordering System", "Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return

def displayManiPediPrice(manicurePedicure, cmdManicurePedicure, LeftInsideLFLF):
    manicurePedicurePrice = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'),
                     text = "$%2d" % int(manicurePedicure[1][cmdManicurePedicure.current()]) , fg = "black", bd = 20)
    manicurePedicurePrice.grid(row = 1, column = 2)
    print(cmdManicurePedicure.current())

def displayWaxingPrice(waxing, cmdWaxing, LeftInsideLFLF):
    waxingPrice = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'),
                 text = "$%2d" % int(waxing[1][cmdWaxing.current()]), fg = "black", bd = 20)
    waxingPrice.grid(row = 2, column = 2)
    print(cmdWaxing.current())

def frame(root, manicurePedicure, waxing):        
    Tops = Frame(root, width = 1350, height = 50, bd = 16, relief = "raise")
    Tops.pack(side = TOP)
    LF = Frame(root, width = 700, height = 650, bd = 16, relief = "raise")
    LF.pack(side = LEFT)
    RF = Frame(root, width = 600, height = 650, bd = 16, relief ="raise")
    RF.pack(side = RIGHT)

    Tops.configure(background = 'black')
    LF.configure(background = 'black')
    RF.configure(background = 'black')

    LeftInsideLF = Frame(LF, width = 700, height = 100, bd = 8, relief = "raise")
    LeftInsideLF.pack(side = TOP)
    LeftInsideLFLF = Frame(LF, width = 700, height = 400, bd = 8, relief = "raise")
    LeftInsideLFLF.pack(side = LEFT)

    RightInsideLF = Frame(RF, width = 604, height = 200, bd = 8, relief = "raise")
    RightInsideLF.pack(side = TOP)
    RightInsideLFLF = Frame(RF, width = 306, height = 400, bd = 8, relief = "raise")
    RightInsideLFLF.pack(side = LEFT)
    RightInsideRFRF = Frame(RF, width = 300, height = 400, bd = 8, relief = "raise")
    RightInsideRFRF.pack(side = RIGHT)

    lblInfor = Label(Tops, font = ('arial', 50, 'bold'), text= "Pinky Ordering Systems",
                     justify = "center", bd = 10, anchor = 'w')
    lblInfor.grid(row = 0, column = 0)

    topLeftFrame(LeftInsideLF)
    bottomLeftFrame(LeftInsideLFLF, manicurePedicure, waxing)
    topRightFrame(RightInsideLF)
    bottomRightFrame(RightInsideLFLF, RightInsideRFRF)
#============================================Top Left Frame =============================#
def topLeftFrame(LeftInsideLF):
    lblWorkerName = Label(LeftInsideLF, font = ('arial', 14, 'bold'), text = "Worker Name",
                           fg = "black", bd = 10, anchor = "w")
    lblWorkerName.grid(row = 0, column = 0)
    txtWorkerName = Entry(LeftInsideLF, font = ('arial', 14, 'bold'), bd = 20, width = 43,
                           bg = "white", justify = 'left', textvariable = WorkerName)
    txtWorkerName.grid(row = 0, column = 1)
#============================================Bottom Left Frame =============================#
def bottomLeftFrame(LeftInsideLFLF, manicurePedicure, waxing):
    lblName = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'), text = "Name",
                           fg = "black", bd = 20)
    lblName.grid(row = 0, column = 1)
    lblPrice = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'), text = "Price",
                           fg = "black", bd = 20)
    lblPrice.grid(row = 0, column = 2)

    lblManicurePedicure = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'), text = "Mani&Pedi",
                           fg = "black", bd = 20)
    lblManicurePedicure.grid(row = 1, column = 0)
    cmdManicurePedicure = ttk.Combobox(LeftInsideLFLF, font = ('arial', 10, 'bold'), width = 43)
    cmdManicurePedicure['value'] = manicurePedicure[0]
    cmdManicurePedicure.grid(row = 1, column = 1)
    cmdManicurePedicure.bind("<<ComboboxSelected>>", displayManiPediPrice(manicurePedicure, cmdManicurePedicure, LeftInsideLFLF))

    lblWaxing = Label(LeftInsideLFLF, font = ('arial', 14, 'bold'), text = "Waxing",
                           fg = "black", bd = 20)
    lblWaxing.grid(row = 2, column = 0)
    cmdWaxing = ttk.Combobox(LeftInsideLFLF, font = ('arial', 10, 'bold'), width = 43)
    cmdWaxing['value'] = waxing[0]
    cmdWaxing.grid(row = 2, column = 1)
    cmdWaxing.bind("<<ComboboxSelected>>", displayWaxingPrice(waxing, cmdWaxing, LeftInsideLFLF))

#============================================Top Right Frame =============================#
def topRightFrame(RightInsideLF):
    lblDateOfOrder = Label(RightInsideLF, font = ('arial', 12, 'bold'), text = "Date of Order",
                           fg = "black", bd = 10, anchor = "w")
    lblDateOfOrder.grid(row = 0, column = 0)
    txtDateOfOrder = Entry(RightInsideLF, font = ('arial', 12, 'bold'), bd = 20, width = 43,
                           bg = "white", justify = 'left', textvariable = DateOfOrder)
    txtDateOfOrder.grid(row = 0, column = 1)

    lblTimeOfOrder = Label(RightInsideLF, font = ('arial', 12, 'bold'), text = "Time of Order",
                           fg = "black", bd = 10, anchor = "w")
    lblTimeOfOrder.grid(row = 1, column = 0)
    lblTimeOfOrder = Entry(RightInsideLF, font = ('arial', 12, 'bold'), bd = 20, width = 43,
                           bg = "white", justify = 'left', textvariable = TimeOfOrder)
    lblTimeOfOrder.grid(row = 1, column = 1)

    lblCustomerRef = Label(RightInsideLF, font = ('arial', 12, 'bold'), text = "Customer Ref",
                           fg = "black", bd = 10, anchor = "w")
    lblCustomerRef.grid(row = 2, column = 0)
    txtCustomerRef = Entry(RightInsideLF, font = ('arial', 12, 'bold'), bd = 20, width = 43,
                           bg = "white", justify = 'left', textvariable = CustomerRef )
    txtCustomerRef.grid(row = 2, column = 1)

#=============================================Right Frame ==========================#
def bottomRightFrame(RightInsideLFLF, RightInsideRFRF):
    lblMethodOfPayment = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Method of Payment",
                                fg = "black", bd = 16, anchor = 'w')
    lblMethodOfPayment.grid(row = 0, column = 0)
    cmdMethondOfPayment = ttk.Combobox(RightInsideLFLF, font = ('arial', 10, 'bold'))
    cmdMethondOfPayment['value'] = (' ', 'Cash', 'Debit Card', 'Visa Card', 'Master Card')
    cmdMethondOfPayment.grid(row = 0, column = 1)

    lblDiscount = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Discount",
                                fg = "black", bd = 16, anchor = 'w')
    lblDiscount.grid(row = 1, column = 0)
    lblDiscount = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 18,
                                bg = "white", justify = 'left', textvariable = Discount)
    lblDiscount.grid(row = 1, column = 1)

    lblTax = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Tax",
                                fg = "black", bd = 16, anchor = 'w')
    lblTax.grid(row = 2, column = 0)
    txtTax = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 18,
                                bg = "white", justify = 'left', textvariable = Tax)
    txtTax.grid(row = 2, column = 1)

    lblSubTotal = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Sub Total   ",
                                fg = "black", bd = 16, anchor = 'w')
    lblSubTotal.grid(row = 3, column = 0)
    txtSubTotal = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 18,
                                bg = "white", justify = 'left', textvariable = SubTotal)
    txtSubTotal.grid(row = 3, column = 1)

    lblTotalCost = Label(RightInsideLFLF, font = ('arial', 12, 'bold'), text = "Total Cost",
                         fg = "black", bd = 16, anchor = 'w')
    lblTotalCost.grid(row = 4, column = 0)
    lblTotalCost = Entry(RightInsideLFLF, font = ('arial', 12, 'bold'), bd = 16, width = 18,
                                bg = "white", justify = 'left', textvariable = TotalCost)
    lblTotalCost.grid(row = 4, column = 1)
    buttomRightFrame(RightInsideRFRF)


#=============================================Button Right Frame==============================================#
def buttomRightFrame(RightInsideRFRF):
    btnTotalCost = Button(RightInsideRFRF, pady = 8, bd = 8, fg = "black", font = ('arial', 16, 'bold'), width = 11,
                          text = "Total Cost", bg = "white").grid(row = 0, column = 0)
    btnReset = Button(RightInsideRFRF, pady = 8, bd = 8, fg = "black", font = ('arial', 16, 'bold'), width = 11,
                          text = "Reset", bg = "white").grid(row = 1, column = 0)
    btnOrderReference = Button(RightInsideRFRF, pady = 8, bd = 8, fg = "black", font = ('arial', 16, 'bold'), width = 11,
                          text = "Order Ref", bg = "white").grid(row = 2, column = 0)
    btnExit = Button(RightInsideRFRF, pady = 8, bd = 8, fg = "black", font = ('arial', 16, 'bold'), width = 11,
                          text = "Exit", bg = "white", command = Exit).grid(row = 3, column = 0)

def main():
    nailSalonOrder = buildConnection()
    frame(root, nailSalonOrder[0], nailSalonOrder[1])
    root.update()
    root.mainloop()


root = Tk()
root.geometry("1350x650+0+0")
root.title("Online Ordering System")
root.configure(background='black')
CustomerRef = StringVar()
Tax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Discount = StringVar()
DateOfOrder = StringVar()
TimeOfOrder = StringVar()
WorkerName = StringVar()
main()
