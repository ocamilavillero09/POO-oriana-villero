from existencias_insuficientes_error import ExistenciasInsuficientesError
from item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, libro, cantidad: int):
        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro, cantidad)

        for item in self.items:
            if item.libro.isbn == libro.isbn:
                if libro.existencias < item.cantidad + cantidad:
                    raise ExistenciasInsuficientesError(libro, item.cantidad + cantidad)
                item.cantidad += cantidad
                print(f"Se han actualizado {cantidad} ejemplares de '{libro.titulo}' en el carrito.")
                return

        self.items.append(ItemCompra(libro, cantidad))
        print(f"Se han agregado {cantidad} ejemplares de '{libro.titulo}' al carrito.")

    def quitar_item(self, isbn: str):
        for item in self.items:
            if item.libro.isbn == isbn:
                self.items.remove(item)
                print(f"El libro '{item.libro.titulo}' ha sido eliminado del carrito.")
                return
        print("El libro no está en el carrito.")

    def calcular_total(self):
        total = 0
        print("Detalle de la compra:")
        for item in self.items:
            subtotal = item.libro.precio * item.cantidad
            total += subtotal
            print(item)
        print(f"Total de la compra: ${total:,.2f}")
        return total