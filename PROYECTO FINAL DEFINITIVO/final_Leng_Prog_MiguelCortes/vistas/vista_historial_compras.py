import tkinter as tk
from tkinter import ttk

class VistaHistorialCompras:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Historial de Compras")
        self.ventana.resizable(0, 0)
        self.frame = ttk.Frame(self.ventana)
        self.frame.pack(padx=10, pady=10)
        self.label_title = ttk.Label(self.frame, text="Historial de Compras")
        self.label_title.grid(column=0, row=0, columnspan=2, pady=10)
        self.tree = ttk.Treeview(self.frame, columns=("Fecha", "Producto", "Cantidad", "Precio"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.grid(row=1, column=0, columnspan=2)
        self.boton_menu = ttk.Button(self.frame, text="Volver al menú", command=self.controlador.cerrar_historial_compras)
        self.boton_menu.grid(row=2, column=0, columnspan=2, pady=10)

    def mostrar_compras(self, compras):
        for compra in compras:
            self.tree.insert("", "end", values=compra)
