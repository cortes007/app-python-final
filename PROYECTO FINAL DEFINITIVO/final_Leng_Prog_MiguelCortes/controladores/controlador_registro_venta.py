import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from vistas.vista_registro_venta import VistaRegistroVenta
from modelos.base_datos import guardar_nueva_venta

class ControladorRegistroVenta:
    def __init__(self, controlador_menu):
        self.controlador_menu = controlador_menu

    def abrir_registro_venta(self):
        if self.controlador_menu.ventana_actual:
            self.controlador_menu.ventana_actual.ventana.destroy()
        self.controlador_menu.ventana_actual = VistaRegistroVenta(self)
        self.controlador_menu.ventana_actual.ventana.mainloop()

    def validar_datos_venta(self):
        nom_producto = self.controlador_menu.ventana_actual.preguntar_producto.get()
        cantidad = self.controlador_menu.ventana_actual.preguntar_cantidad.get()
        precio = self.controlador_menu.ventana_actual.preguntar_precio.get()
        if (nom_producto and cantidad and precio and len(nom_producto) >= 3 and nom_producto.replace(' ', '').isalpha()
                and cantidad.isdigit() and int(cantidad) >= 1 and precio.isdigit() and int(precio) >= 1):
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            
            
            try:
                guardar_nueva_venta(nom_producto, cantidad, precio, fecha_actual)
                messagebox.showinfo("Datos Guardados Correctamente", "Gracias por rellenar los datos solicitados")
                self.controlador_menu.abrir_menu()
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar la venta: {e}")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos con datos válidos.")
    
    def volver_menu(self):
        self.controlador_menu.abrir_menu()
