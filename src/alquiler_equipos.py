
from servicio import Servicio


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
            raise ValueError("El nombre del equipo es obligatorio.")

        if not self.descripcion:
            raise ValueError("La descripción del equipo es obligatoria.")

        if (
            isinstance(self._cantidad_disponible, bool)
            or not isinstance(self._cantidad_disponible, int)
            or self._cantidad_disponible < 0
        ):
            raise ValueError("La cantidad disponible debe ser un entero no negativo.")

        if (
            isinstance(self._costo_por_hora, bool)
            or not isinstance(self._costo_por_hora, (int, float))
            or self._costo_por_hora <= 0
        ):
            raise ValueError("El costo por hora debe ser mayor que cero.")

        return True

    def verificar_disponibilidad(self, cantidad_solicitada):
        if (
            isinstance(cantidad_solicitada, bool)
            or not isinstance(cantidad_solicitada, int)
            or cantidad_solicitada <= 0
        ):
            raise ValueError("La cantidad solicitada debe ser un entero positivo.")

        return cantidad_solicitada <= self._cantidad_disponible

    def alquilar(self, cantidad_solicitada):
        if not self.verificar_disponibilidad(cantidad_solicitada):
            raise ValueError("No hay suficientes equipos disponibles.")

        self._cantidad_disponible -= cantidad_solicitada

        return (
            f"Alquiler realizado. Equipos alquilados: {cantidad_solicitada}. "
            f"Disponibles: {self._cantidad_disponible}."
        )

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
        total = subtotal - valor_descuento

        return round(total * (1 + impuesto / 100), 2)

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Alquiler de equipos | "
            f"Descripción: {self.descripcion} | "
            f"Cantidad disponible: {self._cantidad_disponible} | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
