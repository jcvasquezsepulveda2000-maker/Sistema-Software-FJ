# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del proyecto

Este proyecto desarrolla un sistema integral para gestionar clientes, servicios y reservas de la empresa Software FJ. Fue elaborado en Python aplicando los principios de la Programación Orientada a Objetos (POO).

La aplicación permite registrar y validar clientes, administrar servicios de reserva de salas, alquiler de equipos y asesorías especializadas, calcular costos, gestionar reservas y controlar errores durante la ejecución. La información se administra mediante objetos y listas, sin utilizar bases de datos.

## Objetivo

Desarrollar una aplicación modular y funcional que simule operaciones de gestión de clientes, servicios y reservas, aplicando abstracción, herencia, encapsulación, polimorfismo y manejo avanzado de excepciones.

## Funcionalidades principales

- Registro y validación de clientes, con encapsulación de datos personales.
- Creación y administración de reservas de salas, alquileres de equipos y asesorías especializadas.
- Confirmación, cancelación y procesamiento de reservas.
- Cálculo de costos con variantes de descuentos e impuestos.
- Validación de datos, parámetros, disponibilidad y estados de las reservas.
- Manejo de excepciones personalizadas y encadenamiento de excepciones.
- Uso de bloques `try/except`, `try/except/else` y `try/except/finally`.
- Registro de eventos y errores en archivos de log.
- Simulación de 17 operaciones, con escenarios válidos e inválidos.

## Tecnologías utilizadas

- Python.
- Visual Studio Code.
- Git y GitHub.

## Estructura del proyecto

```text
Sistema-Software-FJ/
├── src/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reservas_salas.py
│   ├── alquiler_equipos.py
│   ├── asesorias.py
│   ├── reserva.py
│   ├── excepciones.py
│   └── registro.py
├── logs/
│   └── sistema.log
├── main.py
├── README.md
└── .gitignore
```

La carpeta `logs` y el archivo `sistema.log` se generan o actualizan durante la ejecución, según los eventos registrados.

## Descripción de los módulos

- **entidad.py:** define la clase abstracta `Entidad`, que establece la estructura general de las entidades del sistema.
- **cliente.py:** administra los datos de los clientes y sus validaciones.
- **servicio.py:** define la clase abstracta `Servicio`, las validaciones comunes y los cálculos de costos.
- **reservas_salas.py:** implementa el servicio especializado de reserva de salas.
- **alquiler_equipos.py:** administra el alquiler de equipos y su disponibilidad.
- **asesorias.py:** implementa los servicios de asesorías especializadas.
- **reserva.py:** integra cliente, servicio, duración y estado; permite confirmar, cancelar y procesar reservas.
- **excepciones.py:** contiene la jerarquía de excepciones personalizadas utilizadas por los módulos.
- **registro.py:** administra el registro de eventos y errores del sistema.
- **main.py:** ejecuta la aplicación y presenta las simulaciones de funcionamiento.

## Ejecución del programa

1. Abrir el proyecto en Visual Studio Code.
2. Abrir una terminal en la carpeta principal del proyecto.
3. Ejecutar:

```bash
python main.py
```

## Simulaciones realizadas

El programa ejecuta **17 operaciones** para demostrar el funcionamiento del sistema:

1. Registro de un cliente válido.
2. Validación y rechazo de un cliente con correo inválido.
3. Creación de un servicio de reserva de sala.
4. Demostración de variantes de cálculo de costos: base, con descuento, con impuestos y con descuento e impuestos.
5. Creación de un servicio de alquiler de equipos.
6. Alquiler exitoso de equipos y actualización de disponibilidad.
7. Rechazo de un alquiler por disponibilidad insuficiente.
8. Creación de un servicio de asesoría especializada.
9. Confirmación de una reserva.
10. Procesamiento de una reserva confirmada.
11. Cancelación de una reserva pendiente.
12. Rechazo del procesamiento de una reserva que no está confirmada.
13. Demostración de polimorfismo con los tres tipos de servicios.
14. Rechazo de la creación de un servicio con capacidad inválida.
15. Rechazo del intento de cancelar una reserva ya procesada.
16. Rechazo de un descuento fuera del rango permitido.
17. Rechazo de la creación de una reserva sin un cliente válido.

Las simulaciones incluyen situaciones válidas e inválidas. Los errores esperados se controlan mediante excepciones para permitir que el programa continúe con las operaciones siguientes.

## Almacenamiento de registros

Los eventos y errores se registran en `logs/sistema.log`. El sistema utiliza archivos únicamente para el registro de eventos y errores; no utiliza un motor de base de datos para almacenar la información de clientes, servicios o reservas.

## Principios de programación aplicados

- **Abstracción:** definición de clases abstractas para establecer estructuras generales.
- **Herencia:** reutilización de atributos y métodos mediante clases derivadas.
- **Encapsulación:** protección y validación de los datos de las entidades.
- **Polimorfismo:** implementación de comportamientos específicos para cada tipo de servicio.
- **Manejo de excepciones:** control de errores mediante excepciones personalizadas, bloques de manejo y encadenamiento.
- **Organización modular:** separación de las responsabilidades del sistema en diferentes archivos.

## Repositorio

Proyecto desarrollado y compartido mediante GitHub:

https://github.com/jcvasquezsepulveda2000-maker/Sistema-Software-FJ
