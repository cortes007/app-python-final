from vistas.vista_historial_ventas import VistaHistorialVentas
from modelos.base_datos import obtener_historial_ventas
from tkinter import messagebox

class ControladorHistorialVentas:
    def __init__(self, controlador_menu):
        self.controlador_menu = controlador_menu

    def abrir_historial_ventas(self):
        if self.controlador_menu.ventana_actual:
            self.controlador_menu.ventana_actual.ventana.destroy()
        self.controlador_menu.ventana_actual = VistaHistorialVentas(self)
        
        try:
            historial_ventas = obtener_historial_ventas()
            self.controlador_menu.ventana_actual.mostrar_ventas(historial_ventas)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el historial de ventas: {e}")
        
        self.controlador_menu.ventana_actual.ventana.mainloop()

    def cerrar_historial_ventas(self):
        self.controlador_menu.abrir_menu()
