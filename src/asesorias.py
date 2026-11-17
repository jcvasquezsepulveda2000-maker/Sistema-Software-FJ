from servicio import Servicio
from excepciones import ErrorServicio


class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesorias especializadas.
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

        self._especialista = (
            " ".join(especialista.split())
            if isinstance(especialista, str) else ""
        )
        self._especialidad = (
            " ".join(especialidad.split())
            if isinstance(especialidad, str) else ""
        )
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
            raise ErrorServicio(
                "El nombre de la asesoria es obligatorio."
            )

        if not self.descripcion:
            raise ErrorServicio(
                "La descripcion de la asesoria es obligatoria."
            )

        if not self._especialista:
            raise ErrorServicio(
                "El nombre del especialista es obligatorio."
            )

        if not self._especialidad:
            raise ErrorServicio(
                "La especialidad es obligatoria."
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
            f"Tipo: Asesoria especializada | "
            f"Especialista: {self._especialista} | "
            f"Especialidad: {self._especialidad} | "
            f"Descripcion: {self.descripcion} | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
