from tiendalibros.modelo.libro_error import LibroError

class ExistenciasInsuficientesError(LibroError):
    
    def __init__(self, libro, cantidad_solicitada: int):
        super().__init__(libro)
        self.cantidad_solicitada = cantidad_solicitada

    def __str__(self):
        return f"No hay suficientes existencias del libro '{self.libro.titulo}'. Solicitado: {self.cantidad_solicitada}, Disponibles: {self.libro.existencias}."


