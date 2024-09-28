import tkinter as tk  
from tkinter import messagebox  
import sqlite3  

# Conectar a la base de datos (se crea si no existe)  
conn = sqlite3.connect('facturacion.db')  
cursor = conn.cursor()  

# Crear tabla de clientes y facturas  
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (  
                    id INTEGER PRIMARY KEY,  
                    nombre TEXT NOT NULL,  
                    dni TEXT NOT NULL)''')  

cursor.execute('''CREATE TABLE IF NOT EXISTS facturas (  
                    id INTEGER PRIMARY KEY,  
                    cliente_id INTEGER,  
                    cantidad REAL NOT NULL,  
                    fecha TEXT NOT NULL,  
                    FOREIGN KEY (cliente_id) REFERENCES clientes (id))''')  

conn.commit()  

# Funciones para manejar la lógica de la aplicación  
def agregar_cliente():  
    nombre = entry_nombre.get()  
    dni = entry_dni.get()  
    
    if nombre and dni:  
        cursor.execute('INSERT INTO clientes (nombre, dni) VALUES (?, ?)', (nombre, dni))  
        conn.commit()  
        messagebox.showinfo('Éxito', 'Cliente agregado correctamente')  
        entry_nombre.delete(0, tk.END)  
        entry_dni.delete(0, tk.END)  
    else:  
        messagebox.showerror('Error', 'Por favor, completa todos los campos')  

def generar_factura():  
    cliente_id = entry_cliente_id.get()  
    cantidad = entry_cantidad.get()  
    
    if cliente_id and cantidad:  
        cursor.execute('INSERT INTO facturas (cliente_id, cantidad, fecha) VALUES (?, ?, DATE("now"))', (cliente_id, cantidad))  
        conn.commit()  
        messagebox.showinfo('Éxito', 'Factura generada correctamente')  
        entry_cliente_id.delete(0, tk.END)  
        entry_cantidad.delete(0, tk.END)  
    else:  
        messagebox.showerror('Error', 'Por favor, completa todos los campos')  

# Crear la interfaz de Tkinter  
root = tk.Tk()  
root.title("Sistema de Facturación")  

# Sección para agregar clientes  
frame_clientes = tk.Frame(root)  
frame_clientes.pack(pady=10)  

tk.Label(frame_clientes, text="Nombre:").grid(row=0, column=0)  
entry_nombre = tk.Entry(frame_clientes)  
entry_nombre.grid(row=0, column=1)  

tk.Label(frame_clientes, text="DNI:").grid(row=1, column=0)  
entry_dni = tk.Entry(frame_clientes)  
entry_dni.grid(row=1, column=1)  

btn_agregar_cliente = tk.Button(frame_clientes, text="Agregar Cliente", command=agregar_cliente)  
btn_agregar_cliente.grid(row=2, columnspan=2)  

# Sección para generar facturas  
frame_facturas = tk.Frame(root)  
frame_facturas.pack(pady=10)  

tk.Label(frame_facturas, text="ID Cliente:").grid(row=0, column=0)  
entry_cliente_id = tk.Entry(frame_facturas)  
entry_cliente_id.grid(row=0, column=1)  

tk.Label(frame_facturas, text="Cantidad:").grid(row=1, column=0)  
entry_cantidad = tk.Entry(frame_facturas)  
entry_cantidad.grid(row=1, column=1)  

btn_generar_factura = tk.Button(frame_facturas, text="Generar Factura", command=generar_factura)  
btn_generar_factura.grid(row=2, columnspan=2)  

# Ejecutar la aplicación  
root.mainloop()  

# Cerrar la conexión al salir  
conn.close()