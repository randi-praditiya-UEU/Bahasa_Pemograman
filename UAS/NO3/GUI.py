from tkinter import *

layar=Tk()
layar.title("APP GUI")
layar.geometry("700x200")

label01=Label(layar,font=("Tahoma",20,"bold"))
label01.configure(text="HALLO GUYS")

label02=Label(layar,font=("Tahoma",20,"italic"))
label02.configure(text="HALLO GUYS")

label03=Label(layar,font=("Tahoma",20,"underline"))
label03.configure(text="HALLO GUYS")

label01.pack(anchor=W)
label02.pack(anchor=W)
label03.pack(anchor=W)

layar.mainloop() 