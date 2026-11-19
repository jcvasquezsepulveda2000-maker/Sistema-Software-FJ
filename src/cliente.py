
import re
from entidad import Entidad
from excepciones import ErrorCliente


class Cliente(Entidad):
    """
    Representa un cliente registrado en el sistema.

    Hereda de Entidad y aplica encapsulación mediante atributos
    privados. Valida los datos personales y permite actualizar
    la dirección de correo electrónico.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):
        """
        Inicializa un cliente con sus datos personales.

        Normaliza los espacios del nombre, convierte el documento
        y el teléfono a texto y almacena el correo en minúsculas.
        Finalmente, ejecuta las validaciones correspondientes.
        """
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
        """Permite consultar el nombre del cliente."""
        return self.__nombre

    @property
    def documento(self):
        """Permite consultar el documento de identificación."""
        return self.__documento

    @property
    def correo(self):
        """Permite consultar el correo electrónico del cliente."""
        return self.__correo

    @property
    def telefono(self):
        """Permite consultar el número de teléfono del cliente."""
        return self.__telefono

    def validar(self):
        """
        Comprueba que los datos personales del cliente sean válidos.

        Verifica la longitud y los caracteres del nombre, el formato
        del documento, la estructura del correo electrónico y la
        longitud y composición del número telefónico.
        """
        if not self.__nombre:
            raise ErrorCliente("El nombre del cliente es obligatorio.")

        if not (2 <= len(self.__nombre) <= 80):
            raise ErrorCliente(
                "El nombre debe tener entre 2 y 80 caracteres."
            )

        if not all(
            caracter.isalpha() or caracter in " -'"
            for caracter in self.__nombre
        ):
            raise ErrorCliente(
                "El nombre contiene caracteres no permitidos."
            )

        if not re.fullmatch(r"[0-9]{5,15}", self.__documento):
            raise ErrorCliente(
                "El documento debe contener entre 5 y 15 digitos."
            )

        if not self._correo_valido(self.__correo):
            raise ErrorCliente(
                "El correo electronico no tiene un formato valido."
            )

        if not re.fullmatch(r"\+?[0-9]{7,15}", self.__telefono):
            raise ErrorCliente(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        return True

    @staticmethod
    def _correo_valido(correo):
        """
        Comprueba si una dirección de correo tiene un formato válido.

        Utiliza una expresión regular para verificar la estructura
        básica de la dirección electrónica.
        """
        patron_correo = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(patron_correo, correo))

    def obtener_informacion(self):
        """
        Devuelve los datos principales del cliente en formato de texto.

        Incluye nombre, documento, correo electrónico y teléfono.
        """
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )

    def actualizar_correo(self, nuevo_correo):
        """
        Actualiza el correo electrónico del cliente.

        Comprueba que el nuevo valor sea texto y tenga un formato
        válido antes de modificar el atributo privado.
        """
        if not isinstance(nuevo_correo, str):
            raise ErrorCliente("El correo debe ser texto.")

        nuevo_correo = nuevo_correo.strip().lower()

        if not self._correo_valido(nuevo_correo):
            raise ErrorCliente(
                "El nuevo correo no tiene un formato valido."
            )

        self.__correo = nuevo_correo

        return "Correo electronico actualizado correctamente."
