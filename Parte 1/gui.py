#!/usr/bin/python
# -*- coding: utf-8 -*-


from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, Button, StringVar, OptionMenu, Scale, HORIZONTAL
from tkFileDialog import askopenfilename
from ttk import Frame, Style
import main as mn
import tkMessageBox

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()

        
    def initUI(self):
        self.blockNum = 20
        self.type = 0
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        #b.pack(padx=10, pady=10)
        Style().configure("TFrame", background="#333")
        
        bard = Image.open("mapa.png")# "Parte 1/mapa.png")
        resized = bard.resize((300,300),Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(resized)
        self.label1 = Label(self, image=bardejov)
        self.label1.image = bardejov
        self.label1.place(x=10, y=40)

        bard2 = Image.open("path.png")# "Parte 1/mapa.png")
        resized2 = bard2.resize((300,300),Image.ANTIALIAS)
        bardejov2 = ImageTk.PhotoImage(resized2)
        self.label2 = Label(self, image=bardejov2)
        self.label2.image = bardejov2
        self.label2.place(x=320, y=40)


        b = Button(self, text="Nueva Imagen", width=12, height=1, command=self.openFile)
        b.place(x= 10, y=10)

        b = Button(self, text="Run", width=12, height=1, command=self.run)
        b.place(x= 10, y=470)

        self.imagePath = StringVar()
        self.imagePath.set("mapa.png")

        self.option = StringVar()
        self.option.set("BFS") # initial value

        options = OptionMenu(self, self.option, "BFS", "DFS", "A*_1", "A*_2")
        options.place(x=10, y = 400)

        self.scale = Scale(self, from_=10,to=200, orient=HORIZONTAL, length = 300)
        self.scale.place(x = 10, y= 350)
        #self.label2 = Label(self, textvariable=self.imagePath,width=40)
        #self.label2.place(x=100, y=10)
        """
        rot = Image.open("Parte 1/path.png")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)        
        
        minc = Image.open("Parte 1/mapa.png")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)  
        """      
              
    def openFile(self):
        self.imagePath.set(askopenfilename())
        self.updateImage()
    
    def updateImage(self):
        print self.imagePath.get()
        bard = Image.open(self.imagePath.get())# "Parte 1/mapa.png")
        resized = bard.resize((300,300),Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(resized)
        self.label1 = Label(self, image=bardejov)
        self.label1.image = bardejov
        self.label1.place(x=10, y=40)
    
    def run(self):
        if self.option.get() == "BFS":
            self.type = 0
        elif self.option.get() == "DFS":
            self.type = 1
        elif self.option.get() ==  "A*_1":
            self.type = 2
        else:
            self.type = 3
        
        path = mn.run(self.imagePath.get(),self.scale.get(), self.type)
        if "error:" in path:
            tkMessageBox.showinfo("Error", path)
            return
        bard2 = Image.open(path)# "Parte 1/mapa.png")
        resized2 = bard2.resize((300,300),Image.ANTIALIAS)
        bardejov2 = ImageTk.PhotoImage(resized2)
        self.label2 = Label(self, image=bardejov2)
        self.label2.image = bardejov2
        self.label2.place(x=320, y=40)
        tkMessageBox.showinfo("Ejecución", "Ejecución finalizada")

def main():
  
    root = Tk()
    root.geometry("650x500")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
