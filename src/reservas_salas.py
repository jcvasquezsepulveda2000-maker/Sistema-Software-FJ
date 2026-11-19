
from servicio import Servicio
from excepciones import ErrorServicio


class ReservaSala(Servicio):
    """
    Representa un servicio de reserva de salas por horas.

    Administra la capacidad de la sala y su costo por hora.
    Hereda de Servicio y proporciona validaciones y métodos
    específicos para este tipo de servicio.
    """

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        capacidad,
        costo_por_hora
    ):
        """
        Inicializa un servicio de reserva de sala.

        Recibe el identificador, nombre, descripción, capacidad
        y costo por hora. Después de asignar los atributos,
        ejecuta las validaciones correspondientes.
        """
        super().__init__(identificador, nombre, descripcion)

        self._capacidad = capacidad
        self._costo_por_hora = costo_por_hora

        self.validar()

    @property
    def capacidad(self):
        """Devuelve la capacidad máxima de personas de la sala."""
        return self._capacidad

    @property
    def costo_por_hora(self):
        """Devuelve el costo establecido por cada hora de uso."""
        return self._costo_por_hora

    def validar(self):
        """
        Comprueba que los datos particulares de la sala sean válidos.

        Verifica que el nombre y la descripción sean obligatorios,
        que la capacidad sea un entero positivo y que el costo
        por hora sea un número estrictamente mayor que cero.
        """
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
        """
        Calcula el costo de reservar la sala.

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
        Devuelve la información completa del servicio de sala.

        Incluye el nombre, tipo de servicio, descripción,
        capacidad máxima y costo por hora.
        """
        return (
            f"Servicio: {self.nombre} | "
            f"Tipo: Reserva de sala | "
            f"Descripcion: {self.descripcion} | "
            f"Capacidad: {self._capacidad} personas | "
            f"Costo por hora: ${self._costo_por_hora:,.2f}"
        )
