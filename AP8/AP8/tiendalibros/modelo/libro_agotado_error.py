from tiendalibros.modelo.libro_error import LibroError

class LibroAgotadoError(LibroError):

    def __init__(self, libro):
        super().__init__(libro)

    def __str__(self):
        return f"El libro '{self.libro.titulo}' está agotado."
