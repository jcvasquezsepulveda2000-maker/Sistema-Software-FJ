
from servicio import Servicio
from excepciones import ErrorServicio


class AsesoriaEspecializada(Servicio):
    """
    Representa un servicio de asesoría especializada.

    Administra la información del especialista, su área de
    especialidad y el costo por hora de la asesoría.
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
        """
        Inicializa una asesoría especializada.

        Recibe los datos generales del servicio, el nombre del
        especialista, su especialidad y el costo por hora.
        Normaliza los espacios de los textos recibidos.
        """
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
        """Devuelve el nombre del especialista responsable."""
        return self._especialista

    @property
    def especialidad(self):
        """Devuelve el área de especialidad de la asesoría."""
        return self._especialidad

    @property
    def costo_por_hora(self):
        """Devuelve el costo establecido por cada hora de asesoría."""
        return self._costo_por_hora

    def validar(self):
        """
        Comprueba que los datos de la asesoría sean correctos.

        Verifica que el nombre, la descripción, el especialista
        y la especialidad sean obligatorios. También comprueba
        que el costo por hora sea un número positivo.
        """
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
        """
        Calcula el costo total de la asesoría.

        Utiliza la duración, el costo por hora y los porcentajes
        opcionales de descuento e impuesto mediante el método
        general de cálculo de la clase Servicio.
        """
        return Servicio.calcular_total(
            duracion,
            self._costo_por_hora,
            descuento,
            impuesto
        )

    def obtener_informacion(self):
        """
        Devuelve la información completa de la asesoría.

        Incluye el nombre del servicio, el especialista,
        su especialidad, la descripción y el costo por hora.
        """
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Asesoria especializada | "
            f"Especialista: {self._especialista} | "
            f"Especialidad: {self._especialidad} | "
            f"Descripcion: {self.descripcion} | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
