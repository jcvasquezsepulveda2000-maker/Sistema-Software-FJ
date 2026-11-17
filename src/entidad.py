from abc import ABC, abstractmethod
from excepciones import ErrorEntidad


class Entidad(ABC):
    """
    Clase abstracta general para las entidades del sistema.
    Sirve como base para Cliente y Servicio.
    """

    def __init__(self, identificador):
        if identificador is None:
            raise ErrorEntidad("El identificador es obligatorio.")

        identificador = str(identificador).strip()

        if not identificador:
            raise ErrorEntidad("El identificador no puede estar vacio.")

        if not identificador.replace("-", "").replace("_", "").isalnum():
            raise ErrorEntidad(
                "El identificador solo puede contener letras, numeros, "
                "guiones y guiones bajos."
            )

        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def validar(self):
        """Cada clase hija debe implementar sus propias validaciones."""
        pass

    @abstractmethod
    def obtener_informacion(self):
        """Cada clase hija debe proporcionar su informacion."""
        pass
