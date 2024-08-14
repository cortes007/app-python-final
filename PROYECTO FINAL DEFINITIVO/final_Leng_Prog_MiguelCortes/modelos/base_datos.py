import mysql.connector
from tkinter import messagebox

def crear_tablas():
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='bdTrabajoFinal')
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Inventario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                cantidad INT NOT NULL,
                precio DECIMAL(11, 2) NOT NULL,
                fecha DATE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Compras (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                cantidad INT NOT NULL,
                precio DECIMAL(11, 2) NOT NULL,
                fecha DATE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ventas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                cantidad INT NOT NULL,
                precio DECIMAL(11, 2) NOT NULL,
                fecha DATE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HistorialCompras (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                cantidad INT NOT NULL,
                precio DECIMAL(11, 2) NOT NULL,
                fecha DATE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HistorialVentas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                cantidad INT NOT NULL,
                precio DECIMAL(11, 2) NOT NULL,
                fecha DATE NOT NULL
            )
        ''')
        conexion.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al crear las tablas: {err}")
    finally:
        cursor.close()
        conexion.close()

def obtener_inventario():
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='bdTrabajoFinal')
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, cantidad, precio, fecha FROM Inventario")
        inventario = cursor.fetchall()
        return inventario
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al recuperar el inventario: {err}")
        return []
    finally:
        cursor.close()
        conexion.close()

def obtener_historial_ventas():
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='bdTrabajoFinal')
        cursor = conexion.cursor()
        cursor.execute('SELECT fecha, nombre, cantidad, precio FROM HistorialVentas')
        ventas = cursor.fetchall()
        return ventas
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al recuperar el historial de ventas: {err}")
        return []
    finally:
        cursor.close()
        conexion.close()

def obtener_historial_compras():
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='bdTrabajoFinal')
        cursor = conexion.cursor()
        cursor.execute('SELECT fecha, nombre, cantidad, precio FROM HistorialCompras')
        compras = cursor.fetchall()
        return compras
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al recuperar el historial de compras: {err}")
        return []
    finally:
        cursor.close()
        conexion.close()

def guardar_nueva_venta(nom_producto, cantidad, precio, fecha):
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='bdTrabajoFinal')
        cursor = conexion.cursor()
        
        cursor.execute('SELECT cantidad, precio, fecha FROM Inventario WHERE nombre=%s', (nom_producto,))
        resultado = cursor.fetchone()

        if resultado:
            cantidad_inventario, precio_producto, fecha_producto = resultado
            nueva_cantidad = cantidad_inventario - int(cantidad)
            if nueva_cantidad < 0:
                raise ValueError("No hay suficiente cantidad en el inventario para realizar la venta")
            cursor.execute('UPDATE Inventario SET cantidad=%s, precio=%s, fecha=%s WHERE nombre=%s', 
                            (nueva_cantidad, precio_producto, fecha_producto, nom_producto))
        else:
            raise ValueError("El producto no existe en el inventario")
        
        cursor.execute('''
            INSERT INTO Ventas (nombre, cantidad, precio, fecha)
            VALUES (%s, %s, %s, %s)
        ''', (nom_producto, cantidad, precio, fecha))
        
        cursor.execute('''
            INSERT INTO HistorialVentas (nombre, cantidad, precio, fecha)
            VALUES (%s, %s, %s, %s)
        ''', (nom_producto, cantidad, precio, fecha))
        
        conexion.commit()
    
    except mysql.connector.Error as err:
        raise Exception(f"Error al registrar la venta: {err}")
    except ValueError as err:
        raise Exception(str(err))
    finally:
        cursor.close()
        conexion.close()

def guardar_nueva_compra(nom_producto, cantidad, precio, fecha):
    try:
        conexion = mysql.connector.connect(host='localhost', user='root', password='', database='bdTrabajoFinal')
        cursor = conexion.cursor()
            
        cursor.execute('SELECT cantidad, precio, fecha FROM Inventario WHERE nombre=%s', (nom_producto,))
        resultado = cursor.fetchone()
        
        if resultado:
            cantidad_inventario, precio_producto, fecha_producto = resultado
            nueva_cantidad = cantidad_inventario + int(cantidad)
            nuevo_precio = ((precio_producto * cantidad_inventario) + (float(precio) * int(cantidad))) / nueva_cantidad
            nueva_fecha = fecha_producto
            cursor.execute('UPDATE Inventario SET cantidad=%s, precio=%s, fecha=%s WHERE nombre=%s', 
                            (nueva_cantidad, nuevo_precio, nueva_fecha, nom_producto))
        else:
            precio_producto = float(precio)
            fecha_producto = fecha
            cursor.execute('INSERT INTO Inventario (nombre, cantidad, precio, fecha) VALUES (%s, %s, %s, %s)', 
                            (nom_producto, cantidad, precio, fecha))

        cursor.execute('''
            INSERT INTO Compras (nombre, cantidad, precio, fecha)
            VALUES (%s, %s, %s, %s)
        ''', (nom_producto, cantidad, precio, fecha))
            
        cursor.execute('''
            INSERT INTO HistorialCompras (nombre, cantidad, precio, fecha)
            VALUES (%s, %s, %s, %s)
        ''', (nom_producto, cantidad, precio, fecha))
    
        conexion.commit()
    
        messagebox.showinfo("Éxito", "Compra registrada correctamente")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al registrar la compra: {err}")
    finally:
        cursor.close()
        conexion.close()
