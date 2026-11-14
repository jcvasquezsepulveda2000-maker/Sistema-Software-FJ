# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema integral para gestionar clientes, servicios y reservas. Fue elaborado en Python aplicando los principios de la Programación Orientada a Objetos (POO).

El sistema permite registrar clientes, administrar diferentes tipos de servicios, calcular costos, gestionar reservas y controlar situaciones que puedan generar errores durante su ejecución.

## Objetivo

Desarrollar una aplicación organizada y funcional que permita simular operaciones de gestión de clientes, servicios y reservas mediante clases, objetos, listas y manejo de excepciones, sin utilizar una base de datos.

## Funcionalidades principales

- Registro y validación de clientes.
- Encapsulación de datos personales.
- Creación y administración de servicios.
- Reserva de salas.
- Alquiler de equipos.
- Gestión de asesorías especializadas.
- Confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos con descuentos e impuestos.
- Manejo de excepciones y errores.
- Registro de eventos y errores en archivos de log.
- Simulación de operaciones válidas e inválidas.

## Tecnologías utilizadas

- Python.
- Visual Studio Code.
- Git.
- GitHub.

## Estructura del proyecto

```text
Sistema-Software-FJ/
│
├── src/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reservas_salas.py
│   ├── alquiler_equipos.py
│   ├── asesorias.py
│   ├── reserva.py
│   └── registro.py
│
├── logs/
│   └── sistema.log
│
├── main.py
├── README.md
└── .gitignore
```

## Ejecución del programa

1. Abrir el proyecto en Visual Studio Code.
2. Abrir una terminal en la carpeta principal del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

## Pruebas realizadas

Se realizaron 12 operaciones de simulación para comprobar el funcionamiento del sistema. Estas incluyen registros correctos, validaciones de datos, cálculos de costos, alquileres, confirmación y cancelación de reservas, además de pruebas con operaciones inválidas.

El sistema permite controlar los errores y continuar con las demás operaciones.

## Almacenamiento de registros

Los eventos y errores se guardan automáticamente en la carpeta `logs`, dentro del archivo `sistema.log`. No se utiliza una base de datos.

## Principios de programación aplicados

- Abstracción.
- Herencia.
- Encapsulación.
- Polimorfismo.
- Manejo de excepciones.
- Organización modular del código.

## Repositorio

Proyecto desarrollado y compartido mediante GitHub:

https://github.com/jcvasquezsepulveda2000-maker/Sistema-Software-FJ
