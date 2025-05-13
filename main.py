import tkinter as tk
from mruf import mruclass
from mruvf import mruvclass

class Aplicacion:
    def __init__(self, raiz):
        self.raiz = raiz
        self.pantalla = tk.Frame(raiz)
        self.pantalla.pack(fill="both", expand=True)
        self.color1 = "#FFF222"
        self.mru = mruclass(self.color1, self.pantalla)
        self.mruv = mruvclass(self.color1, self.pantalla)
        self.menu()
        self.atras()
        self.mostrarpantalla("MENU")


    def menu(self):
        self.menub: list = []
        funciones: dict = {"Movimiento Rectilineo Uniforme": (lambda: self.mostrarpantalla("MRU")),
                           "Movimiento Rectilineo Uniformemente Variado": (lambda: self.mostrarpantalla("MRUV"))}
        self.menup = tk.Frame(self.pantalla)
        self.menup.configure(background=self.color1)
        i = 0
        for f in funciones:
            self.menub.append(tk.Button(self.menup, text=f, padx=10, pady=10, command= funciones[f]))
            self.menub[i].pack(padx= 5, pady=20)
            i = i + 1

    def mostrarpantalla(self, funcion):
        for f in (self.mru.mrup, self.menup, self.enca, self.mruv.mruvp):
            f.pack_forget()
        if funcion == "MRU":
            self.enca.pack(fill="both", expand=True)
            self.mru.mrup.pack(fill="both", expand=True)
            self.raiz.title("Movimiento Rectilineo Uniforme")
        elif funcion == "MENU":
            self.menup.pack(fill="both", expand=True)
            self.raiz.title("Menu")
        elif funcion == "MRUV":
            self.enca.pack(fill="both", expand=True)
            self.mruv.mruvp.pack(fill="both", expand=True)
            self.raiz.title("Movimiento Rectilineo Uniformemente Variado")

    def atras(self):
        self.enca = tk.Frame(self.pantalla)
        self.enca.configure(bg= self.color1)
        self.atrasb = tk.Button(self.enca, text= "Atras", command= lambda: self.mostrarpantalla("MENU"))
        self.atrasb.pack(side = tk.LEFT, pady= 10, padx= 10)
        self.madeof = tk.Label(self.enca,
                               bg= self.color1,
                               text="Hecho por: Jonatán Aldana",
                               font=("Sans", 10),
                               justify= tk.RIGHT)
        self.madeof.pack(side= tk.RIGHT)

# Ajustar el tema de las magnitudes
# Debo de asegurarme que sea intuitivo para el usuario
# Presentar el tema y mi nombre


raiz = tk.Tk()
app = Aplicacion(raiz)
tk.mainloop()