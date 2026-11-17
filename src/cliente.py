
import re
from entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente del sistema.
    Aplica encapsulacion y validaciones de datos.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self.__nombre = (
            " ".join(nombre.split()) if isinstance(nombre, str) else ""
        )
        self.__documento = (
            str(documento).strip() if documento is not None else ""
        )
        self.__correo = (
            correo.strip().lower() if isinstance(correo, str) else ""
        )
        self.__telefono = (
            str(telefono).strip() if telefono is not None else ""
        )

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
        # Validar nombre
        if not self.__nombre:
            raise ValueError("El nombre del cliente es obligatorio.")

        if not (2 <= len(self.__nombre) <= 80):
            raise ValueError(
                "El nombre debe tener entre 2 y 80 caracteres."
            )

        if not all(
            caracter.isalpha() or caracter in " -'’"
            for caracter in self.__nombre
        ):
            raise ValueError(
                "El nombre contiene caracteres no permitidos."
            )

        # Validar documento
        if not re.fullmatch(r"[0-9]{5,15}", self.__documento):
            raise ValueError(
                "El documento debe contener entre 5 y 15 digitos."
            )

        # Validar correo
        if not self._correo_valido(self.__correo):
            raise ValueError(
                "El correo electronico no tiene un formato valido."
            )

        # Validar telefono
        if not re.fullmatch(r"\+?[0-9]{7,15}", self.__telefono):
            raise ValueError(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        return True

    @staticmethod
    def _correo_valido(correo):
        patron_correo = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(patron_correo, correo))

    def obtener_informacion(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str):
            raise ValueError("El correo debe ser texto.")

        nuevo_correo = nuevo_correo.strip().lower()

        if not self._correo_valido(nuevo_correo):
            raise ValueError(
                "El nuevo correo no tiene un formato valido."
            )

        self.__correo = nuevo_correo

        return "Correo electronico actualizado correctamente."
