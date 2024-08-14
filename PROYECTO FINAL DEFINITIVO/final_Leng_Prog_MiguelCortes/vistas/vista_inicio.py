import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class VentanaInicio:
    def __init__(self, root, controlador_menu):
        self.ventana = root
        self.controlador_menu = controlador_menu
        self.ventana.title("Ventana de Inicio")
        self.ventana.geometry("400x400")
        self.ventana.resizable(0, 0)

        self.etiqueta_bienvenida = tk.Label(self.ventana, text="Bienvenido al Sistema", font=("Arial", 18))
        self.etiqueta_bienvenida.pack(pady=70)

        self.etiqueta2 = tk.Label(self.ventana, text="contraseña --> 1234", font=("Arial", 12))
        self.etiqueta2.pack()

        self.n = tk.BooleanVar()

        self.ver_contra = ttk.Checkbutton(self.ventana, text="Ver contraseña", variable=self.n, command=self.ver_contraseña)
        self.ver_contra.pack(pady=10)

        self.contraseña = ttk.Entry(self.ventana, show="*")
        self.contraseña.pack()

        self.boton_inicio = tk.Button(self.ventana, text="Ingresar al Sistema", command=self.vista)
        self.boton_inicio.pack(pady=20)

    def vista(self):
        contraseña = self.contraseña.get()
        if contraseña == "1234":
            messagebox.showinfo("Validado", "Puede ingresar")
            self.controlador_menu.abrir_menu() 
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    def ver_contraseña(self):
        if self.n.get():
            self.contraseña.config(show="")
        else:
            self.contraseña.config(show="*")
