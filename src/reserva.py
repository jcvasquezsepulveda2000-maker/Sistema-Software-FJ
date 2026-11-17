
import math
from datetime import datetime

from entidad import Entidad
from cliente import Cliente
from servicio import Servicio


class ErrorReserva(Exception):
    """Excepcion personalizada para errores de reservas."""
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
        if not isinstance(self._cliente, Cliente):
            raise ErrorReserva(
                "La reserva necesita un cliente valido."
            )

        if not isinstance(self._servicio, Servicio):
            raise ErrorReserva(
                "La reserva necesita un servicio valido."
            )

        if (
            isinstance(self._duracion, bool)
            or not isinstance(self._duracion, (int, float))
        ):
            raise ErrorReserva(
                "La duracion debe ser un numero valido."
            )

        if not math.isfinite(self._duracion) or self._duracion <= 0:
            raise ErrorReserva(
                "La duracion debe ser un numero finito mayor que cero."
            )

        try:
            self._cliente.validar()
            self._servicio.validar()
        except ValueError as error:
            raise ErrorReserva(
                "El cliente o el servicio contiene datos invalidos."
            ) from error

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
            self.validar()

            total = self._servicio.calcular_costo(
                self._duracion,
                descuento,
                impuesto
            )

        except (ValueError, TypeError) as error:
            raise ErrorReserva(
                "No fue posible calcular el costo de la reserva."
            ) from error

        finally:
            print(
                f"Finalizo el intento de procesamiento "
                f"de la reserva {self.identificador}."
            )

        self._estado = "Procesada"
        return total

    def obtener_informacion(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duracion: {self._duracion} horas | "
            f"Estado: {self._estado} | "
            f"Fecha: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )
