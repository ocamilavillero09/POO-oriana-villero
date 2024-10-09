import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")

        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print(f"Libro con ISBN {isbn} retirado del carrito.")
        except ValueError as e:
            print(f"Error: {e}")

    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
        cantidad = int(input("Ingrese la cantidad que desea agregar: "))

        try:
            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
            print(f"{cantidad} ejemplares del libro con ISBN {isbn} agregados al carrito.")
        except ValueError as e:
            print(e)
        except LibroAgotadoError as e:
            print(e)
        except ExistenciasInsuficientesError as e:
            print(e)

        
    # Defina el metodo adicionar_un_libro_a_catalogo
    
    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese la cantidad de existencias: "))

        try:
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"Libro '{titulo}' agregado correctamente al catálogo.")
        except LibroExistenteError as e:
            print(e)
