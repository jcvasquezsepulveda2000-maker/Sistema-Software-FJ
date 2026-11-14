
from datetime import datetime
from entidad import Entidad


class ErrorReserva(Exception):
    """Excepción personalizada para errores de reservas."""
    pass


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio.
    """

    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Procesada"
    )

    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion
    ):
        super().__init__(identificador)

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._fecha_creacion = datetime.now()

        self.validar()

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    def validar(self):
        if self._cliente is None:
            raise ErrorReserva("La reserva necesita un cliente.")

        if self._servicio is None:
            raise ErrorReserva("La reserva necesita un servicio.")

        if (
            isinstance(self._duracion, bool)
            or not isinstance(self._duracion, (int, float))
            or self._duracion <= 0
        ):
            raise ErrorReserva("La duración debe ser mayor que cero.")

        if not hasattr(self._cliente, "obtener_informacion"):
            raise ErrorReserva("El cliente no es válido.")

        if not hasattr(self._servicio, "calcular_costo"):
            raise ErrorReserva("El servicio no es válido.")

        return True

    def confirmar(self):
        if self._estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"

        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self._estado not in ("Pendiente", "Confirmada"):
            raise ErrorReserva(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self._estado = "Cancelada"

        return "Reserva cancelada correctamente."

    def procesar(self, descuento=0, impuesto=0):
        if self._estado != "Confirmada":
            raise ErrorReserva(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            total = self._servicio.calcular_costo(
                self._duracion,
                descuento,
                impuesto
            )

        except ValueError as error:
            raise ErrorReserva(
                "No fue posible calcular el costo de la reserva."
            ) from error

        else:
            self._estado = "Procesada"
            return total

        finally:
            print(
                f"Finalizó el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )

    def obtener_informacion(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duración: {self._duracion} horas | "
            f"Estado: {self._estado} | "
            f"Fecha: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )
