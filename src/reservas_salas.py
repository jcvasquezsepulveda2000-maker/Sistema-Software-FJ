from servicio import Servicio
from excepciones import ErrorServicio


class ReservaSala(Servicio):
    """
    Servicio de reserva de salas por horas.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        capacidad,
        costo_por_hora
    ):
        super().__init__(identificador, nombre, descripcion)

        self._capacidad = capacidad
        self._costo_por_hora = costo_por_hora

        self.validar()

    @property
    def capacidad(self):
        return self._capacidad

    @property
    def costo_por_hora(self):
        return self._costo_por_hora

    def validar(self):
        if not self.nombre:
            raise ErrorServicio("El nombre de la sala es obligatorio.")

        if not self.descripcion:
            raise ErrorServicio("La descripcion de la sala es obligatoria.")

        if (
            isinstance(self._capacidad, bool)
            or not isinstance(self._capacidad, int)
            or self._capacidad <= 0
        ):
            raise ErrorServicio(
                "La capacidad debe ser un entero mayor que cero."
            )

        Servicio.validar_numero(
            self._costo_por_hora,
            "El costo por hora",
            estrictamente_positivo=True
        )

        return True

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
            f"Tipo: Reserva de sala | "
            f"Descripcion: {self.descripcion} | "
            f"Capacidad: {self._capacidad} personas | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
