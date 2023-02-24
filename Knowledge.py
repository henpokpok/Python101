from tkinter import *
from tkinter import ttk #เข้าปาร์ตี้ที่มีแต่ตีน
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

def Button2() :
    text = 'มีเงินในบัญชีอยู่ 300 บัท'
    messagebox.showinfo('เงินในบัญชี', text)


FB1 = LabelFrame(GUI, text = "Little Moe")
FB1.place(x=200, y=200)
B2 = ttk.Button(FB1, text = 'มีตังกี่บัทจ๋า', command = Button2)
B2.pack(ipadx=20, ipady=20)

GUI.mainloop()
