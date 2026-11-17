
from abc import ABC, abstractmethod
from entidad import Entidad


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa un servicio general.
    Los servicios específicos heredarán de esta clase.
    """

    def __init__(self, identificador, nombre, descripcion):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ValueError("La descripción del servicio es obligatoria.")

        self._nombre = nombre.strip()
        self._descripcion = descripcion.strip()

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Calcula el costo específico del servicio."""
        pass

    @abstractmethod
    def obtener_informacion(self):
        """Devuelve la información del servicio."""
        pass

    @abstractmethod
    def validar(self):
        """Valida los datos particulares del servicio."""
        pass

    def calcular_costo_con_impuestos(self, duracion, impuesto=0):
        """Calcula el costo aplicando impuestos sin descuento."""
        return self.calcular_costo(
            duracion,
            descuento=0,
            impuesto=impuesto
        )
