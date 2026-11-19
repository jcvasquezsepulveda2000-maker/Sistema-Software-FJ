
import math
from datetime import datetime

from entidad import Entidad
from cliente import Cliente
from servicio import Servicio
from excepciones import ErrorSistema, ErrorReserva


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente para utilizar
    un servicio durante un período determinado.

    Administra los datos del cliente, el servicio, la duración,
    el estado y la fecha de creación de la reserva.
    """

    # Estados permitidos durante el ciclo de vida de una reserva.
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
        """
        Inicializa una reserva con sus datos principales.

        Establece el estado inicial como Pendiente, registra
        la fecha de creación y valida los datos recibidos.
        """
        super().__init__(identificador)

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._fecha_creacion = datetime.now()

        self.validar()

    @property
    def cliente(self):
        """Devuelve el cliente asociado a la reserva."""
        return self._cliente

    @property
    def servicio(self):
        """Devuelve el servicio asociado a la reserva."""
        return self._servicio

    @property
    def duracion(self):
        """Devuelve la duración contratada para la reserva."""
        return self._duracion

    @property
    def estado(self):
        """Devuelve el estado actual de la reserva."""
        return self._estado

    @property
    def fecha_creacion(self):
        """Devuelve la fecha y hora en que se creó la reserva."""
        return self._fecha_creacion

    def validar(self):
        """
        Comprueba que la información de la reserva sea válida.

        Verifica que exista un cliente y un servicio del tipo
        correspondiente, que la duración sea positiva y finita,
        y que los datos del cliente y del servicio sean válidos.

        Encadena los errores originales para conservar su causa.
        """
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

        try:
            if (
                not math.isfinite(self._duracion)
                or self._duracion <= 0
            ):
                raise ErrorReserva(
                    "La duracion debe ser un numero finito "
                    "mayor que cero."
                )

        except OverflowError as error:
            raise ErrorReserva(
                "La duracion supera el limite numerico permitido."
            ) from error

        try:
            self._cliente.validar()
            self._servicio.validar()

        except ErrorSistema as error:
            raise ErrorReserva(
                "El cliente o el servicio contiene datos invalidos."
            ) from error

        return True

    def confirmar(self):
        """
        Confirma una reserva que se encuentre pendiente.

        Cambia el estado a Confirmada. No permite confirmar
        reservas que ya tengan otro estado.
        """
        if self._estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"

        return "Reserva confirmada correctamente."

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.

        Actualiza el estado a Cancelada y rechaza la cancelación
        de reservas procesadas o que ya estén canceladas.
        """
        if self._estado not in ("Pendiente", "Confirmada"):
            raise ErrorReserva(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self._estado = "Cancelada"

        return "Reserva cancelada correctamente."

    def procesar(self, descuento=0, impuesto=0):
        """
        Procesa una reserva confirmada y calcula su costo final.

        Valida nuevamente los datos, calcula el costo del servicio
        aplicando los porcentajes opcionales de descuento e impuesto
        y actualiza el estado a Procesada cuando la operación termina
        correctamente.

        Captura y encadena los errores del cálculo. El bloque finally
        informa que el intento de procesamiento ha finalizado.
        """
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

        except (ErrorSistema, ValueError, TypeError, OverflowError) as error:
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
        """
        Devuelve un resumen de la reserva en formato de texto.

        Incluye el identificador, el cliente, el servicio,
        la duración, el estado y la fecha de creación.
        """
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duracion: {self._duracion} horas | "
            f"Estado: {self._estado} | "
            f"Fecha: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )
