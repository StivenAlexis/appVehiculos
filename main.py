import tkinter as tk
from modulo import AppVehiculos

def main():
    root = tk.Tk()
    app = AppVehiculos(root)
    root.mainloop()


if __name__ == "__main__":
    main()