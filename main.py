
import sys
from pathlib import Path

# Permitir que Python encuentre los módulos de la carpeta src
RUTA_SRC = Path(__file__).resolve().parent / "src"
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


def ejecutar_sistema():

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

        print(cliente.obtener_informacion())
        registrar_evento("Cliente registrado correctamente.")

    except ValueError as error:
        registrar_error(f"Error al registrar cliente: {error}")

    # -------------------------------------------------
    # OPERACION 2: INTENTAR CREAR UN CLIENTE INVALIDO
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

        print(cliente_invalido.obtener_informacion())

    except ValueError as error:
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

        print(sala.obtener_informacion())
        registrar_evento("Servicio de sala creado correctamente.")

    except ValueError as error:
        registrar_error(f"Error al crear sala: {error}")

    # -------------------------------------------------
    # OPERACION 4: CALCULAR COSTO DE SALA
    # -------------------------------------------------
    mostrar_titulo("OPERACION 4: CALCULO DE COSTO")

    try:
        total_sala = sala.calcular_costo(
            duracion=3,
            descuento=10,
            impuesto=19
        )

        print(f"Costo total de la sala: ${total_sala:,.2f}")
        registrar_evento("Costo de reserva de sala calculado.")

    except ValueError as error:
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

        print(equipo.obtener_informacion())
        registrar_evento("Servicio de alquiler de equipos creado.")

    except ValueError as error:
        registrar_error(f"Error al crear equipo: {error}")

    # -------------------------------------------------
    # OPERACION 6: ALQUILAR EQUIPOS DISPONIBLES
    # -------------------------------------------------
    mostrar_titulo("OPERACION 6: ALQUILER EXITOSO")

    try:
        resultado = equipo.alquilar(2)

        print(resultado)
        registrar_evento("Alquiler de dos proyectores realizado.")

    except ValueError as error:
        registrar_error(f"Error en alquiler: {error}")

    # -------------------------------------------------
    # OPERACION 7: INTENTAR ALQUILAR MAS EQUIPOS
    # DE LOS DISPONIBLES
    # -------------------------------------------------
    mostrar_titulo("OPERACION 7: ALQUILER NO DISPONIBLE")

    try:
        resultado = equipo.alquilar(10)
        print(resultado)

    except ValueError as error:
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

        print(asesoria.obtener_informacion())
        registrar_evento("Servicio de asesoria creado correctamente.")

    except ValueError as error:
        registrar_error(f"Error al crear asesoria: {error}")

    # -------------------------------------------------
    # OPERACION 9: CREAR Y CONFIRMAR UNA RESERVA
    # -------------------------------------------------
    mostrar_titulo("OPERACION 9: CONFIRMAR RESERVA")

    try:
        reserva1 = Reserva(
            "RES001",
            cliente,
            asesoria,
            2
        )

        print(reserva1.obtener_informacion())

        resultado = reserva1.confirmar()
        print(resultado)

        registrar_evento("Reserva RES001 confirmada.")

    except (ValueError, ErrorReserva) as error:
        registrar_error(f"Error al confirmar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 10: PROCESAR UNA RESERVA
    # -------------------------------------------------
    mostrar_titulo("OPERACION 10: PROCESAR RESERVA")

    try:
        total = reserva1.procesar(
            descuento=5,
            impuesto=19
        )

        print(f"Total de la reserva: ${total:,.2f}")
        print(reserva1.obtener_informacion())

        registrar_evento(
            f"Reserva RES001 procesada. Total: ${total:,.2f}"
        )

    except ErrorReserva as error:
        registrar_error(f"Error al procesar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 11: CANCELAR UNA RESERVA PENDIENTE
    # -------------------------------------------------
    mostrar_titulo("OPERACION 11: CANCELAR RESERVA")

    try:
        reserva2 = Reserva(
            "RES002",
            cliente,
            sala,
            2
        )

        print(reserva2.obtener_informacion())

        resultado = reserva2.cancelar()
        print(resultado)

        registrar_evento("Reserva RES002 cancelada correctamente.")

    except ErrorReserva as error:
        registrar_error(f"Error al cancelar reserva: {error}")

    # -------------------------------------------------
    # OPERACION 12: INTENTAR PROCESAR UNA RESERVA
    # SIN CONFIRMAR
    # -------------------------------------------------
    mostrar_titulo("OPERACION 12: VALIDACION DE ESTADO")

    try:
        reserva3 = Reserva(
            "RES003",
            cliente,
            asesoria,
            1
        )

        reserva3.procesar()

    except ErrorReserva as error:
        registrar_error(
            f"Procesamiento rechazado por estado incorrecto: {error}"
        )

    # -------------------------------------------------
    # RESUMEN FINAL
    # -------------------------------------------------
    mostrar_titulo("RESUMEN FINAL DEL SISTEMA")

    print(cliente.obtener_informacion())
    print(sala.obtener_informacion())
    print(equipo.obtener_informacion())
    print(asesoria.obtener_informacion())

    print("\nEstado de la primera reserva:", reserva1.estado)
    print("Estado de la segunda reserva:", reserva2.estado)
    print("Estado de la tercera reserva:", reserva3.estado)

    registrar_evento("Finalizacion de las simulaciones del sistema.")

    print("\nLas simulaciones finalizaron.")
    print("Los eventos y errores se guardaron en la carpeta logs.")


if __name__ == "__main__":
    ejecutar_sistema()
