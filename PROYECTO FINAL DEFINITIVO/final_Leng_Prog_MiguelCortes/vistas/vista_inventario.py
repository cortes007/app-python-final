import tkinter as tk
from tkinter import ttk, messagebox
class VistaInventario:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana_inventario = tk.Toplevel()
        self.ventana_inventario.title("Inventario")
        self.ventana_inventario.resizable(0, 0)

        frame = ttk.Frame(self.ventana_inventario)
        frame.pack(padx=10, pady=10)

        label_title = ttk.Label(frame, text="Inventario")
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Cantidad",), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.grid(row=1, column=0, columnspan=2)

        boton_menu = ttk.Button(frame, text="Volver al menú", command=self.cerrar_inventario)
        boton_menu.grid(row=2, column=0, columnspan=2, pady=10)

        self.cargar_datos()
        
    def mostrar(self):
        print("")
        
    def cargar_datos(self):
        inventario = self.controlador.obtener_inventario()
        for item in inventario:
            self.tree.insert("", "end", values=item)

    def cerrar_inventario(self):
        self.ventana_inventario.destroy()
        self.controlador.volver_menu()

