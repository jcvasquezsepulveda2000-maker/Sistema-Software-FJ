
from abc import ABC, abstractmethod
from excepciones import ErrorEntidad


class Entidad(ABC):
    """
    Clase abstracta base para las entidades del sistema.

    Proporciona un identificador común y define los métodos
    que deben implementar las clases derivadas, como Cliente
    y Servicio.
    """

    def __init__(self, identificador):
        """
        Inicializa una entidad con un identificador único.

        Comprueba que el identificador no sea nulo ni esté vacío
        y que contenga únicamente letras, números, guiones
        o guiones bajos.
        """
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
        """Devuelve el identificador de la entidad."""
        return self._identificador

    @abstractmethod
    def validar(self):
        """
        Define el método abstracto para validar una entidad.

        Cada clase derivada debe implementar sus propias reglas
        de validación de acuerdo con sus atributos.
        """
        pass

    @abstractmethod
    def obtener_informacion(self):
        """
        Define el método abstracto para obtener información.

        Cada clase derivada debe implementar la presentación
        de sus propios datos.
        """
        pass
