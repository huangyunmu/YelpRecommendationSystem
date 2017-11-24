from tkinter import *
import sys
sys.path.append("..")
from PMF import user_query
from dataStructure import BusinessQuery
from dataStructure import Converter
root = Tk()
root.title("PMF Recommendation System")
root.geometry('480x360')
root.resizable(width=False, height=True)

def getrecommend():
    User_id = var.get()
    if User_id == "":
        
        messagebox.showinfo(title='Remainder', message='Please input User ID!')
        print("test only")
    City = var2.get()
    if City == "":
        messagebox.showinfo(title='Remainder', message='Please input Location!')

    if User_id != "" and City != "":
        
        business_query=BusinessQuery.BusinessQuery()
        iid_list=business_query.getBusinessIdByCity(City)
        converter=Converter.Converter()
        User_id=converter.getUserInt(User_id)
        #item_list=[converter.getBusinessInt(iid) for iid in iid_list]
        print(len(iid_list))
        #recommend=sort_by_rating(User_id,item_list)
        recommend=user_query.sort_by_rating(0,range(0,100))
        print(recommend[:5])
        ShowWindow(recommend[:5])
        

def ShowWindow(recommend):
    top1 = Toplevel()
    top1.geometry('360x360')
    top1.title("Recommendation Results")
    root.resizable(width=False, height=True)
    test = Label(top1, text='List:', font=('Arial', 15),width=10).pack()
    ##
    
    ##
    Button(top1,text="Close Window",width = 20,command = top1.quit).pack(side=TOP, expand=NO, fill =Y)
    top1.mainloop()
    top1.destroy()
    
Label(root, text='Welcome!', font=('Arial', 20)).pack()

# USER ID
frm = Frame(root)
#Left
frm_L = Frame(frm)
Label(frm_L, text='User ID:', font=('Arial', 15),width=10).pack()
frm_L.pack(side=LEFT)
#Right
frm_R = Frame(frm)
var = StringVar()
e = Entry(frm_R,textvariable = var)
e.pack()
frm_R.pack(side=RIGHT,expand=YES)
frm.pack()

#CITY INPUT
frm2 = Frame(root)
#Left
frm_L2 = Frame(frm2)
Label(frm_L2, text='City:', font=('Arial', 15),width=10).pack()
frm_L2.pack(side=LEFT)
#Right
frm_R2 = Frame(frm2)
var2 = StringVar()
e2 = Entry(frm_R2,textvariable = var2)
e2.pack()
frm_R2.pack(side=RIGHT,expand=YES)
frm2.pack()

Label(root, text='   ', font=('Arial', 15)).pack()

Button(root,text="Recommend",width = 20,command = getrecommend).pack(side=TOP, expand = NO,fill=Y)
Button(root,text="Quit",width = 20,command = frm.quit).pack(side=TOP, expand=NO, fill =Y)

root.mainloop()
root.destroy()




