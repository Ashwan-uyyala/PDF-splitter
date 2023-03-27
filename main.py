from tkinter import *
from PyPDF2 import *
from tkinter.filedialog import *
import os.path as os_path
# creating a tkinter ui interface
fd = " "
r = Tk()
r.title("pdf splitter")
# setting window size
r.geometry("800x600")
r.config(background="#26000a")
#functhins of the splitter

# brows function

def browse():
    global fd
    fd=askopenfilename(title="open pdf")
    e1.insert(0,fd)
    try:
        with open(fd, "rb") as file:
            os_path=PdfReader(file)
            totalpages=len(os_path.pages)
            e2.insert(0,totalpages)
    except:
        print("select any file")
# adding split defination
def split():
    global fd
    try:
        pages=e3.get().split("-")
        startpage=int(pages[0])
        endpage=int(pages[1])
        with open(fd,"rb")as fp:
            rd=PdfReader(fp)
            wd=PdfWriter()
            for i in range(startpage,endpage):
                cpage=rd.pages[i]
                wd.add_page(cpage)
            with open("result.pdf","wb") as nf:
                wd.write(nf)
        if os_path.exists("result.pdf"):
            print("pdf successfully split")
    except:
        print("enter the correct value")

# owrking on clear button
def delete():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
# now adding lables and widgets
# heading or the title of the project
l1 = Label(r, text="PDF SPLITTER", fg="white", font=("helvetica 26 bold"),bg="#26000a")
l1.pack()

l2=Label(r, text="select PDF:", font=("Times 15 bold"),bg="#26000a",fg="white")
l2.place(x=60, y=100)
#now adding entries
e1 = Entry(r, width=40, borderwidth=5, selectborderwidth=20, font=("arial 15"))
e1.place(x=190, y=95)
# now adding button for that entry
b1=Button(r,text="Browse PDF",bg="red",fg="white",command=browse,width=15,font=("Time 10 bold"))
b1.place(x=340,y=140)

# lable for total pages
l3=Label(r,text="Total pages:",font=("Times 15 bold"),bg="#26000a",fg="white")
l3.place(x=60,y=190)
# entry for counting total number of pages
e2=Entry(r,width=40, borderwidth=5, selectborderwidth=20, font=("arial 15"))
e2.place(x=190,y=190)
# splliting enter the lable and entry
l4=Label(r,text="select the pages:",font=("Times 15 bold"),bg="#26000a",fg="white")
l4.place(x=60,y=270)
e3=Entry(r,width=38, borderwidth=5, selectborderwidth=20, font=("arial 15"))
e3.place(x=210,y=270)
# now adding button to split the pdf
b2=Button(r,text="split PDF",bg="green",fg="white",command=split,width=15,font=("Time 10 bold"))
b2.place(x=340,y=320)
b3=Button(r,text="CLEAR",bg="black",fg="white",command=delete,width=20,height=2,font=("Time 10 bold"))
b3.place(x=320,y=360)
r.mainloop()




