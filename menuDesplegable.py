import tkinter as tk
from tkinter import messagebox


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Bienvenidos a nuestro Local de Reparación")
ventana.geometry("400x200")

# Mensaje de bienvenida
mensaje_bienvenida = tk.Label(ventana, text="¡Bienvenidos a nuestro Local de Reparación de Vehículos!", font=("Arial", 10))
mensaje_bienvenida.pack(pady=20)

# Variable para almacenar la selección de vehiculo
opcion = tk.StringVar()
opcion.set("Seleccione un vehiculo")

# Menú desplegable
menu_desplegable = tk.OptionMenu(ventana, opcion, "moto", "auto")
menu_desplegable.pack(pady=10)

# Botón para confirmar la selección
boton_confirmar = tk.Button(ventana, text="Confirmar")
boton_confirmar.pack(pady=10)


ventana.mainloop()
