import tkinter as tk
from tkinter import messagebox


class mruclass:

    def __init__(self, color1, pantalla):
        self.color1 = color1
        self.pantalla = pantalla
        self.b_vel = False
        self.mag_vel = "m/s"
        self.valores= [None, None, None]  # Velocidad tiempo distancia


    def inicializar(self):
        self.mru()
        self.contextual()
        self.leyenda()
        self.UILeft.pack(side=tk.TOP, pady=(0, 10))
        self.mrup2.pack(side=tk.TOP)
        self.UIbottom.pack(side=tk.BOTTOM)

    def mrucalcular(self):
        self.valorb = [False, False, False]  # Velocidad, tiempo, distancia
        self.magnitudes = ["velocidad", "tiempo", "distancia"]
        for r in self.mruEntry:
            r.configure(state=tk.DISABLED)
        self.mruBoton[2].configure(state=tk.DISABLED)
        self.mruBoton[3].configure(state=tk.DISABLED)
        for i in range(0, len(self.valores)):
            try:
                if i == 1 and float(self.mruEntry[i].get()) < 0:
                    self.valorb[i] = False
                    tk.messagebox.showerror(f"Error en {self.magnitudes[i]}", "Ingrese un tiempo positivo")
                else:
                    self.valores[i] = float(self.mruEntry[i].get())
                    self.valorb[i] = True
                if i == 0 and self.b_vel:
                    self.valores[i] = float(self.valores[i] * 5 / 18)
            except ValueError:
                self.valorb[i] = False
                if self.mruEntry[i].get() == '':
                    pass
                else:
                    tk.messagebox.showerror(f"Error en {self.magnitudes[i]}", "Ingrese un valor válido")
            for a in range(0, len(self.valorb)):
                if self.valorb[a]:
                    self.mruEntry[a].configure(disabledforeground='black', disabledbackground='lightblue')
                else:
                    self.mruEntry[a].configure(disabledforeground="black", disabledbackground="lightgreen")
        if self.valorb[0] and self.valorb[1] and self.valorb[2]:
            print(abs((self.valores[2] / self.valores[1]) - self.valores[0]))
            if abs((self.valores[2] / self.valores[1]) - self.valores[0]) < 0.005:
                tk.messagebox.showinfo("¡Correcto!", "La información es real")
            else:
                tk.messagebox.showerror("Falsedad de datos", "Los datos ingresados no son verdaderos")
            pass
        elif self.valorb[1] and self.valorb[2]:
            self.mruEntry[0].configure(state=tk.NORMAL)
            velo = self.valores[2] / self.valores[1]
            self.mruEntry[0].delete(0, tk.END)
            if self.b_vel:
                velo = velo * (18 / 5)
            self.mruEntry[0].insert(0, f"{velo:.2f}")
            self.mruEntry[0].configure(state='disabled')
        elif self.valorb[1] and self.valorb[0]:
            dist = self.valores[0] * self.valores[1]
            self.mruEntry[2].configure(state=tk.NORMAL)
            self.mruEntry[2].delete(0, tk.END)
            self.mruEntry[2].insert(0, f"{dist:.2f}")
            self.mruEntry[2].configure(state='disabled')
        elif self.valorb[2] and self.valorb[0]:
            if (self.valores[2] * self.valores[0]) >= 0:
                self.mruEntry[1].configure(state=tk.NORMAL)
                tiem = self.valores[2] / self.valores[0]
                self.mruEntry[1].delete(0, tk.END)
                self.mruEntry[1].insert(0, f"{tiem:.2f}")
                self.mruEntry[1].configure(state='disabled')
            else:
                tk.messagebox.showerror("Error de signos", "Verifique el ingreso de los signos")
                self.mrureinicio()
        else:
            tk.messagebox.showerror("Insuficientes datos", "Ingrese al menos 2 datos válidos para realizar el calculo")
            self.mrureinicio()


    def mrureinicio(self):
        try:
            for r in range(0, len(self.mruEntry)):
                self.mruEntry[r].configure(state=tk.NORMAL)
                if not self.valorb[r]:
                    self.mruEntry[r].delete(0, tk.END)
            self.mruBoton[2].configure(state=tk.NORMAL)
            self.mruBoton[3].configure(state=tk.NORMAL)
        except AttributeError:
            pass



    def mrulimpiar(self):
        for r in self.mruEntry:
            r.configure(state=tk.NORMAL)
            r.delete(0, tk.END)
        self.mruBoton[2].configure(state=tk.NORMAL)
        self.mruBoton[3].configure(state=tk.NORMAL)


    def mru(self):
        self.mruEntry = []
        self.mruLabel = []
        self.mruBoton = []
        self.mrup = tk.Frame(self.pantalla)
        self.mrup2 = tk.Frame(self.mrup)
        self.mrup.configure(background=self.color1)
        self.mrup2.configure(background=self.color1)
        self.mruEntry.append(tk.Entry(self.mrup2, width=20))  # Indice 0, para velocidad
        self.mruLabel.append(tk.Label(self.mrup2, text=f"Velocidad ({self.mag_vel}): ", background=self.color1))  # Indice 0, para Velocidad
        self.mruEntry.append(tk.Entry(self.mrup2, width=20))  # Indice 1, para tiempo
        self.mruLabel.append(tk.Label(self.mrup2, text="Tiempo (Segundos): ", background=self.color1))  # Indice 1, para tiempo
        self.mruLabel.append(tk.Label(self.mrup2, text="Distancia (Metros): ", background=self.color1))  # Indice 3, para distancia
        self.mruEntry.append(tk.Entry(self.mrup2, width=20))  # Indice 2, para distancia
        self.mruBoton.append(tk.Button(self.mrup2, text="Corregir", pady=10, command=self.mrureinicio))  # Boton 0, Reinicio
        self.mruBoton.append(tk.Button(self.mrup2, text="Limpiar", pady=10, command=self.mrulimpiar))  # Boton 1, Limpiar)
        self.mruBoton.append(tk.Button(self.mrup2, text="Calcular", pady=10, command=self.mrucalcular))  # Boton 2, Calcular
        self.mruBoton.append(tk.Button(self.mrup2, text=f"{self.mag_vel}", pady=10, padx=10, command=self.cambio_magnitud))
        self.colocar_pantalla()

    def contextual(self):
        options = [
            {'text': 'Valor ingresado', 'color': 'lightblue'},
            {'text': 'Valor calculado', 'color': 'lightgreen'}
        ]
        self.UIbottom = tk.Frame(self.mrup, bg=self.color1)

        for i, option in enumerate(options):
            item_frame = tk.Frame(self.UIbottom, bg=self.color1)
            color_box = tk.Frame(item_frame, bg=option['color'], width=20, height=20, relief='sunken', bd=1)
            color_box.pack(side=tk.LEFT, padx=(0, 5))
            label = tk.Label(item_frame, text=option['text'], bg=self.color1)
            label.pack(side=tk.LEFT)
            item_frame.grid(row=0, column=i, padx=10, pady=5)

    def leyenda(self):
        self.UILeft= tk.Frame(self.mrup, bg=self.color1)
        faux = tk.Frame(self.UILeft, bg=self.color1)
        i = tk.PhotoImage(file="help.png")
        b_au = tk.Button(faux, border=0, image=i, bg=self.color1, command=self.help)
        b_au.image = i
        faux.pack(side=tk.TOP, fill="x")
        b_au.pack(side=tk.RIGHT, padx=5)
        Labels: list = []
        parrafo = ("El Movimiento Rectilíneo Uniforme (MRU) es un tipo de movimiento en el que un\n"
                   "objeto se desplaza en línea recta a velocidad constante, es decir, recorriendo\n"
                   "distancias iguales en intervalos de tiempo iguales, sin experimentar aceleración\n \n."
                   "Ingrese los datos conocidos, los campos vacios se calcularán:")
        self.UILeft.pack(side=tk.BOTTOM, expand=True, padx=10)
        Labels.append(tk.Label(self.UILeft,
                               text="Movimiento Rectilineo Uniforme",
                               font= ("Arial", 16, "bold"),
                               justify=tk.CENTER,
                               bg=self.color1))
        Labels.append(tk.Label(self.UILeft,
                               text=f"{parrafo}",
                               font=("Arial", 8),
                               justify=tk.LEFT,
                               bg=self.color1))
        for l in Labels:
            l.pack(side=tk.TOP)

    def cambio_magnitud(self):
        if self.b_vel:
            self.b_vel = False
            self.mag_vel = "m/s"
        else:
            self.b_vel = True
            self.mag_vel = "km/h"
        for f in self.mruEntry:
            f.grid_forget()
        for f in self.mruLabel:
            f.grid_forget()
        for f in self.mruBoton:
            f.grid_forget()
        self.mruLabel[0].config(text=f"Velocidad ({self.mag_vel}): ")
        self.mruBoton[3].config(text=f"{self.mag_vel}")
        self.colocar_pantalla()

    def colocar_pantalla(self):
        self.mruEntry[0].grid(row=0, column=1, pady=5)
        self.mruLabel[0].grid(row=0, column=0, pady=5, sticky='W')
        self.mruEntry[1].grid(row=1, column=1, pady=5)
        self.mruLabel[1].grid(row=1, column=0, pady=5, sticky='W')
        self.mruLabel[2].grid(row=2, column=0, sticky='W')
        self.mruEntry[2].grid(row=2, column=1)
        self.mruBoton[0].grid(row=4, column=0, pady=5)
        self.mruBoton[1].grid(row=5, column=0, pady=5)
        self.mruBoton[2].grid(row=4, column=1, pady=5)
        self.mruBoton[3].grid(row=5, column=1, pady=5)

    def help(self):
        emergente = tk.Toplevel(bg=self.color1)
        emergente.title("Ayuda")
        emergente.geometry("400x350")
        emergente.resizable(False, False)
        Label: list = []
        Label.append(tk.Label(emergente, font=("Helvetica", 14, "bold"), text="¿Cómo usar esta calculadora?", justify=tk.CENTER, bg=self.color1))
        cuerpo = (
            "Para usar este sistema correctamente es importante comprender el uso de cada uno de los campos disponibles. \n\n"
            "En esta calculadora podrá encontrar 3 campos disponibles, de los cuales, pueden realizarse dos funciones: "
            "Calcular o Verificar. Será decidido cual usar según la cantidad de campos ingresados.\n\n"
            "Se verificará si las magnitudes son ciertas o no, si se ingresan los 3 campos\n"
            "Se calculará, si se ingresan únicamente 2 campos, calculando el faltante.\n"
            "El programa marcará error si se ingresa solo una cantidad, ya que los datos serán insuficientes para resol"
            "ver el problema"
        )
        Label.append(tk.Label(emergente, font=("Helvetica", 10), text=cuerpo, justify=tk.LEFT, bg=self.color1,
                              wraplength=300))
        for l in Label:
            l.pack(padx=(5,0))