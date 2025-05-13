import tkinter as tk
from tkinter import messagebox


class mruclass:

    def __init__(self, color1, pantalla):
        self.color1 = color1
        self.pantalla = pantalla
        self.mru()
        self.contextual()
        self.leyenda()
        self.valores= [None, None, None]  # Velocidad tiempo distancia
        self.UILeft.pack(side=tk.TOP, pady=(0, 10))
        self.mrup2.pack(side=tk.TOP)
        self.UIbottom.pack(side=tk.BOTTOM)

    def mrucalcular(self):
        self.valorb = [False, False, False]  # Velocidad, tiempo, distancia
        self.magnitudes = ["velocidad", "tiempo", "distancia"]
        for r in self.mruEntry:
            r.configure(state=tk.DISABLED)
        self.mruBoton[2].configure(state=tk.DISABLED)
        for i in range(0, len(self.valores)):
            try:
                if i == 1 and float(self.mruEntry[i].get()) < 0:
                    self.valorb[i] = False
                    tk.messagebox.showerror(f"Error en {self.magnitudes[i]}", "Ingrese un tiempo positivo")
                else:
                    self.valores[i] = float(self.mruEntry[i].get())
                    self.valorb[i] = True
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
            if abs((self.valores[2] / self.valores[1]) - self.valores[0]) < 0.00001:
                tk.messagebox.showinfo("¡Correcto!", "La información es real")
            else:
                tk.messagebox.showerror("Falsedad de datos", "Los datos ingresados no son verdaderos")
            pass
        elif self.valorb[1] and self.valorb[2]:
            self.mruEntry[0].configure(state=tk.NORMAL)
            velo = self.valores[2] / self.valores[1]
            self.mruEntry[0].delete(0, tk.END)
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
        for r in self.mruEntry:
            r.configure(state=tk.NORMAL)
        self.mruBoton[2].configure(state=tk.NORMAL)


    def mrulimpiar(self):
        for r in self.mruEntry:
            r.configure(state=tk.NORMAL)
            r.delete(0, tk.END)
        self.mruBoton[2].configure(state=tk.NORMAL)


    def mru(self):
        self.mruEntry = []
        self.mruLabel = []
        self.mruBoton = []
        self.mrup = tk.Frame(self.pantalla)
        self.mrup2 = tk.Frame(self.mrup)
        self.mrup.configure(background=self.color1)
        self.mrup2.configure(background=self.color1)
        self.mruEntry.append(tk.Entry(self.mrup2, width=20))  # Indice 0, para velocidad
        self.mruEntry[0].grid(row=0, column=1, pady=5)
        self.mruLabel.append(tk.Label(self.mrup2, text="Velocidad (m/s): ", background=self.color1))  # Indice 0, para Velocidad
        self.mruLabel[0].grid(row=0, column=0, pady=5, sticky='W')
        self.mruEntry.append(tk.Entry(self.mrup2, width=20))  # Indice 1, para tiempo
        self.mruEntry[1].grid(row=1, column=1, pady=5)
        self.mruLabel.append(tk.Label(self.mrup2, text="Tiempo (Segundos): ", background=self.color1))  # Indice 1, para tiempo
        self.mruLabel[1].grid(row=1, column=0, pady=5, sticky='W')
        self.mruLabel.append(tk.Label(self.mrup2, text="Distancia (Metros): ", background=self.color1))  # Indice 3, para distancia
        self.mruLabel[2].grid(row=2, column=0, sticky='W')
        self.mruEntry.append(tk.Entry(self.mrup2, width=20))  # Indice 2, para distancia
        self.mruEntry[2].grid(row=2, column=1)
        self.mruBoton.append(tk.Button(self.mrup2, text="Reiniciar", pady=10, command=self.mrureinicio))  # Boton 0, Reinicio
        self.mruBoton[0].grid(row=4, column=0, pady=5)
        self.mruBoton.append(tk.Button(self.mrup2, text="Limpiar", pady=10, command=self.mrulimpiar))  # Boton 1, Limpiar)
        self.mruBoton[1].grid(row=5, column=0, pady=5)
        self.mruBoton.append(tk.Button(self.mrup2, text="Calcular", pady=10, command=self.mrucalcular))  # Boton 2, Calcular
        self.mruBoton[2].grid(row=4, column=3, pady=5, rowspan=2)

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
        Labels: list = []
        parrafo = ("El Movimiento Rectilíneo Uniforme (MRU) es un tipo de movimiento en el que un\n"
                   "objeto se desplaza en línea recta a velocidad constante, es decir, recorriendo\n"
                   "distancias iguales en intervalos de tiempo iguales, sin experimentar aceleración.")
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