
from servicio import Servicio
from excepciones import ErrorServicio, ErrorDisponibilidad


class AlquilerEquipo(Servicio):
    """
    Representa un servicio de alquiler de equipos por horas.

    Hereda de Servicio y administra la cantidad de equipos
    disponibles, el costo por hora y las operaciones de alquiler.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        cantidad_disponible,
        costo_por_hora
    ):
        """
        Inicializa el servicio de alquiler de equipos.

        Recibe los datos generales del servicio, la cantidad
        disponible y el costo correspondiente a cada hora.
        """
        super().__init__(identificador, nombre, descripcion)

        self._cantidad_disponible = cantidad_disponible
        self._costo_por_hora = costo_por_hora

        self.validar()

    @property
    def cantidad_disponible(self):
        """Devuelve la cantidad actual de equipos disponibles."""
        return self._cantidad_disponible

    @property
    def costo_por_hora(self):
        """Devuelve el costo establecido por cada hora de alquiler."""
        return self._costo_por_hora

    def validar(self):
        """
        Comprueba que los datos del servicio sean correctos.

        Verifica el nombre, la descripción, la cantidad disponible
        y que el costo por hora sea un número positivo.
        """
        if not self.nombre:
            raise ErrorServicio("El nombre del equipo es obligatorio.")

        if not self.descripcion:
            raise ErrorServicio("La descripcion del equipo es obligatoria.")

        if (
            isinstance(self._cantidad_disponible, bool)
            or not isinstance(self._cantidad_disponible, int)
            or self._cantidad_disponible < 0
        ):
            raise ErrorServicio(
                "La cantidad disponible debe ser un entero no negativo."
            )

        Servicio.validar_numero(
            self._costo_por_hora,
            "El costo por hora",
            estrictamente_positivo=True
        )

        return True

    def verificar_disponibilidad(self, cantidad_solicitada):
        """
        Comprueba si existe suficiente cantidad de equipos.

        Valida que la cantidad solicitada sea un entero positivo
        y la compara con las unidades disponibles.

        Devuelve True si hay disponibilidad y False en caso contrario.
        """
        if (
            isinstance(cantidad_solicitada, bool)
            or not isinstance(cantidad_solicitada, int)
            or cantidad_solicitada <= 0
        ):
            raise ErrorServicio(
                "La cantidad solicitada debe ser un entero positivo."
            )

        return cantidad_solicitada <= self._cantidad_disponible

    def alquilar(self, cantidad_solicitada):
        """
        Realiza el alquiler y actualiza las unidades disponibles.

        Si no existe suficiente inventario, genera una excepción
        de disponibilidad. Si el alquiler es posible, descuenta
        las unidades solicitadas.
        """
        if not self.verificar_disponibilidad(cantidad_solicitada):
            raise ErrorDisponibilidad(
                "No hay suficientes equipos disponibles."
            )

        self._cantidad_disponible -= cantidad_solicitada

        return (
            f"Alquiler realizado. Equipos alquilados: {cantidad_solicitada}. "
            f"Disponibles: {self._cantidad_disponible}."
        )

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """
        Calcula el costo total del alquiler.

        Utiliza la duración, el costo por hora y los porcentajes
        opcionales de descuento e impuesto.
        """
        return Servicio.calcular_total(
            duracion,
            self._costo_por_hora,
            descuento,
            impuesto
        )

    def obtener_informacion(self):
        """
        Devuelve una descripción del servicio de alquiler.

        Incluye el nombre, tipo de servicio, descripción,
        cantidad disponible y costo por hora.
        """
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Alquiler de equipos | "
            f"Descripcion: {self.descripcion} | "
            f"Cantidad disponible: {self._cantidad_disponible} | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
