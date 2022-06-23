import tkinter
from tkinter import *
from tkinter import ttk,font
class Ventana(object):
    __ventana=None
    __altura=None
    __peso=None
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title('Calculadora IMC')
        self.__ventana.configure(background='lightblue')
        fuente=font.Font(weight='normal')
        opts = { 'ipadx': 10, 'ipady': 10, 'sticky':'nswe' }
        self.__altura=DoubleVar()
        self.__peso=DoubleVar()
        self.__peso.set('')
        self.__altura.set('')
        self.labelA=ttk.Label(self.__ventana,background='lightblue',text='Altura:',font=fuente,padding=(5,5))
        self.textA=ttk.Entry(self.__ventana,textvariable=self.__altura,width=30)
        self.textA.configure(background='#000000')
        self.labelB=ttk.Label(self.__ventana,background='lightblue',text='Peso:',font=fuente,padding=(5,5))
        self.textB=ttk.Entry(self.__ventana,textvariable=self.__peso,width=30)
        self.boton1=ttk.Button(self.__ventana,text='Calcular',command=self.calcular)
        self.boton2=ttk.Button(self.__ventana,text='Limpiar',command=self.limpiar)
        self.separator1=ttk.Separator(self.__ventana,orient=HORIZONTAL)
        self.separator2=ttk.Separator(self.__ventana,orient=HORIZONTAL)

        self.labelA.grid(column=0,row=2)
        self.textA.grid(column=1,row=2)
        self.labelB.grid(column=0,row=3)
        self.textB.grid(column=1,row=3)
        self.boton1.grid(column=0,row=4)
        self.boton2.grid(column=1,row=4)


    def calcular(self):

        imc=self.__peso.get()/(self.__altura.get()*self.__altura.get())
        self.labelC=ttk.Label(self.__ventana,background='lightblue',text='Su indice de masa corporal es {:.2f}'.format(imc))
        self.labelC.grid(column=0,row=5)
        if imc < 18.5:
            self.labelD=ttk.Label(self.__ventana,background='lightblue',text='Peso inferior al Normal')
            self.labelD.grid(column=1,row=5)
        elif imc >= 18.5 and imc <=24.9:
            self.labelD=ttk.Label(self.__ventana,background='lightblue',text='Peso Normal')
            self.labelD.grid(column=1,row=5)
        elif imc >= 25 and imc <30:
            self.labelD=ttk.Label(self.__ventana,background='lightblue',text='Peso Superior al Normal')
            self.labelD.grid(column=1,row=5)
        elif imc >=30:
            self.labelD=ttk.Label(self.__ventana,background='lightblue',text='Obesidad')
            self.labelD.grid(column=1,row=5)
        self.labelE=ttk.Label(self.__ventana,background='lightblue',text='Limpie para continuar')
        self.labelE.grid(column=1,row=6)

    def limpiar(self):
        self.__peso.set('')
        self.__altura.set('')
        self.labelC.grid_forget()
        self.labelD.grid_forget()



    def ejecutar(self):
        self.__ventana.mainloop()
if __name__=='__main__':
    ventana=Ventana()
    ventana.ejecutar()
