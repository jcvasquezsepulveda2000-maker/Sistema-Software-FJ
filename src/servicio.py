import math
from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import ErrorServicio


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa un servicio general.
    Los servicios especificos heredan de esta clase.
    """

    def __init__(self, identificador, nombre, descripcion):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ErrorServicio("La descripcion del servicio es obligatoria.")

        self._nombre = " ".join(nombre.split())
        self._descripcion = " ".join(descripcion.split())

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @staticmethod
    def validar_numero(valor, nombre, minimo=None, maximo=None,
                       estrictamente_positivo=False):
        """Comprueba que un valor sea numerico, finito y valido."""

        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ErrorServicio(f"{nombre} debe ser un numero valido.")

        try:
            if not math.isfinite(valor):
                raise ErrorServicio(f"{nombre} debe ser un numero finito.")
        except OverflowError as error:
            raise ErrorServicio(
                f"{nombre} esta fuera del rango permitido."
            ) from error

        if estrictamente_positivo and valor <= 0:
            raise ErrorServicio(f"{nombre} debe ser mayor que cero.")

        if minimo is not None and valor < minimo:
            raise ErrorServicio(f"{nombre} no puede ser menor que {minimo}.")

        if maximo is not None and valor > maximo:
            raise ErrorServicio(f"{nombre} no puede superar {maximo}.")

        return valor

    @staticmethod
    def calcular_total(duracion, costo_por_hora, descuento=0, impuesto=0):
        """Calcula el costo final aplicando descuento e impuesto."""

        Servicio.validar_numero(
            duracion, "La duracion", estrictamente_positivo=True
        )
        Servicio.validar_numero(
            costo_por_hora, "El costo por hora",
            estrictamente_positivo=True
        )
        Servicio.validar_numero(
            descuento, "El descuento", minimo=0, maximo=100
        )
        Servicio.validar_numero(
            impuesto, "El impuesto", minimo=0, maximo=100
        )

        subtotal = costo_por_hora * duracion
        total_descuento = subtotal * (1 - descuento / 100)
        total = total_descuento * (1 + impuesto / 100)

        try:
            if not math.isfinite(total):
                raise ErrorServicio(
                    "El resultado del calculo no es finito."
                )

            resultado = round(total, 2)

        except OverflowError as error:
            raise ErrorServicio(
                "El resultado del calculo es demasiado grande."
            ) from error

        return resultado

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Calcula el costo especifico del servicio."""
        pass

    @abstractmethod
    def obtener_informacion(self):
        """Devuelve la informacion del servicio."""
        pass

    @abstractmethod
    def validar(self):
        """Valida los datos particulares del servicio."""
        pass

    def calcular_costo_con_impuestos(self, duracion, impuesto=0):
        """Calcula el costo aplicando impuestos sin descuento."""
        return self.calcular_costo(
            duracion, descuento=0, impuesto=impuesto
        )

    def calcular_costo_con_descuento(self, duracion, descuento=0):
        """Calcula el costo aplicando descuento sin impuestos."""
        return self.calcular_costo(
            duracion, descuento=descuento, impuesto=0
        )
