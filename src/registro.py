
import logging
from pathlib import Path

from excepciones import ErrorRegistro


# Crear automáticamente la carpeta donde se almacenan los registros.
CARPETA_LOGS = Path(__file__).resolve().parent.parent / "logs"
CARPETA_LOGS.mkdir(parents=True, exist_ok=True)

# Definir la ubicación del archivo de registro del sistema.
ARCHIVO_LOG = CARPETA_LOGS / "sistema.log"


class RegistroSistema:
    """
    Gestiona el registro de eventos, advertencias y errores.

    Utiliza el módulo logging de Python para almacenar los mensajes
    del sistema en un archivo de texto con codificación UTF-8.
    """

    def __init__(self):
        """
        Configura el sistema de registro.

        Establece el nivel de registro, evita la propagación de
        mensajes y configura un controlador de archivo para guardar
        los eventos y errores.
        """
        self.logger = logging.getLogger("SistemaGestion")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # Evitar agregar varios controladores al mismo registro.
        if not self.logger.handlers:
            formato = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            manejador = logging.FileHandler(
                ARCHIVO_LOG,
                encoding="utf-8"
            )

            manejador.setFormatter(formato)
            self.logger.addHandler(manejador)

    @staticmethod
    def _validar_mensaje(mensaje):
        """
        Comprueba que el mensaje que se va a registrar sea válido.

        Rechaza valores que no sean texto o que estén vacíos.
        Devuelve el mensaje sin espacios innecesarios al inicio
        o al final.
        """
        if not isinstance(mensaje, str) or not mensaje.strip():
            raise ErrorRegistro(
                "El mensaje del registro debe ser texto y no estar vacio."
            )

        return mensaje.strip()

    def registrar_evento(self, mensaje):
        """
        Registra un evento informativo del sistema.

        Valida el mensaje antes de enviarlo al sistema logging
        con nivel INFO.
        """
        mensaje = self._validar_mensaje(mensaje)
        self.logger.info(mensaje)

    def registrar_error(self, mensaje):
        """
        Registra un error ocurrido durante la ejecución.

        Valida el mensaje antes de almacenarlo con nivel ERROR.
        """
        mensaje = self._validar_mensaje(mensaje)
        self.logger.error(mensaje)

    def registrar_advertencia(self, mensaje):
        """
        Registra una advertencia relacionada con el funcionamiento.

        Valida el mensaje antes de almacenarlo con nivel WARNING.
        """
        mensaje = self._validar_mensaje(mensaje)
        self.logger.warning(mensaje)


# Crear una instancia compartida para utilizarla desde otros módulos.
registro = RegistroSistema()
