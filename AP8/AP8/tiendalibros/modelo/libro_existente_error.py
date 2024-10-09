from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    # Defina metodo inicializador
    def __init__(self, libro):
            super().__init__(libro)
    

    # Defina metodo especial
    def __str__(self):
        return f"El libro con ISBN {self.libro.isbn} ya existe en el catálogo."

