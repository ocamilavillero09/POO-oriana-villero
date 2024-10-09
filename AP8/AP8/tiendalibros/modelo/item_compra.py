class ItemCompra:
    def __init__(self, libro, cantidad: int):
        self.libro = libro
        self.cantidad = cantidad

    def __str__(self):
        return "{} x{} - Subtotal: ${:,.2f}".format(self.libro, self.cantidad, self.libro.precio * self.cantidad)
