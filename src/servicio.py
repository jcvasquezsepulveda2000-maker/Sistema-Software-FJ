
import math
from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import ErrorServicio


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa un servicio general del sistema.

    Hereda de Entidad y establece los atributos y métodos comunes
    que deben implementar los servicios especializados, como
    reservas de salas, alquiler de equipos y asesorías.
    """

    def __init__(self, identificador, nombre, descripcion):
        """
        Inicializa un servicio con su identificador, nombre y descripción.

        Comprueba que el nombre y la descripción sean textos válidos
        y normaliza los espacios innecesarios.
        """
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if not isinstance(descripcion, str) or not descripcion.strip():
            raise ErrorServicio("La descripcion del servicio es obligatoria.")

        self._nombre = " ".join(nombre.split())
        self._descripcion = " ".join(descripcion.split())

    @property
    def nombre(self):
        """Devuelve el nombre del servicio."""
        return self._nombre

    @property
    def descripcion(self):
        """Devuelve la descripción del servicio."""
        return self._descripcion

    @staticmethod
    def validar_numero(valor, nombre, minimo=None, maximo=None,
                       estrictamente_positivo=False):
        """
        Valida un valor numérico utilizado en las operaciones del sistema.

        Comprueba que el valor sea numérico, finito y que respete
        los límites mínimo, máximo o de positividad establecidos.

        No acepta valores booleanos como números. Si ocurre un
        desbordamiento numérico, genera una excepción personalizada
        conservando la causa original.
        """
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
        """
        Calcula el costo final de un servicio.

        Valida la duración, el costo por hora, el porcentaje de
        descuento y el porcentaje de impuesto. Calcula el subtotal,
        aplica primero el descuento y después el impuesto.

        Devuelve el resultado redondeado a dos decimales.
        """
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
        """
        Define el cálculo de costo que debe implementar cada servicio.

        Permite que las clases derivadas apliquen sus propias reglas
        de cálculo utilizando la duración, el descuento y el impuesto.
        """
        pass

    @abstractmethod
    def obtener_informacion(self):
        """
        Define la presentación de información de cada servicio.

        Cada clase especializada debe proporcionar los datos
        correspondientes a su tipo de servicio.
        """
        pass

    @abstractmethod
    def validar(self):
        """
        Define las validaciones particulares de cada servicio.

        Obliga a las clases derivadas a comprobar sus atributos
        específicos antes de utilizar el servicio.
        """
        pass

    def calcular_costo_con_impuestos(self, duracion, impuesto=0):
        """
        Calcula el costo del servicio aplicando únicamente impuestos.

        Establece el descuento en cero y delega el cálculo
        al método calcular_costo implementado por la clase derivada.
        """
        return self.calcular_costo(
            duracion, descuento=0, impuesto=impuesto
        )

    def calcular_costo_con_descuento(self, duracion, descuento=0):
        """
        Calcula el costo del servicio aplicando únicamente descuentos.

        Establece el impuesto en cero y delega el cálculo
        al método calcular_costo implementado por la clase derivada.
        """
        return self.calcular_costo(
            duracion, descuento=descuento, impuesto=0
        )
