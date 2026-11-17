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
- Aplicación de herencia, abstracción y polimorfismo.

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

## Descripción de los módulos

- **entidad.py:** contiene la clase abstracta Entidad, que establece la estructura general de las entidades del sistema.
- **cliente.py:** administra los datos de los clientes y sus respectivas validaciones.
- **servicio.py:** define la estructura general de los servicios y los métodos para calcular costos.
- **reservas_salas.py:** gestiona los servicios de reserva de salas.
- **alquiler_equipos.py:** administra el alquiler y la disponibilidad de equipos.
- **asesorias.py:** gestiona los servicios de asesorías especializadas.
- **reserva.py:** permite crear, confirmar, cancelar y procesar reservas.
- **registro.py:** administra el registro de eventos y errores del sistema.
- **main.py:** ejecuta la aplicación y realiza las simulaciones de funcionamiento.

## Ejecución del programa

1. Abrir el proyecto en Visual Studio Code.
2. Abrir una terminal en la carpeta principal del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

## Pruebas realizadas

Se implementaron 14 operaciones de simulación para comprobar el funcionamiento del sistema. Estas incluyen:

- Registro de clientes y validación de información.
- Creación de diferentes tipos de servicios.
- Cálculo de costos.
- Alquiler de equipos y comprobación de disponibilidad.
- Confirmación, cancelación y procesamiento de reservas.
- Pruebas con operaciones inválidas.
- Demostración del polimorfismo.
- Validación del manejo de excepciones.

El sistema controla los errores generados durante las operaciones y continúa ejecutándose sin detener toda la aplicación.

## Almacenamiento de registros

Los eventos y errores se guardan automáticamente en la carpeta `logs`, dentro del archivo `sistema.log`. Esta carpeta y el archivo se generan durante la ejecución del programa. No se utiliza una base de datos.

## Principios de programación aplicados

- **Abstracción:** definición de clases abstractas para establecer estructuras generales.
- **Herencia:** reutilización de atributos y métodos mediante clases derivadas.
- **Encapsulación:** protección y validación de los datos de las entidades.
- **Polimorfismo:** implementación de comportamientos específicos para cada tipo de servicio.
- **Manejo de excepciones:** control de errores para mantener la continuidad del sistema.
- **Organización modular:** separación de las funcionalidades en diferentes archivos.

## Repositorio

Proyecto desarrollado y compartido mediante GitHub:

https://github.com/jcvasquezsepulveda2000-maker/Sistema-Software-FJ
