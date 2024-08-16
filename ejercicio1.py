class Libro: 
    def __init__(self, titulo, autor, isbn, numeroDePag,genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.__numeroDePag = numeroDePag
        self.genero = genero

    def getNumeroPag(self):
        print("El libro es: " + self.__numeroDePag)

    def prestar(self):
        print("El libro ha sido prestado")
        return True
    
    def devolver(self):
        print("El libro ha sido devuelto")
        return True
    
    def buscarPorTitulo(self, titulo):
        if self.titulo == titulo:
            return True
        else:
            return False
        

class LibroInfantil(Libro):
    def __init__(self, titulo, autor, isbn, numeroDePag, genero, edadMinima):
        super().__init__(titulo, autor, isbn, numeroDePag, genero)
        self.edadMinima = edadMinima


class Autor:
    def __init__(self, nombre, nacionalidad,fechaDeNacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fechadenacimiento = fechaDeNacimiento

    def publicarLibro(self, titulo, autor, isbn, numeroDePag, genero):
        libro = Libro(titulo, autor, isbn, numeroDePag, genero)
        return libro
    
class Lector:
    def __init__(self, nombre, edad, direccion, numeroDeSocio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numeroDeSocio = numeroDeSocio

    def prestarLibro(self, libro):
        if libro.prestar():
            return True
        else:
            return False

    def devolverLibro(self, libro):
        if libro.devolver():
            return True
        else:
            return False


class Libreria:

    def __init__(self, libros,autores, lectores):
        self.libros = libros
        self.autores = autores
        self.lectores = lectores

    lectores = []
    libros = []

    

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def buscarLibro(self, titulo):
        for libro in self.libros:
            if libro.buscarPorTitulo(titulo):
                return libro
        return None
    
    def prestarLibro(self, libro, lector):
        if lector.prestarLibro(libro):
            return True
        else:
            return False
        
    def devolverLibro(self, libro, lector):
        if lector.devolverLibro(libro):
            return True
        else:
            return False
        
    def registrarLector(self, lector):
        self.lectores.append(lector)


