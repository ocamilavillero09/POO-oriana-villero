# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod
from .errores import (
    NoCumpleLongitudMinimaError, 
    NoTieneLetraMayusculaError, 
    NoTieneLetraMinusculaError, 
    NoTieneNumeroError, 
    NoTieneCaracterEspecialError, 
    NoTienePalabraSecretaError
)


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)  # Longitud mínima de 8 caracteres

    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = "@_#$%"
        return any(c in especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no tiene la longitud suficiente.")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula.")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número.")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un carácter especial.")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)  # Longitud mínima de 6 caracteres

    def contiene_calisto(self, clave: str) -> bool:
        index = clave.lower().find("calisto")
        if index == -1:
            return False
        subcadena = clave[index:index + 7]
        mayusculas = sum(1 for c in subcadena if c.isupper())
        return 2 <= mayusculas < 7

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave no tiene la longitud suficiente.")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número.")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La palabra 'calisto' no está correctamente formada.")
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

