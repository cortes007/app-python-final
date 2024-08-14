from vistas.vista_historial_compras import VistaHistorialCompras
from modelos.base_datos import obtener_historial_compras
from tkinter import messagebox

class ControladorHistorialCompras:
    def __init__(self, controlador_menu):
        self.controlador_menu = controlador_menu

    def abrir_historial_compras(self):
        if self.controlador_menu.ventana_actual:
            self.controlador_menu.ventana_actual.ventana.destroy()
        self.controlador_menu.ventana_actual = VistaHistorialCompras(self)
        
        try:
            historial_compras = obtener_historial_compras()
            self.controlador_menu.ventana_actual.mostrar_compras(historial_compras)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el historial de compras: {e}")
        
        self.controlador_menu.ventana_actual.ventana.mainloop()

    def cerrar_historial_compras(self):
        self.controlador_menu.abrir_menu()
