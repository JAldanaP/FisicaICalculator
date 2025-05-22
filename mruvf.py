import tkinter as tk
from tkinter import messagebox
import math
import sys
import os

class mruvclass:
    def __init__(self, color1, pantalla):
        self.pantalla = pantalla
        self.color1 = color1
        # self.Entry: list = []
        # self.frames: list = []
        # self.labels: list = []
        # self.botones: list = []
        self.m_vel = 'm/s'
        self.p_ejec = True
        self.magnitudes: list = ["Velocidad final (m/s)", "Velocidad inicial (m/s)", "Aceleración (m/s²)", "Tiempo (s)"
            , "Distancia (m)"]
        self.valores: list = []
        self.b_vel: bool = False
        for i in range(0, len(self.magnitudes)):
            self.valores.append(None)
        self.df_b = [[True, True, True, True, True], # 0
                [True, True, True, True, False], # 1
                [True, True, True, False, True], # 2
                [True, True, True, False, False], # 3
                [True, True, False, True, True], # 4
                [True, True, False, True, False], # 5
                [True, True, False, False, True], # 6
                [True, False, True, True, True], # 7
                [True, False, True, True, False], # 8
                [True, False, True, False, True], # 9
                [True, False, False, True, True], # 10
                [False, True, True, True, True], # 11
                [False, True, True, True, False], # 12
                [False, True, True, False, True], # 13
                [False, True, False, True, True], # 14
                [False, False, True, True, True] # 15
                ]
        pass

    def inicializar(self):
        self.mruv()
        self.contextual()
        self.leyenda()
        self.mruvp2.pack(side=tk.TOP)

    def reiniciar(self):
        try:
            for r in range(0,len(self.Entry)):
                self.Entry[r].configure(state= tk.NORMAL, readonlybackground='#F0F0F0')
                if not self.booleanos[r]:
                    self.Entry[r].delete(0, tk.END)
            self.botones[2].configure(state= tk.NORMAL)
            self.botones[3].configure(state=tk.NORMAL)
        except AttributeError:
            pass

    def acesinvf(self):
        a = ((self.valores[4] / self.valores[3] - self.valores[1]) * 2) / self.valores[3]
        return a

    # def mostrartodo(self):
    #     for r in range(0, len(self.valores)):
    #         print(f"{self.magnitudes[r]}: {self.valores[r]:.2f}")

    def limpiar(self):
        for r in range(0, len(self.Entry)):
            self.Entry[r].configure(state=tk.NORMAL, disabledforeground='#F0F0F0')
            self.Entry[r].delete(0, tk.END)
        self.botones[2].configure(state=tk.NORMAL)
        self.botones[3].configure(state=tk.NORMAL)

    def vfsinace(self):
        a = (2 * self.valores[4] / self.valores[3]) - self.valores[1]
        return a

    def vfsinti(self, inv: bool):
        b = 1
        if inv:
            b = -1
        a = b * math.sqrt(self.valores[1] ** 2 + 2 * self.valores[2] * self.valores[4])
        return a

    def vfsindis(self):
        a = self.valores[1] + self.valores[2] * self.valores[3]
        return a

    def visinvf(self):
        a = (self.valores[4] - (self.valores[2] * (self.valores[3] ** 2) / 2)) / self.valores[3]
        return a

    def vinsinace(self):
        a = (self.valores[4] / self.valores[3] * 2) - self.valores[0]
        return a

    def acesindis(self):
        a = (self.valores[0] - self.valores[1]) / self.valores[3]
        return a

    def disinace(self):
        d = (self.valores[1] + self.valores[0]) / 2 * self.valores[3]
        return d

    def disinvefi(self):
        d = (self.valores[1] * self.valores[3]) + (self.valores[2] * self.valores[3] ** 2 / 2)
        return d

    def tisinace(self):
        t = 2 * self.valores[4] / (self.valores[0] + self.valores[1])
        return t

    def tisindis(self):
        t = (self.valores[0] - self.valores[1]) / self.valores[2]
        return t

    def aceinvadi(self):
        a = -1 * (math.fabs(self.valores[0]) ** 2 / self.valores[4])
        return a

    def vinisindis(self):
        vi = self.valores[0] - self.valores[2] * self.valores[3]
        return vi

    def vinsinti(self):
        vi = math.sqrt(-1 * (2 * self.valores[2] * self.valores[4]) + self.valores[0] ** 2)
        return vi

    def evaluarlogica(self, show: bool):
        # self.mostrartodo()
        evaluador = ((((self.valores[1] + self.valores[0]) / 2) * self.valores[3]) - ((self.valores[1] * self.valores[3]) + (self.valores[2] * (self.valores[3] ** 2) / 2)))
        # evaluador2 = math.sqrt(self.valores[1] ** 2 + 2 * self.valores[2] * self.valores[4]) - self.valores[0]
        evaluador1 = self.valores[1] ** 2 + -1 * (self.valores[0] ** 2) + 2 * self.valores[2] * self.valores[4]
        # print(evaluador)
        # print(evaluador1)
        # print(evaluador2)
        if 0.05 >= evaluador >= -0.05 and (0.05 >= evaluador1 >= -0.05):
            for r in range(0, len(self.valores)):
                self.Entry[r].configure(state=tk.NORMAL)
                self.Entry[r].delete(0, tk.END)
                self.Entry[r].insert(0, f"{self.valores[r]:.2f}")
                self.Entry[r].configure(state=tk.DISABLED)
            if show:
                tk.messagebox.showinfo("¡Correcto!", "El sistema está correctamente escrito")
            if self.valores[3] < 0:
                tk.messagebox.showinfo("Posible error", "Según el contexto, este problema podría no"
                                                        " tener solución. Verifique las magnitudes"
                                                        " ingresadas")
        else:
            tk.messagebox.showerror("Datos invalidos", "Los datos ingresados son invalidos")

    def calcular(self):
        if self.booleanos == self.df_b[0]:
            self.evaluarlogica(True)
            pass
        elif self.booleanos == self.df_b[1]:
            try:
                self.valores[4] = self.disinace()
                self.evaluarlogica(True)
            except ZeroDivisionError:
                self.valores[4] = self.disinvefi()
                self.evaluarlogica(True)
            pass
        elif self.booleanos == self.df_b[2]:
            try:
                self.valores[3] = self.tisinace()
                self.evaluarlogica(True)
            except ZeroDivisionError:
                try:
                    self.valores[3] = self.tisindis()
                    self.evaluarlogica(True)
                except ZeroDivisionError:
                    tk.messagebox.showerror("Fisicamente imposible", "El problema no tiene una solución real")
        elif self.booleanos == self.df_b[3]:
            try:
                self.valores[3] = self.tisindis()
                self.valores[4] = self.disinvefi()
                self.evaluarlogica(False)
            except ZeroDivisionError:
                tk.messagebox.showerror("Insuficientes datos", "La aceleración en el problema no puede ser 0")
        elif self.booleanos == self.df_b[4]:
            try:
                self.valores[2] = self.acesindis()
                self.evaluarlogica(True)
            except ZeroDivisionError:
                tk.messagebox.showerror("Insuficientes datos", "El tiempo en el problema no puede ser 0")
        elif self.booleanos == self.df_b[5]:
            try:
                self.valores[2] = self.acesindis()
                self.valores[4] = self.disinvefi()
                self.evaluarlogica(False)
            except ZeroDivisionError:
                tk.messagebox.showerror("Insuficientes datos", "El tiempo en el problema no puede ser 0")
        elif self.booleanos == self.df_b[6]:
            try:
                self.valores[3] = self.tisinace()
                self.valores[2] = self.acesindis()
                self.evaluarlogica(False)
            except ZeroDivisionError:
                try:
                    self.valores[2] = self.aceinvadi()
                    self.valores[3] = self.tisindis()
                    self.evaluarlogica(False)
                except ZeroDivisionError:
                    tk.messagebox.showerror("Verifique las magnitudes", "El problema no tiene solución física real")
        elif self.booleanos == self.df_b[7]:
            self.valores[1] = self.vinisindis()
            self.evaluarlogica(True)
        elif self.booleanos == self.df_b[8]:
            self.valores[1] = self.vinisindis()
            self.valores[4] = self.disinvefi()
            self.evaluarlogica(False)
        elif self.booleanos == self.df_b[9]:
            try:
                self.valores[1] = self.vinsinti()
                if self.valores[0] == self.valores[1] and self.valores[2] != 0:
                    self.valores[1] = -1 * self.valores[1]
                    tk.messagebox.showinfo("Ambiguedad de resultados", "Es posible que el tiempo sea 0, pero"
                                                                       " se ignora el caso y se presenta el otro posible")
                try:
                    self.valores[3] = self.tisindis()
                    if self.valores[3] < 0:
                        self.valores[1] = self.valores[1] * -1
                        self.valores[3] = self.tisindis()
                    self.evaluarlogica(False)
                except ZeroDivisionError:
                    try:
                        self.valores[3] = self.tisinace()
                        if self.valores[3] < 0:
                            self.valores[1] = self.valores[1] * -1
                            self.valores[3] = self.tisinace()
                        self.evaluarlogica(False)
                    except ZeroDivisionError:
                        tk.messagebox.showerror("Verifique las magnitudes", "El problema no tiene solución física real")
            except ValueError:
                tk.messagebox.showerror("Verifique las magnitudes", "El problema no tiene solución física real")
        elif self.booleanos == self.df_b[11]:
            self.valores[0] = self.vfsindis()
            self.evaluarlogica(True)
        elif self.booleanos == self.df_b[10]:
            try:
                self.valores[1] = self.vinsinace()
                self.valores[2] = self.acesindis()
                self.evaluarlogica(False)
            except ZeroDivisionError:
                self.valores[1] = self.valores[0]
                self.valores[3] = 0
        elif self.booleanos == self.df_b[12]:
            self.valores[0] = self.vfsindis()
            self.valores[4] = self.disinvefi()
            self.evaluarlogica(False)
        elif self.booleanos == self.df_b[13]:
            self.valores[0] = self.vfsinti(False)
            try:
                self.valores[3] = self.tisindis()
            except ZeroDivisionError:
                try:
                    self.valores[3] = self.tisinace()
                    if self.valores[3] <= 0:
                        self.valores[0] = self.vfsinti(True)
                        self.valores[3] = self.tisinace()
                    self.evaluarlogica(False)
                except ZeroDivisionError:
                    try:
                        self.valores[0] = self.vfsinti(True)
                        self.valores[3] = self.tisinace()
                        self.evaluarlogica(False)
                    except ZeroDivisionError:
                        tk.messagebox.showerror("Verifique las magnitudes", "El problema no tiene solución física real")
            else:
                if self.valores[3] <= 0:
                    self.valores[0] = self.vfsinti(True)
                    self.valores[3] = self.tisindis()
                self.evaluarlogica(False)
        elif self.booleanos == self.df_b[14]:
            try:
                self.valores[0] = self.vfsinace()
                self.valores[2] = self.acesinvf()
                self.evaluarlogica(False)
            except ZeroDivisionError:
                tk.messagebox.showerror("El tiempo es incorrecto", "Por la naturaleza de la consulta, el "
                                                                   "tiempo no puede ser 0"
                                                                   " para la determinación de los casos.")
        elif self.booleanos == self.df_b[15]:
            try:
                self.valores[1] = self.visinvf()
                self.valores[0] = self.vfsinace()
                self.evaluarlogica(False)
            except ZeroDivisionError:
                tk.messagebox.showerror("El tiempo es incorrecto", "Por la naturaleza de la consulta, el "
                                                                   "tiempo no puede ser 0"
                                                                   " para la determinación de los casos.")

    def evaluar(self):
        fllw = True
        self.booleanos = []
        for i in range(0, len(self.magnitudes)):
            self.booleanos.append(False)
        for i in range(0, len(self.Entry)):
            try:
                if i != 3:
                    self.valores[i] = float(self.Entry[i].get())
                    self.booleanos[i] = True
                elif i == 3 and float(self.Entry[i].get()) >= 0:
                    self.valores[i] = float(self.Entry[i].get())
                    self.booleanos[i] = True
                else:
                    tk.messagebox.showerror("Error con tiempo", "Verifique la magnitud del tiempo. "
                                                                "El tiempo no es negativo")
                    fllw = False
            except ValueError:
                self.booleanos[i] = False
                if self.Entry[i].get() == '':
                    pass
                else:
                    tk.messagebox.showerror(f"Error en {self.magnitudes[i]}", "Ingrese un valor válido")
        if fllw:
            i = 0
            for r in range(0, len(self.booleanos)):
                if self.booleanos[r]:
                    i = i + 1
            if i >= 3:
                for i in range(0, len(self.Entry)):
                    self.Entry[i].configure(state="disabled")
                    if self.booleanos[i]:
                        self.Entry[i].configure(disabledbackground='lightblue', disabledforeground= 'black')
                    else:
                        self.Entry[i].configure(disabledbackground='lightgreen', disabledforeground= 'black')
                self.botones[2].configure(state=tk.DISABLED)
                self.botones[3].configure(state=tk.DISABLED)
                self.calcular()
            else:
                tk.messagebox.showerror("Datos insuficientes", "Datos insuficientes para realizar el problema")


    def mruv(self):
        self.frames = []
        self.Entry = []
        self.labels = []
        self.botones = []
        self.mruvp = tk.Frame(self.pantalla, background=self.color1)
        self.mruvp2 = tk.Frame(self.mruvp, background=self.color1)
        self.frames.append(tk.Frame(self.mruvp2, background=self.color1))  # Frame 0, Ingreso de datos
        self.frames[0].pack(fill="both", expand=True)
        self.frames.append(tk.Frame(self.mruvp2, background=self.color1))  # Frame 1, Botones
        self.frames[1].pack(fill="both", expand=True)
        for i in range(0, len(self.magnitudes)):
            self.Entry.append(tk.Entry(self.frames[0], width= 20))
            self.labels.append(tk.Label(self.frames[0], background=self.color1, text=self.magnitudes[i]))
        self.botones.append(tk.Button(self.frames[1], text="Corregir", command=self.reiniciar))
        self.botones.append(tk.Button(self.frames[1], text="Limpiar", command=self.limpiar))
        self.botones.append(tk.Button(self.frames[1], text="Calcular", command=self.evaluar))
        self.botones.append(tk.Button(self.frames[1], text=f"{self.m_vel}", command=self.cambiarmagnitud))

        self.contruirpantalla()


    def contextual(self):
        options = [
            {'text': 'Valor ingresado', 'color': 'lightblue'},
            {'text': 'Valor calculado', 'color': 'lightgreen'}
        ]
        self.UIbottom = tk.Frame(self.mruvp, bg=self.color1)

        for i, option in enumerate(options):
            item_frame = tk.Frame(self.UIbottom, bg=self.color1)
            color_box = tk.Frame(item_frame, bg=option['color'], width=20, height=20, relief='sunken', bd=1)
            color_box.pack(side=tk.LEFT, padx=(0, 5))
            label = tk.Label(item_frame, text=option['text'], bg=self.color1)
            label.pack(side=tk.LEFT)
            item_frame.grid(row=0, column=i, padx=10, pady=5)
        self.UIbottom.pack(side=tk.BOTTOM, pady=(0, 20))

    def leyenda(self):
        path = os.path.join(sys._MEIPASS, "help.png")
        i = tk.PhotoImage(file=path)
        self.UILeft= tk.Frame(self.mruvp, bg=self.color1)
        Frameaux = tk.Frame(self.UILeft, bg=self.color1)
        Labels: list = []
        a_bo = tk.Button(Frameaux, command=self.help, image=i, bg=self.color1, border=0)
        a_bo.image = i
        parrafo = ("El movimiento rectilíneo uniformemente variado (MRUV), también conocido como movimiento rectilíneo uniformemente\n"
                    "acelerado (MRUA), es un movimiento en el que un cuerpo se desplaza en línea recta, pero su velocidad no es \n"
                    "constante porque está sometido a una aceleración constante.\n \n"
                   "Ingrese los datos conocidos, los campos vacios se calcularán:")
        Labels.append(tk.Label(self.UILeft,
                               text="Movimiento Rectilineo Uniformemente Variado",
                               font= ("Arial", 16, "bold"),
                               justify=tk.CENTER,
                               bg=self.color1))
        Labels.append(tk.Label(self.UILeft,
                               text=f"{parrafo}",
                               font=("Arial", 8),
                               justify=tk.LEFT,
                               bg=self.color1))
        Frameaux.pack(side=tk.TOP, fill="x")
        a_bo.pack(side=tk.RIGHT, padx=5)
        for l in Labels:
            l.pack(side=tk.TOP)
        self.UILeft.pack(side=tk.TOP, expand=True, pady=(0, 10), padx=5)

    def cambiarmagnitud(self):
        if self.b_vel:
            self.b_vel = False
            self.m_vel = 'm/s'
        else:
            self.b_vel = True
            self.m_vel = 'km/h'
        for i in self.labels:
            i.pack_forget()
        for i in self.Entry:
            i.pack_forget()
        for i in self.botones:
            i.grid_forget()
        self.magnitudes: list = [f"Velocidad final ({self.m_vel})", f"Velocidad inicial ({self.m_vel})", f"Aceleración ({self.m_vel}²)", f"Tiempo ({self.m_vel.split('/')[1]})"
            , f"Distancia ({self.m_vel.split('/')[0]})"]
        for i in range(len(self.labels)):
            self.labels[i].config(text=f"{self.magnitudes[i]}")
        self.botones[3].config(text=f"{self.m_vel}")
        self.contruirpantalla()

    def contruirpantalla(self):
        for i in range(0, len(self.magnitudes)):
            self.Entry[i].grid(row=i, column=1, padx=10, pady=3)
            self.labels[i].grid(row=i, column=0, sticky='W', padx=10, pady=3)
        self.botones[0].grid(row=0, column=0, pady=10, padx=10)
        self.botones[1].grid(row=1, column=0, pady=10, padx=10)
        self.botones[2].grid(row=0, column=2, pady=10, padx=10)
        self.botones[3].grid(row=1, column=2, pady=10, padx=10)

    def help(self):
        emergente = tk.Toplevel(bg=self.color1)
        emergente.title("Ayuda")
        emergente.geometry("400x420")
        emergente.resizable(False, False)
        Label: list = []
        Label.append(tk.Label(emergente, font=("Helvetica", 14, "bold"), text="¿Cómo usar esta calculadora?", justify=tk.CENTER, bg=self.color1))
        cuerpo = (
            "Para utilizar este sistema correctamente, es importante comprender el uso de cada uno de los campos disponibles.\n\n"
            "Usted puede ingresar entre 3 y 5 valores. Si no se alcanza ese mínimo, el sistema marcará el problema como "
            "sin solución, ya que no se cuenta con suficiente información (recuerde que el valor 0 sí es válido).\n\n"
            "El sistema puede realizar dos funciones principales: evaluar o calcular. Esta decisión dependerá de los campos "
            "que queden vacíos (los cuales, se calcularán, y serán marcados con un color verde claro).\n\n"
            "En caso de ingresar 4 valores, puede aparecer una advertencia indicando que el problema no tiene solución, ya "
            "que con esa cantidad de datos el sistema podría ser inválido o erróneo.\n\n"
            "Si se ingresan los 5 valores, el sistema validará automáticamente si la información es coherente y consistente."
        )
        Label.append(tk.Label(emergente, font=("Helvetica", 10), text=cuerpo, justify=tk.LEFT, bg=self.color1,
                              wraplength=300))
        for l in Label:
            l.pack(padx=(5,0))
