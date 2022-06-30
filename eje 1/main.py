from tkinter import *
from tkinter import ttk, font
import sys
class Aplicacion():
    __ventana=None
    __peso=None
    __altura=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Acceso")
        self.__ventana.resizable(0,0)
        fuente = font.Font(weight='bold')
        self.marco = ttk.Frame(self.__ventana, borderwidth=2,relief="raised", padding=(10,10))
        self.pesoLbl = ttk.Label(self.marco, text="Peso en kg:",font=fuente, padding=(5,5))
        self.alturaLbl = ttk.Label(self.marco, text="Altura:",font=fuente, padding=(5,5))
        self.__peso = StringVar()
        self.__altura = StringVar()
        self.__peso.set('')
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.__peso,width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.__altura, width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar",padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar",padding=(5,5))
        self.marco.grid(column=0, row=0)
        self.pesoLbl.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.alturaLbl.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)
        self.ctext1.focus_set()
        self.__ventana.mainloop()
    def aceptar(self):
        calculo=float(self.ctext1.get())/float(self.ctext2.get())**2
        print(calculo)
        messagebox.showerror(title='su peso',message="Peso inferior al normal")

        if calculo<18.5:
            messagebox.showerror(title='su peso',message="Peso inferior al normal")
        if calculo>18.5 and calculo<25:
            messagebox.showerror(title='su peso',message="Peso normal")
        if calculo>=25.0 and calculo<30:
            messagebox.showerror(title='su peso',message="Peso superior normal")
        else:
            messagebox.showerror(title='su peso',message="Obesidad")
                    
def testAPP():
    mi_app = Aplicacion()
    return 0
if __name__ == '__main__':
    testAPP()

