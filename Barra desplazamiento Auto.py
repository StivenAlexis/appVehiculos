import tkinter as tk
from tkinter import font

# Ventana principal
ventana = tk.Tk()
ventana.title('Mantenimiento Auto' )
ventana.geometry ('300x300' )
marco = tk.Frame(ventana)
marco.pack(padx = 10, pady = 10)
scrollbar = tk.Scrollbar (marco)
scrollbar .pack(side = tk.RIGHT, fill = tk.Y)
lista = tk.Listbox(marco, yscrollcommand = scrollbar .set)

# Crear una fuente personalizada
mi_fuente = font.Font(family="Helvetica", size=14, weight="bold")

# Crear la Listbox con la fuente personalizada
lista = tk.Listbox(marco, yscrollcommand=scrollbar.set, font=mi_fuente)
# Crear la Listbox con formato
lista = tk.Listbox(marco, yscrollcommand=scrollbar.set, font=mi_fuente, bg="lightgray", fg="navy", relief="groove")

# Lista de servicios
mantenimiento = ["Service", "Alineado y Balanceo", "Cubiertas", "Bateria", "Frenos", "Amortiguadores", "Luces"]

# Agregar elementos a la lista
for mantenimiento in mantenimiento:
    lista.insert(tk.END, mantenimiento)

# Crear una barra de desplazamiento
scrollbar = tk.Scrollbar(ventana)

# Configurar la lista para usar la barra de desplazamiento
lista.config(yscrollcommand=scrollbar.set)

# Empaquetar la lista y la barra de desplazamiento
lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

ventana.mainloop()