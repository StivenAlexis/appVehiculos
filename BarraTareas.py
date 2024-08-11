import tkinter as tk
from datetime import datetime

ventana = tk.Tk()
ventana.title('Lista de tareas')
ventana.geometry('500x400')

tareas = {}

tk.Label(ventana, text="Detalles de la reparación:").pack()
detalles_reparacion = tk.Text(ventana, height=4, width=50)
detalles_reparacion.pack()

tk.Label(ventana, text="Tareas realizadas:").pack()
lista_tareas = tk.Listbox(ventana, width=50)
lista_tareas.pack()

tk.Label(ventana, text="Hora de carga:").pack()
hora_carga = tk.Entry(ventana)
hora_carga.pack()

def agregar_tarea():
    tarea = ingreso_tarea.get()
    descripcion = detalles_reparacion.get("1.0", tk.END).strip()
    if tarea:
        hora_carga_actual = datetime.now().strftime('%H:%M:%S')
        tareas[tarea] = {"descripcion": descripcion, "hora": hora_carga_actual}
        lista_tareas.insert(tk.END, f"{tarea} - {hora_carga_actual}")
        hora_carga.delete(0, tk.END)
        hora_carga.insert(0, hora_carga_actual)
        ingreso_tarea.delete(0, tk.END)
        detalles_reparacion.delete("1.0", tk.END)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea = lista_tareas.get(seleccion).split(" - ")[0]
        del tareas[tarea]
        lista_tareas.delete(seleccion)

tk.Label(ventana, text="Nueva tarea:").pack()
ingreso_tarea = tk.Entry(ventana, width=50)
ingreso_tarea.pack()

boton_agregar = tk.Button(ventana, text='Agregar tarea', command=agregar_tarea)
boton_agregar.pack()

boton_eliminar = tk.Button(ventana, text='Eliminar tarea', command=eliminar_tarea)
boton_eliminar.pack()

ventana.mainloop()

#no se como hacer que se guarde con una descrpcion 