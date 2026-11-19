import sys
from pathlib import Path

# Permitir que Python encuentre los módulos de la carpeta src.
RUTA_SRC = Path(__file__).resolve().parent / "src"

if str(RUTA_SRC) not in sys.path:
    sys.path.insert(0, str(RUTA_SRC))


# Importar las clases necesarias para gestionar clientes,
# servicios especializados y reservas.
from cliente import Cliente
from reservas_salas import ReservaSala
from alquiler_equipos import AlquilerEquipo
from asesorias import AsesoriaEspecializada
from reserva import Reserva
from registro import registro

# Importar las excepciones personalizadas centralizadas.
from excepciones import (
    ErrorSistema,
    ErrorReserva,
    ErrorOperacion
)


def mostrar_titulo(texto):
    """
    Muestra un título centrado para separar las secciones
    y operaciones durante la ejecución del sistema.
    """
    print("\n" + "=" * 65)
    print(texto.center(65))
    print("=" * 65)


def registrar_evento(mensaje):
    """
    Registra un evento informativo en el archivo de logs
    y muestra un mensaje de confirmación en pantalla.
    """
    registro.registrar_evento(mensaje)
    print("[OK]", mensaje)


def registrar_error(mensaje):
    """
    Registra un error ocurrido durante una operación
    y muestra su notificación en pantalla.
    """
    registro.registrar_error(mensaje)
    print("[ERROR]", mensaje)


def registrar_advertencia(mensaje):
    """
    Registra una advertencia del sistema y la muestra
    en pantalla para informar sobre una situación especial.
    """
    registro.registrar_advertencia(mensaje)
    print("[AVISO]", mensaje)


def ejecutar_sistema():
    """
    Ejecuta las simulaciones completas del sistema de gestión.

    Crea clientes, servicios y reservas; realiza operaciones
    válidas e inválidas; demuestra cálculos, polimorfismo,
    manejo de excepciones y registro de eventos y errores.
    Finalmente, presenta un resumen de los objetos creados.
    """

    # Listas internas para gestionar los objetos del sistema.
    clientes = []
    servicios = []
    reservas = []

    # Inicializar referencias para controlar los objetos creados.
    cliente = None
    sala = None
    equipo = None
    asesoria = None
    reserva1 = None
    reserva2 = None
    reserva3 = None

    mostrar_titulo("SISTEMA INTEGRAL DE GESTION")

    # -------------------------------------------------
    # OPERACION 1: CREAR UN CLIENTE VALIDO
    # Se registra un cliente con información correcta.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 1: REGISTRO DE CLIENTE")

    try:
        cliente = Cliente(
            "CLI001",
            "Juan Carlos Perez",
            "1234567890",
            "juan@gmail.com",
            "3001234567"
        )

        clientes.append(cliente)

    except (ErrorSistema, ValueError, TypeError) as error:
        cliente = None
        registrar_error(f"Error al registrar cliente: {error}")

    else:
        print(cliente.obtener_informacion())
        registrar_evento("Cliente registrado correctamente.")

    # -------------------------------------------------
    # OPERACION 2: CREAR UN CLIENTE INVALIDO
    # Se intenta registrar un cliente con correo incorrecto.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 2: VALIDACION DE CLIENTE")

    try:
        cliente_invalido = Cliente(
            "CLI002",
            "Maria Lopez",
            "1234567891",
            "correo_invalido",
            "3001234568"
        )

        clientes.append(cliente_invalido)
        print(cliente_invalido.obtener_informacion())

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(f"Cliente rechazado: {error}")

    # -------------------------------------------------
    # OPERACION 3: CREAR SERVICIO DE RESERVA DE SALA
    # Se crea una sala con capacidad y costo válidos.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 3: RESERVA DE SALA")

    try:
        sala = ReservaSala(
            "SAL001",
            "Sala de reuniones",
            "Sala equipada para reuniones empresariales",
            15,
            50000
        )

        servicios.append(sala)
        print(sala.obtener_informacion())
        registrar_evento("Servicio de sala creado correctamente.")

    except (ErrorSistema, ValueError, TypeError) as error:
        sala = None
        registrar_error(f"Error al crear sala: {error}")

    # -------------------------------------------------
    # OPERACION 4: DEMOSTRAR VARIANTES DE CALCULO
    # Se realizan cálculos base, con descuento e impuestos.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 4: VARIANTES DE CALCULO")

    try:
        if sala is None:
            raise ErrorOperacion(
                "No existe una sala disponible para calcular."
            )

        # Cálculo del costo base.
        costo_base = sala.calcular_costo(duracion=3)

        # Cálculo aplicando descuento.
        costo_descuento = sala.calcular_costo_con_descuento(
            duracion=3,
            descuento=10
        )

        # Cálculo aplicando impuestos.
        costo_impuesto = sala.calcular_costo_con_impuestos(
            duracion=3,
            impuesto=19
        )

        # Cálculo aplicando descuento e impuestos.
        costo_final = sala.calcular_costo(
            duracion=3,
            descuento=10,
            impuesto=19
        )

        print(f"Costo base: ${costo_base:,.2f}")
        print(f"Costo con descuento: ${costo_descuento:,.2f}")
        print(f"Costo con impuestos: ${costo_impuesto:,.2f}")
        print(
            f"Costo con descuento e impuestos: ${costo_final:,.2f}"
        )

        registrar_evento(
            "Se realizaron las cuatro variantes de calculo del servicio."
        )

    except (ErrorSistema, ValueError, TypeError, OverflowError) as error:
        registrar_error(f"Error en calculo de sala: {error}")

    # -------------------------------------------------
    # OPERACION 5: CREAR SERVICIO DE ALQUILER DE EQUIPOS
    # Se registra un servicio de alquiler de proyectores.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 5: ALQUILER DE EQUIPOS")

    try:
        equipo = AlquilerEquipo(
            "EQ001",
            "Proyector",
            "Proyector multimedia para presentaciones",
            5,
            15000
        )

        servicios.append(equipo)
        print(equipo.obtener_informacion())
        registrar_evento("Servicio de alquiler de equipos creado.")

    except (ErrorSistema, ValueError, TypeError) as error:
        equipo = None
        registrar_error(f"Error al crear equipo: {error}")

    # -------------------------------------------------
    # OPERACION 6: ALQUILAR EQUIPOS DISPONIBLES
    # Se realiza un alquiler de dos proyectores.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 6: ALQUILER EXITOSO")

    try:
        if equipo is None:
            raise ErrorOperacion(
                "No existe un equipo disponible para alquilar."
            )

        resultado = equipo.alquilar(2)
        print(resultado)

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(f"Error en alquiler: {error}")

    else:
        registrar_evento("Alquiler de dos proyectores realizado.")

    finally:
        print("Finalizo el intento de alquiler de equipos.")

    # -------------------------------------------------
    # OPERACION 7: INTENTAR ALQUILAR MAS EQUIPOS
    # DE LOS DISPONIBLES
    # Se prueba el manejo de una disponibilidad insuficiente.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 7: ALQUILER NO DISPONIBLE")

    try:
        if equipo is None:
            raise ErrorOperacion(
                "No existe un equipo para realizar el alquiler."
            )

        resultado = equipo.alquilar(10)
        print(resultado)

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(f"Alquiler rechazado: {error}")

    # -------------------------------------------------
    # OPERACION 8: CREAR SERVICIO DE ASESORIA
    # Se registra una asesoría con especialista y especialidad.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 8: ASESORIA ESPECIALIZADA")

    try:
        asesoria = AsesoriaEspecializada(
            "ASE001",
            "Asesoria informatica",
            "Orientacion sobre sistemas y tecnologia",
            "Carlos Rodriguez",
            "Ingenieria de sistemas",
            80000
        )

        servicios.append(asesoria)
        print(asesoria.obtener_informacion())
        registrar_evento("Servicio de asesoria creado correctamente.")

    except (ErrorSistema, ValueError, TypeError) as error:
        asesoria = None
        registrar_error(f"Error al crear asesoria: {error}")

    # -------------------------------------------------
    # OPERACION 9: CREAR Y CONFIRMAR UNA RESERVA
    # Se crea una reserva válida y se cambia su estado.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 9: CONFIRMAR RESERVA")

    try:
        if cliente is None or asesoria is None:
            raise ErrorOperacion(
                "Se necesita un cliente y una asesoria validos."
            )

        reserva1 = Reserva(
            "RES001",
            cliente,
            asesoria,
            2
        )

        reservas.append(reserva1)
        print(reserva1.obtener_informacion())

        resultado = reserva1.confirmar()
        print(resultado)

        registrar_evento("Reserva RES001 confirmada.")

    except (ErrorSistema, ValueError, TypeError) as error:
        reserva1 = None
        registrar_error(f"Error al confirmar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 10: PROCESAR UNA RESERVA
    # Se calcula el costo de una reserva previamente confirmada.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 10: PROCESAR RESERVA")

    try:
        if reserva1 is None:
            raise ErrorOperacion(
                "No existe una reserva para procesar."
            )

        total = reserva1.procesar(
            descuento=5,
            impuesto=19
        )

        print(f"Total de la reserva: ${total:,.2f}")
        print(reserva1.obtener_informacion())

        registrar_evento(
            f"Reserva RES001 procesada. Total: ${total:,.2f}"
        )

    except (ErrorSistema, ValueError, TypeError, OverflowError) as error:
        registrar_error(f"Error al procesar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 11: CANCELAR UNA RESERVA PENDIENTE
    # Se crea una reserva y se cancela antes de confirmarla.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 11: CANCELAR RESERVA")

    try:
        if cliente is None or sala is None:
            raise ErrorOperacion(
                "Se necesita un cliente y una sala validos."
            )

        reserva2 = Reserva(
            "RES002",
            cliente,
            sala,
            2
        )

        reservas.append(reserva2)
        print(reserva2.obtener_informacion())

        resultado = reserva2.cancelar()
        print(resultado)

        registrar_evento("Reserva RES002 cancelada correctamente.")

    except (ErrorSistema, ValueError, TypeError) as error:
        reserva2 = None
        registrar_error(f"Error al cancelar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 12: PROCESAR RESERVA SIN CONFIRMAR
    # Se verifica que no se procesen reservas pendientes.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 12: VALIDACION DE ESTADO")

    try:
        if cliente is None or asesoria is None:
            raise ErrorOperacion(
                "Se necesita un cliente y una asesoria validos."
            )

        reserva3 = Reserva(
            "RES003",
            cliente,
            asesoria,
            1
        )

        reservas.append(reserva3)
        reserva3.procesar()

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(
            f"Procesamiento rechazado por estado incorrecto: {error}"
        )

    # -------------------------------------------------
    # OPERACION 13: DEMOSTRAR POLIMORFISMO
    # Se recorren los servicios y se utilizan sus métodos comunes.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 13: DEMOSTRACION DE POLIMORFISMO")

    if not servicios:
        registrar_advertencia(
            "No hay servicios disponibles para demostrar polimorfismo."
        )

    else:
        for servicio in servicios:
            try:
                print("\nInformacion del servicio:")
                print(servicio.obtener_informacion())

                costo = servicio.calcular_costo(duracion=1)

                print(f"Costo de una hora: ${costo:,.2f}")

                registrar_evento(
                    f"Servicio consultado mediante polimorfismo: "
                    f"{servicio.nombre}"
                )

            except (
                ErrorSistema,
                ValueError,
                TypeError,
                AttributeError
            ) as error:
                registrar_error(
                    f"Error al consultar un servicio mediante "
                    f"polimorfismo: {error}"
                )

    # -------------------------------------------------
    # OPERACION 14: INTENTAR CREAR UN SERVICIO INVALIDO
    # Se intenta crear una sala con capacidad igual a cero.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 14: VALIDACION DE SERVICIO")

    try:
        servicio_invalido = ReservaSala(
            "SAL002",
            "Sala invalida",
            "Servicio de prueba con capacidad incorrecta",
            0,
            50000
        )

        servicios.append(servicio_invalido)
        print(servicio_invalido.obtener_informacion())

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(
            f"Servicio rechazado por datos invalidos: {error}"
        )

    # -------------------------------------------------
    # OPERACION 15: INTENTAR CANCELAR UNA RESERVA PROCESADA
    # Se comprueba que una reserva procesada no pueda cancelarse.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 15: CANCELACION NO PERMITIDA")

    try:
        if reserva1 is None:
            raise ErrorOperacion(
                "No existe una reserva para realizar la prueba."
            )

        if reserva1.estado != "Procesada":
            raise ErrorOperacion(
                "La prueba requiere una reserva procesada."
            )

        resultado = reserva1.cancelar()
        print(resultado)

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(
            f"Cancelacion rechazada por estado incorrecto: {error}"
        )

    # -------------------------------------------------
    # OPERACION 16: INTENTAR APLICAR UN DESCUENTO INVALIDO
    # Se prueba el rechazo de un descuento superior al 100 %.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 16: DESCUENTO FUERA DE RANGO")

    try:
        if sala is None:
            raise ErrorOperacion(
                "No existe una sala para realizar el calculo."
            )

        costo = sala.calcular_costo(
            duracion=1,
            descuento=150
        )

        print(f"Costo calculado: ${costo:,.2f}")

    except (ErrorSistema, ValueError, TypeError, OverflowError) as error:
        registrar_error(
            f"Descuento rechazado por estar fuera de rango: {error}"
        )

    # -------------------------------------------------
    # OPERACION 17: INTENTAR CREAR UNA RESERVA SIN CLIENTE
    # Se comprueba que una reserva requiera un cliente válido.
    # -------------------------------------------------
    mostrar_titulo("OPERACION 17: RESERVA SIN CLIENTE")

    try:
        if sala is None:
            raise ErrorOperacion(
                "No existe un servicio para realizar la prueba."
            )

        reserva_sin_cliente = Reserva(
            "RES004",
            None,
            sala,
            1
        )

        print(reserva_sin_cliente.obtener_informacion())

    except (ErrorSistema, ValueError, TypeError) as error:
        registrar_error(
            f"Reserva rechazada por falta de cliente: {error}"
        )

    # -------------------------------------------------
    # RESUMEN FINAL DEL SISTEMA
    # Mostrar los clientes, servicios y reservas creados.
    # -------------------------------------------------
    mostrar_titulo("RESUMEN FINAL DEL SISTEMA")

    print(f"\nClientes registrados: {len(clientes)}")

    for elemento in clientes:
        try:
            print(elemento.obtener_informacion())

        except (ErrorSistema, ValueError, TypeError, AttributeError) as error:
            registrar_error(f"Error al mostrar un cliente: {error}")

    print(f"\nServicios creados correctamente: {len(servicios)}")

    for elemento in servicios:
        try:
            print(elemento.obtener_informacion())

        except (ErrorSistema, ValueError, TypeError, AttributeError) as error:
            registrar_error(f"Error al mostrar un servicio: {error}")

    print(f"\nReservas creadas: {len(reservas)}")

    for elemento in reservas:
        try:
            print(elemento.obtener_informacion())
            print("Estado:", elemento.estado)

        except (ErrorSistema, ValueError, TypeError, AttributeError) as error:
            registrar_error(f"Error al mostrar una reserva: {error}")

    # Registrar la finalización de todas las simulaciones.
    registrar_evento("Finalizacion de las simulaciones del sistema.")

    print("\nLas simulaciones finalizaron.")
    print("Los eventos y errores se guardaron en la carpeta logs.")


# Punto de entrada principal del programa.
# Ejecutar las simulaciones únicamente cuando se inicia este archivo.
if __name__ == "__main__":
    ejecutar_sistema()
