import tkinter as tk
from tkinter import ttk

class VistaMenu:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Menú")
        self.ventana.geometry("400x300")
        self.ventana.resizable(0, 0)

        etiqueta = ttk.Label(self.ventana, text="¿Qué acción desea realizar?")
        etiqueta.grid(column=0, row=0, padx=10, pady=10)

        boton_ver_inventario = ttk.Button(self.ventana, text="Ver el inventario", command=self.controlador.abrir_inventario)
        boton_ver_inventario.grid(column=0, row=1, pady=5)

        boton_registrar_nueva_compra = ttk.Button(self.ventana, text="Registrar una nueva compra", command=self.controlador.abrir_registro_compra)
        boton_registrar_nueva_compra.grid(column=0, row=2, pady=5)

        boton_registrar_nueva_venta = ttk.Button(self.ventana, text="Registrar una nueva venta", command=self.controlador.abrir_registro_venta)
        boton_registrar_nueva_venta.grid(column=0, row=3, pady=5)

        boton_historial_de_compras = ttk.Button(self.ventana, text="Historial de compras", command=self.controlador.abrir_historial_compras)
        boton_historial_de_compras.grid(column=0, row=4, pady=5)

        boton_historial_de_ventas = ttk.Button(self.ventana, text="Historial de ventas", command=self.controlador.abrir_historial_ventas)
        boton_historial_de_ventas.grid(column=0, row=5, pady=5)

        self.ventana.columnconfigure(0, weight=1)

    def mostrar(self):
        self.ventana.mainloop()
