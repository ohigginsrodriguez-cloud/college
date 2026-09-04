# Simulación de cafetería con SimPy

Programa en Python que simula el funcionamiento de una cafetería usando la
librería SimPy, basado en datos reales recolectados mediante observación de
campo (ver `coffee_shop.csv`).

## ¿Cómo funciona?

El programa modela clientes que llegan en grupos a una cafetería, hacen fila
para pagar en caja y son atendidos. Los parámetros de la simulación (tiempo
entre llegadas, tamaños de grupo y tiempo de servicio) no son inventados:
se calcularon a partir de una observación real de 33 minutos con 2 cajas.

- Tiempo medio de servicio: 2.1 min (calculado de 66 min-servidor / 31 clientes atendidos)
- Tiempo medio entre llegadas de grupos: 3.25 min
- Tamaños de grupo observados: 2 a 6 personas

## Datos de entrada

El programa pide por terminal:

1. Cuántas cajas (servidores) simular
2. Duración de la simulación en minutos

## Salida

El programa imprime en terminal el registro de cada cliente (llegada, inicio
de atención, salida) y al final reporta:

- Número de clientes atendidos
- Tiempo de espera promedio
- Tiempo de espera máximo

## Cómo correrlo

```bash
pip install simpy
python3 simulacion_cafeteria.py
```

## Archivos

- `simulacion_cafeteria.py`: programa de simulación
- `coffee_shop.csv`: datos de observación de campo (llegadas y atenciones por minuto)