
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta general para las entidades del sistema.
    Sirve como base para Cliente y Servicio.
    """

    def __init__(self, identificador):
        if identificador is None:
            raise ValueError("El identificador es obligatorio.")

        identificador = str(identificador).strip()

        if not identificador:
            raise ValueError("El identificador no puede estar vacío.")

        if not identificador.replace("-", "").replace("_", "").isalnum():
            raise ValueError(
                "El identificador solo puede contener letras, números, "
                "guiones y guiones bajos."
            )

        self._identificador = identificador

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
