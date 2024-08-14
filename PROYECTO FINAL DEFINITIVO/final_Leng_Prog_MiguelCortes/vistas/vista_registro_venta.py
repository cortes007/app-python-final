import tkinter as tk
from tkinter import ttk, messagebox

class VistaRegistroVenta:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Registro de Venta")
        self.ventana.geometry("400x400")
        self.ventana.resizable(0, 0)
        self.frame = ttk.Frame(self.ventana)
        self.frame.pack(padx=10, pady=10)
        self.label_title = ttk.Label(self.frame, text="Registrar Venta")
        self.label_title.grid(column=0, row=0, columnspan=2, pady=10)
        self.label_producto = ttk.Label(self.frame, text="Nombre del Producto")
        self.label_producto.grid(column=0, row=1)
        self.preguntar_producto = ttk.Entry(self.frame)
        self.preguntar_producto.grid(column=1, row=1)
        self.label_cantidad = ttk.Label(self.frame, text="Cantidad")
        self.label_cantidad.grid(column=0, row=2)
        self.preguntar_cantidad = ttk.Entry(self.frame)
        self.preguntar_cantidad.grid(column=1, row=2)
        self.label_precio = ttk.Label(self.frame, text="Precio")
        self.label_precio.grid(column=0, row=3)
        self.preguntar_precio = ttk.Entry(self.frame)
        self.preguntar_precio.grid(column=1, row=3)
        self.boton_guardar = ttk.Button(self.frame, text="Guardar", command=self.controlador.validar_datos_venta)
        self.boton_guardar.grid(column=0, row=4, columnspan=2, pady=10)
        self.boton_menu = ttk.Button(self.frame, text="Volver al menú", command=self.controlador.volver_menu)
        self.boton_menu.grid(column=0, row=5, columnspan=2, pady=10)
