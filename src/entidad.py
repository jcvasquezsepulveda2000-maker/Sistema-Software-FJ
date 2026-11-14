
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta general para las entidades del sistema.
    Sirve como base para Cliente, Servicio y Reserva.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self._identificador = str(identificador)

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def validar(self):
        """
        Cada clase hija debe implementar sus propias validaciones.
        """
        pass

    @abstractmethod
    def obtener_informacion(self):
        """
        Cada clase hija debe proporcionar su información.
        """
        pass
