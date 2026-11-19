
"""
Jerarquía de excepciones personalizadas del Sistema de Gestión
de Servicios.

Centraliza los errores propios de la aplicación para facilitar
su identificación, captura, tratamiento y registro.
"""


class ErrorSistema(Exception):
    """
    Excepción base de todos los errores personalizados.

    Permite capturar de forma general los errores propios
    del sistema mediante una única clase.
    """
    pass


class ErrorEntidad(ErrorSistema):
    """Representa errores relacionados con entidades generales."""
    pass


class ErrorCliente(ErrorEntidad):
    """
    Representa errores en los datos o validaciones de los clientes.

    Hereda de ErrorEntidad porque Cliente es una entidad del sistema.
    """
    pass


class ErrorServicio(ErrorSistema):
    """Representa errores relacionados con la gestión de servicios."""
    pass


class ErrorDisponibilidad(ErrorServicio):
    """
    Representa errores cuando un recurso o servicio no está disponible.

    Hereda de ErrorServicio para facilitar su captura específica
    o general dentro de las operaciones de servicios.
    """
    pass


class ErrorReserva(ErrorSistema):
    """Representa errores durante la creación y gestión de reservas."""
    pass


class ErrorOperacion(ErrorSistema):
    """Representa errores cuando se intenta realizar una operación no permitida."""
    pass


class ErrorRegistro(ErrorSistema):
    """Representa errores relacionados con el registro de eventos y mensajes."""
    pass
