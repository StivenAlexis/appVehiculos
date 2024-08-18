import tkinter as tk
from tkinter import font

ventana = tk.Tk()
ventana.title('Mantenimiento Moto')
ventana.geometry('300x300')

marco = tk.Frame(ventana)
marco.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mi_fuente = font.Font(family="Helvetica", size=14, weight="bold")

lista = tk.Listbox(marco, yscrollcommand=scrollbar.set, font=mi_fuente, bg="lightgray", fg="navy", relief="groove")
lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

mantenimientos_moto = ["Cambio de aceite", "Revisión de cadena", "Ajuste de frenos", 
                       "Cambio de filtro de aire", "Revisión de luces", "Inspección de neumáticos", 
                       "Ajuste de embrague"]

for mantenimiento in mantenimientos_moto:
    lista.insert(tk.END, mantenimiento)

scrollbar.config(command=lista.yview)

ventana.mainloop()
