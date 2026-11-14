
import re
from entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente del sistema.
    Aplica encapsulación y validaciones de datos.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre.strip() if isinstance(nombre, str) else ""
        self.__documento = str(documento).strip()
        self.__correo = correo.strip().lower() if isinstance(correo, str) else ""
        self.__telefono = str(telefono).strip()

        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        if not self.__nombre:
            raise ValueError("El nombre del cliente es obligatorio.")

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]{2,80}", self.__nombre):
            raise ValueError("El nombre contiene caracteres no permitidos.")

        if not re.fullmatch(r"\d{5,15}", self.__documento):
            raise ValueError("El documento debe contener entre 5 y 15 dígitos.")

        patron_correo = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"
        if not re.fullmatch(patron_correo, self.__correo):
            raise ValueError("El correo electrónico no tiene un formato válido.")

        if not re.fullmatch(r"\+?\d{7,15}", self.__telefono):
            raise ValueError("El teléfono debe contener entre 7 y 15 dígitos.")

        return True

    def obtener_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str):
            raise ValueError("El correo debe ser texto.")

        nuevo_correo = nuevo_correo.strip().lower()

        if not re.fullmatch(r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$", nuevo_correo):
            raise ValueError("El nuevo correo no tiene un formato válido.")

        self.__correo = nuevo_correo
        return "Correo electrónico actualizado correctamente."
