from tkinter import ttk, font
import tkinter as tk

class Ventana(tk.Tk):
    __precio_base=None
    __precio_iva=None
    __total=None
    __iva=None
    def __init__(self):
        super().__init__()
        self.__iva=tk.IntVar()
        self.__precio_base=tk.StringVar()
        self.__precio_iva=tk.StringVar()
        self.__total=tk.StringVar()
        
    def widget(self):
        opts = { 'ipadx': 10, 'ipady': 10, 'fill': tk.BOTH }
        titulo=tk.Label(self, text="Calculo de IVA",bg="light blue")
        frame=tk.Frame(self)
        frame['borderwidth'] = 2
        frame['relief'] = 'sunken'
        frame=self.Frame(frame)
        
        titulo.pack(side=tk.TOP, **opts)
        frame.pack(fill=tk.BOTH,expand=True)
        
    def Frame(self,ventana):
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        label_precio=tk.Label(ventana,text="Precio sin IVA")
        entry_precio=tk.Entry(ventana,textvariable=self.__precio_base)
        RButtoniva21=tk.Radiobutton(ventana,text="IVA 21%",variable=self.__iva,value=0)
        Rbuttoniva10=tk.Radiobutton(ventana,text="IVA 10,5%",variable=self.__iva,value=1)
        label_iva=tk.Label(ventana,text="IVA")
        entry_iva=tk.Entry(ventana,textvariable=self.__precio_iva)
        label_total=tk.Label(ventana,text="Precio Con IVA")
        entry_resultado=tk.Entry(ventana,textvariable=self.__total)
        bottonCalcula=tk.Button(ventana,text="Calcular",bg="light blue",command=self.calcula)
        bottonSalir=tk.Button(ventana,text="Salir",bg="red",command=self.destroy)
       
        label_precio.grid(row=0,column=0)
        entry_precio.grid(row=0,column=1)
        RButtoniva21.grid(row=1,column=0)
        Rbuttoniva10.grid(row=2,column=0)
        label_iva.grid(row=3,column=0)
        entry_iva.grid(row=3,column=1)
        label_total.grid(row=4,column=0)
        entry_resultado.grid(row=4,column=1)
        bottonCalcula.grid(row=5,column=0)
        bottonSalir.grid(row=5,column=1)
        return ventana
        
    def calcula(self):
        if self.__iva.get()==0:
            total=float(self.__precio_base.get())*0.21
            self.__precio_iva.set(total)
            self.__total.set(total+float(self.__precio_base.get()))
        else:
            if self.__iva.get()==1:
                total=float(self.__precio_base.get())*0.105
                self.__precio_iva.set(total)
                self.__total.set(total+float(self.__precio_base.get()))
        
        
        
        
if __name__ == "__main__":
    ventana=Ventana()
    ventana.widget()
    ventana.mainloop()