import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AppVehiculos:
    
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
        
    def create_register_screen(self):
        self.register_frame = tk.Frame(self.frame, bg='lightblue')  
        self.register_frame.pack(padx=10, pady=10)


        tk.Label(self.register_frame,bg='lightblue', text="Bienvenido a AUTOBOT SRL, por favor complete los campos para registrar su vehículo", wraplength=250).grid(row=0, column=2, columnspan=3)
        self.tipo_vehiculo = tk.StringVar()
        tk.Radiobutton(self.register_frame, bg='lightblue',text="Automotor", variable=self.tipo_vehiculo, value="Automotor").grid(row=1, column=2)
        tk.Radiobutton(self.register_frame, bg='lightblue',text="Motocicleta", variable=self.tipo_vehiculo, value="Motocicleta").grid(row=1, column=3)
        tk.Label(self.register_frame, text="Vehículo:",bg='lightblue').grid(row=1, column=1)

        tk.Label(self.register_frame, text="Marca:",bg='lightblue').grid(row=2, column=1)
        self.brand_entry = tk.Entry(self.register_frame, bg='lightgrey')
        self.brand_entry.grid(row=2, column=2, columnspan=2)

        tk.Label(self.register_frame, text="Modelo:",bg='lightblue').grid(row=3, column=1)
        self.model_entry = tk.Entry(self.register_frame, bg='lightgrey')
        self.model_entry.grid(row=3, column=2, columnspan=2)

        tk.Label(self.register_frame, text="Año:",bg='lightblue').grid(row=4, column=1)
        self.year_entry = tk.Entry(self.register_frame, bg='lightgrey')
        self.year_entry.grid(row=4, column=2, columnspan=2)

        tk.Button(self.register_frame, text="Registrar", command=self.register_vehicle, bg='lightgrey').grid(row=5, column=2, columnspan=2, pady=10)

    def register_vehicle(self):
        self.data_vehiculo = {
            "type": self.tipo_vehiculo.get(),
            "brand": self.brand_entry.get(),
            "model": self.model_entry.get(),
            "year": self.year_entry.get()
        }
        if any(value == "" for value in self.data_vehiculo.values()):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        #Ocultar pantalla de registro y mostrar pantalla de usuario
        self.register_frame.pack_forget()
        self.create_user_screen()

    def create_user_screen(self):
        self.user_frame = tk.Frame(self.frame,bg='lightblue')
        self.user_frame.pack(padx=10, pady=10)

        #Datos del vehículo
        tk.Label(self.user_frame, text=f"Bienvenido usuario del vehículo:", bg='lightblue').grid(row=0, column=1, columnspan=2)
        tk.Label(self.user_frame, text=f"Tipo: {self.data_vehiculo['type']}", bg='lightblue').grid(row=1, column=1, columnspan=2)
        tk.Label(self.user_frame, text=f"Marca: {self.data_vehiculo['brand']}", bg='lightblue').grid(row=2, column=1, columnspan=2)
        tk.Label(self.user_frame, text=f"Modelo: {self.data_vehiculo['model']}", bg='lightblue').grid(row=3, column=1, columnspan=2)
        tk.Label(self.user_frame, text=f"Año: {self.data_vehiculo['year']}", bg='lightblue').grid(row=4, column=1, columnspan=2)

        #Lista de reparaciones disponibles
        self.parts_listbox = tk.Listbox(self.user_frame, bg='lightgrey', width=40)
        self.parts_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        
        self.update_parts_list()
        tk.Label(self.user_frame, text=f"Reparaciones disponibles",bg='lightblue').grid(row=5, column=0, columnspan=2)
        tk.Label(self.user_frame, text=f"Turnos pendientes",bg='lightblue').grid(row=5, column=2, columnspan=2)
        tk.Button(self.user_frame, text="Solicitar turno", command=self.show_reservation_screen, bg='lightgrey').grid(row=7, column=0, pady=10)

        #Lista de turnos pendientes
        self.reservations = []
        self.turnos_lista = tk.Listbox(self.user_frame, bg='lightgrey', width=40)
        self.turnos_lista.grid(row=6, column=2, columnspan=2, padx=10, pady=10)
        

    #Función tipo de vehículo

    def update_parts_list(self):

        self.parts_listbox.delete(0, tk.END)
        if self.data_vehiculo["type"] == "Automotor":
            parts = ["Service", "Alineado y Balanceo", "Cubiertas", "Bateria", "Frenos", "Amortiguadores", "Luces" , "Bocina"]
        else:
            parts = ["Cambio de aceite", "Revisión de cadena", "Ajuste de frenos", "Cambio de filtro de aire", "Revisión de luces", "Inspección de neumáticos", "Ajuste de embrague"]

        for part in parts:
            self.parts_listbox.insert(tk.END, part)

    def show_reservation_screen(self):
        selected_part_index = self.parts_listbox.curselection()
        if not selected_part_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una parte.")
            return

        selected_part = self.parts_listbox.get(selected_part_index)
        self.part_to_reserve = selected_part
        

        self.user_frame.pack_forget()
        self.create_reservation_screen()

    def create_reservation_screen(self):
        self.reservation_frame = tk.Frame(self.frame, bg='lightblue')
        self.reservation_frame.pack(padx=10, pady=10)

        tk.Label(self.reservation_frame, text="Complete con sus datos de contacto y se le avisará al próximo turno disponible", bg='lightblue', wraplength=250).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.reservation_frame, text=f"Parte seleccionada: {self.part_to_reserve}", bg='lightblue').grid(row=1, column=0, columnspan=2)

        tk.Label(self.reservation_frame, text="Nombre:", bg='lightblue').grid(row=2, column=0)
        self.name_entry = tk.Entry(self.reservation_frame, bg='lightgrey')
        self.name_entry.grid(row=2, column=1)

        tk.Label(self.reservation_frame, text="Teléfono:", bg='lightblue').grid(row=3, column=0)
        self.phone_entry = tk.Entry(self.reservation_frame, bg='lightgrey')
        self.phone_entry.grid(row=3, column=1)

        tk.Label(self.reservation_frame, text="Correo:", bg='lightblue').grid(row=4, column=0)
        self.phone_entry = tk.Entry(self.reservation_frame, bg='lightgrey')
        self.phone_entry.grid(row=4, column=1)


        tk.Button(self.reservation_frame, text="Guardar reserva", bg='lightgrey', command=self.save_reservation).grid(row=5, column=0, columnspan=2, pady=10)

    def save_reservation(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        fecha = datetime.now().strftime('%H:%M:%S')
        if not name or not phone:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        reservation_details = f"{self.part_to_reserve} - {name} - {phone} - {fecha}"
        self.reservations.append(reservation_details)

        messagebox.showinfo("Solicitud completada", "Su reserva ha sido registrada con éxito. En breve será contactado para coordinar detalles. Muchas gracias.")
        self.reservation_frame.pack_forget()
        self.show_updated_user_screen()

    def show_updated_user_screen(self):
        self.user_frame = tk.Frame(self.frame, bg='lightblue')
        self.user_frame.pack(padx=10, pady=10)

        #Datos del vehículo actualizado
        tk.Label(self.user_frame, text=f"Bienvenido usuario del vehículo:", bg='lightblue').grid(row=0, column=0, columnspan=2)
        tk.Label(self.user_frame, text=f"Tipo: {self.data_vehiculo['type']}", bg='lightblue').grid(row=1, column=0, columnspan=2)
        tk.Label(self.user_frame, text=f"Marca: {self.data_vehiculo['brand']}", bg='lightblue').grid(row=2, column=0, columnspan=2)
        tk.Label(self.user_frame, text=f"Modelo: {self.data_vehiculo['model']}", bg='lightblue').grid(row=3, column=0, columnspan=2)
        tk.Label(self.user_frame, text=f"Año: {self.data_vehiculo['year']}", bg='lightblue').grid(row=4, column=0, columnspan=2)

        #Lista de reparaciones disponibles actualizada
        self.parts_listbox = tk.Listbox(self.user_frame, bg='lightgrey', width=40)
        self.parts_listbox.grid(row=6, column=0, padx=10, pady=10)
        
        self.update_parts_list()

        tk.Label(self.user_frame, text=f"Reparaciones disponibles",bg='lightblue').grid(row=5, column=0)
        tk.Label(self.user_frame, text=f"Turnos pendientes",bg='lightblue').grid(row=5, column=1)
        tk.Button(self.user_frame, text="Solicitar turno", command=self.show_reservation_screen, bg='lightgrey').grid(row=8, column=0, pady=10)

        #Lista de reservas pendientes actualizada
        self.turnos_lista = tk.Listbox(self.user_frame, bg='lightgrey', width=40)
        self.turnos_lista.grid(row=6, column=1, padx=10, pady=10)
        for reservation in self.reservations:
            self.turnos_lista.insert(tk.END, reservation)
        self.scrollbar_x = tk.Scrollbar(self.user_frame, orient=tk.HORIZONTAL)
        self.turnos_lista.config(xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_x.config(command=self.turnos_lista.xview)
        self.scrollbar_x.grid(row=7, column=1, columnspan=2, sticky="ew")



