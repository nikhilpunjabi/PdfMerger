from tkinter import *
from tkinter.filedialog import *
#from tkinter.ttk import Combobox
from DragDrop import *
import PyPDF2

class PDF_Doc():

    def __init__ (self,filename):
        self.filename = filename
        self.display = filename.split('/')[-1]
        self.pdf = load_pdf(filename)
        self.pages = self.pdf.getNumPages()
        self.start = 1
        self.end = self.pages

    def add_to_writer(self,writer):
        for i in range(self.start-1,self.end):
            writer.addPage(self.pdf.getPage(i))

def load_pdf(filename):
    f = open(filename,'rb')
    return PyPDF2.PdfFileReader(f)

def exit():
    home.destroy()

def remove():
    index = int(listbox.curselection()[0])
    pdf_list.pop(index)
    listbox.delete(ANCHOR)
    #print(pdf_list)

def display(*args):
    index = 0
    print(listbox.curselection())
    index = int(listbox.curselection()[0])
    value = listbox.get(index)
    filename.set(value)
    pages.set(pdf_list[index].pages)
    start.set(pdf_list[index].start)
    end.set(pdf_list[index].end)

def add():
    f = askopenfilename(filetypes = (('PDF File','*.pdf'),('ALL Files','*.*')))
    pdf = PDF_Doc(f)
    pdf_list.append(pdf)
    listbox.insert(END,pdf.display)
    #print(pdf_list)

def set_start(*args):
    index = int(listbox.curselection()[0])
    try :
        pdf_list[index].start = int(start.get())
    except Exception :
        pass

def set_end(*args):
    index = int(listbox.curselection()[0])
    try :
        pdf_list[index].end = int(end.get())
    except Exception :
        pass

def advance():
    try :
        display()
    except Exception:
        pass

def save_pdf():
    writer = PyPDF2.PdfFileWriter()

    output_filename = asksaveasfilename(filetypes = (('PDF File','*.pdf'),('ALL Files','*.*')))
    output_file = open(output_filename,'wb')

    for doc in pdf_list :
        doc.add_to_writer(writer)

    writer.write(output_file)
    output_file.close()
    home.quit()
    
pdf_list = []
home = Tk()
home.title('Merge PDF')
photo = PhotoImage(file = "icon.png")
home.iconphoto(False,photo)
home.configure(bg = 'DodgerBlue4',
               relief = 'groove',
               borderwidth = 10)
home.geometry('650x350+500+200')

filename = StringVar()
pages = StringVar()
start = StringVar()
end = StringVar()

heading = Label(home,
                text = 'PDF   Merger',
                bg = 'gray35',
                fg = 'white',
                highlightcolor="green",
                relief = 'ridge',
                borderwidth = 6,
                font = 'Times 22 bold')
heading.grid(row = 0,column = 0,columnspan = 4,pady = 10,sticky = N)

add_button = Button(home,
                    text = 'ADD',
                    command = add,
                    relief = 'raised',
                    borderwidth = 5,
                    width = 15)
add_button.grid(row = 1,column = 0,sticky = S, padx = 10)

listbox = DragDropListbox(home,pdf_list,
                  bg = 'gray80',
                  fg = 'black',
                  borderwidth = 3,
                  width = 30,
                  font = "times 12",
                  relief = 'ridge')
listbox.bind('<<listboxselect>>',display)

listbox.grid(row = 1,column = 1,rowspan = 4,sticky = E,padx = 20)

del_button = Button(home,
                    text = 'Delete',
                    command = remove,
                    relief = 'raised',
                    borderwidth = 5,
                    width = 15)
del_button.grid(row = 2,column = 0,sticky = S,padx = 10)

file = Label(home,
             text = 'File : ',
             bg = 'DodgerBlue4',
             fg = 'white',
             width = 10)
file.grid(row = 1,column = 2,sticky = E)

pg = Label(home,
             text = 'Pages : ',
             bg = 'DodgerBlue4',
             fg = 'white',
             width = 10)
pg.grid(row = 2,column = 2,sticky = E)

st = Label(home,
             text = 'Start : ',
             bg = 'DodgerBlue4',
             fg = 'white',
             width = 10)
st.grid(row = 3,column = 2,sticky = E)

ed = Label(home,
             text = 'End : ',
             bg = 'DodgerBlue4',
             fg = 'white',
             width = 10)
ed.grid(row = 4,column = 2,sticky = E)



file = Label(home,
             textvariable = filename,
             bg = 'DodgerBlue4',
             fg = 'white',
             width = 15,
             )
file.grid(row = 1,column = 3,sticky = W,padx = 10)

pag = Label(home,
             textvariable = pages,
             bg = 'DodgerBlue4',
             fg = 'white',
             width = 15,
             )
pag.grid(row = 2,column = 3,sticky = W,padx = 10)


s1 = Entry(home,
           textvariable = start,
           relief = 'ridge',
           borderwidth = 3,
           width = 3)
s1.grid(row = 3,column = 3,sticky = W,padx = 10)

e1 = Entry(home,
           textvariable = end,
           relief = 'ridge',
           borderwidth = 3,
           width = 3)
e1.grid(row = 4,column = 3,sticky = W,padx = 10)

advance_button = Button(home,
                    text = 'Details',
                    command = advance,
                    relief = 'raised',
                    borderwidth = 5,
                    width = 15)
advance_button.grid(row = 4,column = 0,sticky = S,padx = 10)

merge_button = Button(home,
                    text = 'Merge',
                    command = save_pdf,
                    relief = 'raised',
                    borderwidth = 5,
                    width = 15)
merge_button.grid(row = 3,column = 0,sticky = S,padx = 10)

start.trace('w',set_start)
end.trace('w',set_end)

exit_button = Button(home,
                    text = 'EXIT',
                    command = exit,
                    relief = 'raised',
                    borderwidth = 5,
                    width = 15)
exit_button.grid(row = 5,column = 0,columnspan = 4,sticky = S, pady = 15)

home.mainloop()




















