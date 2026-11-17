from servicio import Servicio
from excepciones import ErrorServicio, ErrorDisponibilidad


class AlquilerEquipo(Servicio):
    """
    Servicio para alquilar equipos por horas.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        cantidad_disponible,
        costo_por_hora
    ):
        super().__init__(identificador, nombre, descripcion)

        self._cantidad_disponible = cantidad_disponible
        self._costo_por_hora = costo_por_hora

        self.validar()

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @property
    def costo_por_hora(self):
        return self._costo_por_hora

    def validar(self):
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
        return Servicio.calcular_total(
            duracion,
            self._costo_por_hora,
            descuento,
            impuesto
        )

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Alquiler de equipos | "
            f"Descripcion: {self.descripcion} | "
            f"Cantidad disponible: {self._cantidad_disponible} | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
