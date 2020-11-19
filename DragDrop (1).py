from tkinter import *

class DragDropListbox(Listbox):
    
    def __init__(self, master,lst, **kw):
        kw['selectmode'] = SINGLE
        Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None
        self.lst = lst

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            pdf_ind = self.curselection()[0]
            pdf = self.lst[pdf_ind]
            self.delete(i)
            self.lst.pop(pdf_ind)
            self.insert(i+1, x)
            self.lst.insert(pdf_ind-1,pdf)
            self.curIndex = i
            for doc in self.lst:
                print(doc.display)
                
        elif i > self.curIndex:
            x = self.get(i)
            pdf_ind = self.curselection()[0]
            pdf = self.lst[pdf_ind]
            self.delete(i)
            self.lst.pop(pdf_ind)
            self.insert(i-1, x)
            self.lst.insert(pdf_ind+1,pdf)
            self.curIndex = i
            for doc in self.lst:
                print(doc.display) 
