
import logging
from pathlib import Path


# Crear automáticamente la carpeta de registros
CARPETA_LOGS = Path(__file__).resolve().parent.parent / "logs"
CARPETA_LOGS.mkdir(parents=True, exist_ok=True)

ARCHIVO_LOG = CARPETA_LOGS / "sistema.log"


class RegistroSistema:
    """
    Registra los eventos y errores del sistema
    en un archivo de texto.
    """

    def __init__(self):
        self.logger = logging.getLogger("SistemaGestion")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # Evitar agregar varios controladores al mismo registro
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

    def registrar_evento(self, mensaje):
        self.logger.info(mensaje)

    def registrar_error(self, mensaje):
        self.logger.error(mensaje)

    def registrar_advertencia(self, mensaje):
        self.logger.warning(mensaje)


# Instancia compartida para utilizar en los módulos
registro = RegistroSistema()
