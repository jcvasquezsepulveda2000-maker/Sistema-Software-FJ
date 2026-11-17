
import sys
from pathlib import Path

# Permitir que Python encuentre los modulos de la carpeta src
RUTA_SRC = Path(__file__).resolve().parent / "src"
if str(RUTA_SRC) not in sys.path:
    sys.path.insert(0, str(RUTA_SRC))

# Importar las clases del sistema
from cliente import Cliente
from reservas_salas import ReservaSala
from alquiler_equipos import AlquilerEquipo
from asesorias import AsesoriaEspecializada
from reserva import Reserva, ErrorReserva
from registro import registro


def mostrar_titulo(texto):
    print("\n" + "=" * 65)
    print(texto.center(65))
    print("=" * 65)


def registrar_evento(mensaje):
    registro.registrar_evento(mensaje)
    print("[OK]", mensaje)


def registrar_error(mensaje):
    registro.registrar_error(mensaje)
    print("[ERROR]", mensaje)


def registrar_advertencia(mensaje):
    registro.registrar_advertencia(mensaje)
    print("[AVISO]", mensaje)


def ejecutar_sistema():

    # Listas internas para gestionar los objetos del sistema
    clientes = []
    servicios = []
    reservas = []

    # Inicializar referencias
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

    except (ValueError, TypeError) as error:
        cliente = None
        registrar_error(f"Error al registrar cliente: {error}")

    else:
        print(cliente.obtener_informacion())
        registrar_evento("Cliente registrado correctamente.")

    # -------------------------------------------------
    # OPERACION 2: CREAR UN CLIENTE INVALIDO
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

    except (ValueError, TypeError) as error:
        registrar_error(f"Cliente rechazado: {error}")

    # -------------------------------------------------
    # OPERACION 3: CREAR SERVICIO DE RESERVA DE SALA
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

    except (ValueError, TypeError) as error:
        sala = None
        registrar_error(f"Error al crear sala: {error}")

    # -------------------------------------------------
    # OPERACION 4: DEMOSTRAR VARIANTES DE CALCULO
    # -------------------------------------------------
    mostrar_titulo("OPERACION 4: VARIANTES DE CALCULO")

    try:
        if sala is None:
            raise ValueError(
                "No existe una sala disponible para calcular."
            )

        # Calculo del costo base.
        costo_base = sala.calcular_costo(duracion=3)

        # Calculo aplicando descuento.
        costo_descuento = sala.calcular_costo_con_descuento(
            duracion=3,
            descuento=10
        )

        # Calculo aplicando impuestos.
        costo_impuesto = sala.calcular_costo_con_impuestos(
            duracion=3,
            impuesto=19
        )

        # Calculo aplicando descuento e impuestos.
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

    except (ValueError, TypeError) as error:
        registrar_error(f"Error en calculo de sala: {error}")

    # -------------------------------------------------
    # OPERACION 5: CREAR SERVICIO DE ALQUILER DE EQUIPOS
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

    except (ValueError, TypeError) as error:
        equipo = None
        registrar_error(f"Error al crear equipo: {error}")

    # -------------------------------------------------
    # OPERACION 6: ALQUILAR EQUIPOS DISPONIBLES
    # -------------------------------------------------
    mostrar_titulo("OPERACION 6: ALQUILER EXITOSO")

    try:
        if equipo is None:
            raise ValueError(
                "No existe un equipo disponible para alquilar."
            )

        resultado = equipo.alquilar(2)
        print(resultado)
        registrar_evento("Alquiler de dos proyectores realizado.")

    except (ValueError, TypeError) as error:
        registrar_error(f"Error en alquiler: {error}")

    # -------------------------------------------------
    # OPERACION 7: INTENTAR ALQUILAR MAS EQUIPOS
    # DE LOS DISPONIBLES
    # -------------------------------------------------
    mostrar_titulo("OPERACION 7: ALQUILER NO DISPONIBLE")

    try:
        if equipo is None:
            raise ValueError(
                "No existe un equipo para realizar el alquiler."
            )

        resultado = equipo.alquilar(10)
        print(resultado)

    except (ValueError, TypeError) as error:
        registrar_error(f"Alquiler rechazado: {error}")

    # -------------------------------------------------
    # OPERACION 8: CREAR SERVICIO DE ASESORIA
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

    except (ValueError, TypeError) as error:
        asesoria = None
        registrar_error(f"Error al crear asesoria: {error}")

    # -------------------------------------------------
    # OPERACION 9: CREAR Y CONFIRMAR UNA RESERVA
    # -------------------------------------------------
    mostrar_titulo("OPERACION 9: CONFIRMAR RESERVA")

    try:
        if cliente is None or asesoria is None:
            raise ValueError(
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

    except (ValueError, TypeError, ErrorReserva) as error:
        reserva1 = None
        registrar_error(f"Error al confirmar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 10: PROCESAR UNA RESERVA
    # -------------------------------------------------
    mostrar_titulo("OPERACION 10: PROCESAR RESERVA")

    try:
        if reserva1 is None:
            raise ErrorReserva(
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

    except (ValueError, TypeError, ErrorReserva) as error:
        registrar_error(f"Error al procesar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 11: CANCELAR UNA RESERVA PENDIENTE
    # -------------------------------------------------
    mostrar_titulo("OPERACION 11: CANCELAR RESERVA")

    try:
        if cliente is None or sala is None:
            raise ValueError(
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

    except (ValueError, TypeError, ErrorReserva) as error:
        reserva2 = None
        registrar_error(f"Error al cancelar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 12: PROCESAR RESERVA SIN CONFIRMAR
    # -------------------------------------------------
    mostrar_titulo("OPERACION 12: VALIDACION DE ESTADO")

    try:
        if cliente is None or asesoria is None:
            raise ValueError(
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

    except (ValueError, TypeError, ErrorReserva) as error:
        registrar_error(
            f"Procesamiento rechazado por estado incorrecto: {error}"
        )

    # -------------------------------------------------
    # OPERACION 13: DEMOSTRAR POLIMORFISMO
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

            except (ValueError, TypeError, AttributeError) as error:
                registrar_error(
                    f"Error al consultar un servicio mediante "
                    f"polimorfismo: {error}"
                )

    # -------------------------------------------------
    # OPERACION 14: INTENTAR CREAR UN SERVICIO INVALIDO
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

    except (ValueError, TypeError) as error:
        registrar_error(
            f"Servicio rechazado por datos invalidos: {error}"
        )

    # -------------------------------------------------
    # RESUMEN FINAL DEL SISTEMA
    # -------------------------------------------------
    mostrar_titulo("RESUMEN FINAL DEL SISTEMA")

    print(f"\nClientes registrados: {len(clientes)}")

    for elemento in clientes:
        try:
            print(elemento.obtener_informacion())
        except (ValueError, TypeError, AttributeError) as error:
            registrar_error(f"Error al mostrar un cliente: {error}")

    print(f"\nServicios creados correctamente: {len(servicios)}")

    for elemento in servicios:
        try:
            print(elemento.obtener_informacion())
        except (ValueError, TypeError, AttributeError) as error:
            registrar_error(f"Error al mostrar un servicio: {error}")

    print(f"\nReservas creadas: {len(reservas)}")

    for elemento in reservas:
        try:
            print(elemento.obtener_informacion())
            print("Estado:", elemento.estado)
        except (ValueError, TypeError, AttributeError) as error:
            registrar_error(f"Error al mostrar una reserva: {error}")

    registrar_evento("Finalizacion de las simulaciones del sistema.")

    print("\nLas simulaciones finalizaron.")
    print("Los eventos y errores se guardaron en la carpeta logs.")


if __name__ == "__main__":
    ejecutar_sistema()
