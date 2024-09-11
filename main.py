import tkinter as tk
from modulo import AppVehiculos
from tkinter import ttk, messagebox
from datetime import datetime


def __init__(self, root):
        self.root = root
        self.root.title("AUTOBOT REPARACIONES SRL: Tu vehículo al 100%!")
        self.root.geometry("700x700")
 
        #Crear el frame principal
        self.frame = tk.Frame(self.root, bg='steelblue')
        self.frame.pack(padx=10, pady=10, fill='both', expand='true')

        #Pantalla de registro del vehículo
        self.data_vehiculo = {}
        self.create_register_screen()






if __name__ == "__main__":
    root = tk.Tk()
    app = AppVehiculos(root)
    root.mainloop()
