from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry('200x300')
w.title('ShoppingZone')
w.config(bg='grey')
Label(text='item',font=('gothic',20)).grid(row=0,column=0)
item=Entry(font=('gothic',20))
item.grid(row=0,column=1)
Label(text='quantity',font=('gothic',20)).grid(row=1,column=0)
quantity=Entry(font=('gothic',20))
quantity.grid(row=1,column=1)
Label(text='price',font=('gothic',20)).grid(row=2,column=0)
price=Entry(font=('gothic',20))
price.grid(row=2,column=1)
def ShoppingZone():
    it=item.get()
    qty=quantity.get()
    f=open('shop.txt','r')
    for i in f:
        if (i.split(' ')[0]==it and i.split(' ')[1]<=qty):
            messagebox.showinfo('thankyou','this item is available')
            break
    else:
        messagebox.showinfo('sorry','this item is not available')
    f.close()
Button(text='ENTER',command=ShoppingZone).grid (row=3,column=0,columnspan=3)
w.mainloop()




