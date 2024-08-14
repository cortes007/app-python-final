import tkinter as tk
from vistas.vista_menu import VistaMenu
from vistas.vista_inicio import VentanaInicio

from controladores.controlador_inventario import ControladorInventario
from controladores.controlador_historial_ventas import ControladorHistorialVentas
from controladores.controlador_historial_compras import ControladorHistorialCompras
from controladores.controlador_registro_venta import ControladorRegistroVenta
from controladores.controlador_registro_compra import ControladorRegistroCompra

class ControladorMenu:
    def __init__(self):
        self.historial_ventas = []
        self.historial_compras = []
        self.inventario = []
        self.ventana_actual = None

    def iniciar_sistema(self):
        self.abrir_inicio()

    def abrir_inicio(self):
        root = tk.Tk()
        self.ventana_actual = VentanaInicio(root, self)
        root.mainloop()

    def abrir_menu(self):
        if self.ventana_actual:
            self.ventana_actual.ventana.destroy()
        self.ventana_actual = VistaMenu(self)  
        self.ventana_actual.ventana.mainloop()

    def abrir_inventario(self):
        controlador = ControladorInventario(self)
        controlador.abrir_inventario()

    def abrir_historial_ventas(self):
        controlador = ControladorHistorialVentas(self)
        controlador.abrir_historial_ventas()

    def abrir_historial_compras(self):
        controlador = ControladorHistorialCompras(self)
        controlador.abrir_historial_compras()

    def abrir_registro_venta(self):
        controlador = ControladorRegistroVenta(self)
        controlador.abrir_registro_venta()

    def abrir_registro_compra(self):
        controlador = ControladorRegistroCompra(self)
        controlador.abrir_registro_compra()
