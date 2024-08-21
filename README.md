# Numeros Complejos

### Santiago Hurtado Martínez
### Laboratorio 1 CNYT 

## Introducción

El siguiente codigo implementa varias operaciones aritméticas con números Complejos manejados como tuplas.
Es decir (a,b) siendo a la parte real y b la parte imaginaria del número.

## Descripción de las funciones

El codigo implementa las siguiente funciones:

Suma

Resta

Multiplicación

División

Representación compleja ((a,b) -> a+bi)

Modulo 

Conjugado

Ángulo en el plano Complejo

Representación polar

Representación cartesiana (A partir de la polar)

## Entradas

La entrada depende de la operación en cuestión, si la operación requiere 2 números complejos la entrada serán 2 tuplas de números (a,b) y (c,d) para a, b, c y d en los Reales.

Si la operación solo requiere un número la entrada será una sola tupla (a,b) para a y b en los Reales.

## Salidas

Para todas las funciones menos la representación polar la salida está compuesta por una tupla (a,b) para a y b en los Reales.

La representación polar es una cadena de strings que contienen tanto a como b.

## Pruebas

Para las pruebas se implementó un codigo adicional con la clase TestFuncionesComplejos.

importando las funciones anteriores y haciendo uso de la función assert.Equal() y assertAlmostEqual.() para verificar y comparar los valores de las distintas funciones para distintas entradas.
