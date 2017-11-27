from tkinter import *
from tkinter.messagebox import *
import sys
sys.path.append("..")
from PMF import user_query
from dataStructure import BusinessQuery
from dataStructure import Converter


def getrecommend():
    User_id = var.get()
    if User_id == "":
        
        showinfo(title='Remainder', message='Please input User ID!')
        print("test only")
    City = var2.get()
    if City == "":
        showinfo(title='Remainder', message='Please input location!')

    if User_id != "" and City != "":
        
        business_query=BusinessQuery.BusinessQuery()
        iid_list=business_query.getBusinessIdByCity(City)
        converter=Converter.Converter()
        User_id=converter.getUserInt(User_id)
        item_list=converter.getBusinessIntByCity(City)
        
        if(item_list==None):
            showinfo(title='Remainder', message='Please input valid location!')
        else: 
            top_five=user_query.sort_by_rating(User_id,item_list)[0:5]
            #print(top_five)
            rating=['%.2f'%top_five[i][1] for i in range(0,5)]
            #print(rating)
            recommend=[converter.getBusinessStr(i[0]) for i in top_five]
            recommend=[business_query.getBusinessById(i.strip('\n'))[0] for i in recommend]
            ShowWindow(recommend,rating,City)
        

def ShowWindow(recommend,rating,city):
    top1 = Toplevel()
    top1.geometry('360x360')
    top1.title("Recommendation Results")
    root.resizable(width=False, height=True)
    test = Label(top1, text='Recommended Restaurant in '+city+' :', font=('Arial', 15),width=50).pack()
    ttitle = Label (top1,text ='Restaurant\tRating', font=('Arial', 12),width=50).pack()
    for i in range(0,5):
        tt = Label (top1,text =recommend[i]+'\t'+rating[i], font=('Arial', 10),width=50).pack()
    Button(top1,text="Close Window",width = 20,command = top1.quit).pack(side=TOP, expand=NO, fill =Y)
    top1.mainloop()
    top1.destroy()
    
if __name__ == "__main__":
    
    root = Tk()
    root.title("PMF Recommendation System")
    root.geometry('480x360')
    root.resizable(width=False, height=True)
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
    e = Entry(frm_R,textvariable = var,width=25)
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
    e2 = Entry(frm_R2,textvariable = var2,width=25)
    e2.pack()
    frm_R2.pack(side=RIGHT,expand=YES)
    frm2.pack()

    Label(root, text='   ', font=('Arial', 15)).pack()

    Button(root,text="Recommend",width = 20,command = getrecommend).pack(side=TOP, expand = NO,fill=Y)
    Button(root,text="Quit",width = 20,command = frm.quit).pack(side=TOP, expand=NO, fill =Y)

    root.mainloop()
    root.destroy()




