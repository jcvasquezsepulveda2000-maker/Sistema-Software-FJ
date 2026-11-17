"""
Excepciones personalizadas del Sistema de Gestion de Servicios.

Centraliza los errores para facilitar su identificacion,
captura y registro.
"""


class ErrorSistema(Exception):
    """Excepcion base para los errores propios del sistema."""
    pass


class ErrorEntidad(ErrorSistema):
    """Errores relacionados con entidades generales."""
    pass


class ErrorCliente(ErrorEntidad):
    """Errores relacionados con los datos de los clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Errores relacionados con los servicios."""
    pass


class ErrorDisponibilidad(ErrorServicio):
    """Errores cuando no existen recursos disponibles."""
    pass


class ErrorReserva(ErrorSistema):
    """Errores relacionados con la gestion de reservas."""
    pass


class ErrorOperacion(ErrorSistema):
    """Errores cuando una operacion no esta permitida."""
    pass


class ErrorRegistro(ErrorSistema):
    """Errores relacionados con el registro de eventos."""
    pass
