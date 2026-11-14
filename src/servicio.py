
from abc import abstractmethod
from entidad import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio general.
    Los servicios específicos heredarán de esta clase.
    """

    def __init__(self, identificador, nombre, descripcion):
        super().__init__(identificador)

        self._nombre = nombre.strip() if isinstance(nombre, str) else ""
        self._descripcion = descripcion.strip() if isinstance(descripcion, str) else ""

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """
        Calcula el costo del servicio.
        Cada servicio específico implementará su propia fórmula.
        """
        pass

    @abstractmethod
    def obtener_informacion(self):
        """
        Devuelve la información del servicio.
        """
        pass

    @abstractmethod
    def validar(self):
        """
        Valida los datos particulares del servicio.
        """
        pass

    def calcular_costo_con_impuestos(self, duracion, impuesto=0):
        """
        Variante de cálculo que permite aplicar impuestos.
        """
        return self.calcular_costo(
            duracion,
            descuento=0,
            impuesto=impuesto
        )
