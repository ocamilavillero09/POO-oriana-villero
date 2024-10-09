from carro_compra import CarroCompras
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError
from libro import Libro
class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo = []
        self.carro_compras =  CarroCompras()


    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                raise LibroExistenteError(libro)
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo.append(nuevo_libro)
        print(f"El libro '{titulo}' ha sido agregado al catálogo con {existencias} existencias.")


    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, isbn: str, cantidad: int):
        libro = self.buscar_libro_por_isbn(isbn)
        if libro is None:
            print(f"El libro con ISBN {isbn} no está disponible en el catálogo.")
        else:
            if libro.existencias == 0:
                raise LibroAgotadoError(libro)
            try:
                self.carro_compras.agregar_item(libro, cantidad)
                libro.existencias -= cantidad
            except ExistenciasInsuficientesError as e:
                print(e)


    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn: str):
        libro = self.buscar_libro_por_isbn(isbn)
        if libro:
            for item in self.carro_compras.items:
                if item.libro.isbn == isbn:
                    libro.existencias += item.cantidad
                    break
        self.carro_compras.quitar_item(isbn)