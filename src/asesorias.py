
from servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesorías especializadas.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        especialista,
        especialidad,
        costo_por_hora
    ):
        super().__init__(identificador, nombre, descripcion)

        self._especialista = especialista.strip() if isinstance(especialista, str) else ""
        self._especialidad = especialidad.strip() if isinstance(especialidad, str) else ""
        self._costo_por_hora = costo_por_hora

        self.validar()

    @property
    def especialista(self):
        return self._especialista

    @property
    def especialidad(self):
        return self._especialidad

    @property
    def costo_por_hora(self):
        return self._costo_por_hora

    def validar(self):
        if not self.nombre:
            raise ValueError("El nombre de la asesoría es obligatorio.")

        if not self.descripcion:
            raise ValueError("La descripción de la asesoría es obligatoria.")

        if not self._especialista:
            raise ValueError("El nombre del especialista es obligatorio.")

        if not self._especialidad:
            raise ValueError("La especialidad es obligatoria.")

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
        total = subtotal - valor_descuento

        return round(total * (1 + impuesto / 100), 2)

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Asesoría especializada | "
            f"Especialista: {self._especialista} | "
            f"Especialidad: {self._especialidad} | "
            f"Descripción: {self.descripcion} | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
