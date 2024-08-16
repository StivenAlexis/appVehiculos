import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Autos')
ventana.geometry('400x200')

# Crear y colocar un título
titulo = tk.Label(ventana, text="Mantenimiento de automotor", font=("Calibri", 16))
titulo.pack()

# Crear y colocar un campo de entrada
ingreso_tarea = tk.Entry(ventana)
ingreso_tarea.pack()

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = ingreso_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        ingreso_tarea.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar la tarea

# Crear y colocar un botón para agregar la tarea
boton_agregar = tk.Button(ventana, text='Agregar tarea', command=agregar_tarea)
boton_agregar.pack()

# Función para eliminar la tarea seleccionada de la lista
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)

# Crear y colocar un botón para eliminar la tarea seleccionada
boton_eliminar = tk.Button(ventana, text='Eliminar tarea', command=eliminar_tarea)
boton_eliminar.pack()

# Crear y colocar una lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
