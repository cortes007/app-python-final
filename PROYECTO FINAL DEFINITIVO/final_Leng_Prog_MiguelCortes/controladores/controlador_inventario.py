from vistas.vista_inventario import VistaInventario
from modelos.base_datos import (
    crear_tablas, 
    obtener_inventario, 
    obtener_historial_ventas, 
    obtener_historial_compras, 
    guardar_nueva_venta, 
    guardar_nueva_compra
)
class ControladorInventario:
    def __init__(self, controlador_principal):
        self.controlador_principal = controlador_principal
        crear_tablas()

    def abrir_inventario(self):
        self.vista_inventario = VistaInventario(self)
        self.vista_inventario.mostrar()

    def obtener_inventario(self):
        inventario = obtener_inventario()
        return inventario

    def obtener_historial_ventas(self):
        historial_ventas = obtener_historial_ventas()
        return historial_ventas

    def obtener_historial_compras(self):
        historial_compras = obtener_historial_compras()
        return historial_compras

    def guardar_nueva_venta(self, nom_producto, cantidad, precio, fecha):
        guardar_nueva_venta(nom_producto, cantidad, precio, fecha)

    def guardar_nueva_compra(self, nom_producto, cantidad, precio, fecha):
        guardar_nueva_compra(nom_producto, cantidad, precio, fecha)

    def volver_menu(self):
        self.controlador_principal.abrir_menu()
