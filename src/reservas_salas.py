
from servicio import Servicio


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
            raise ValueError("El nombre de la sala es obligatorio.")

        if not self.descripcion:
            raise ValueError("La descripción de la sala es obligatoria.")

        if not isinstance(self._capacidad, int) or self._capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero mayor que cero.")

        if (
            isinstance(self._costo_por_hora, bool)
            or not isinstance(self._costo_por_hora, (int, float))
            or self._costo_por_hora <= 0
        ):
            raise ValueError("El costo por hora debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        if not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        subtotal = self._costo_por_hora * duracion
        valor_descuento = subtotal * (descuento / 100)
        total_con_descuento = subtotal - valor_descuento

        return round(
            total_con_descuento * (1 + impuesto / 100),
            2
        )

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Reserva de sala | "
            f"Descripción: {self.descripcion} | "
            f"Capacidad: {self._capacidad} personas | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
