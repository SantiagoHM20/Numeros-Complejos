import math


def division_complejos(a, b):
    if (b[0]) ** 2 + (b[1]) ** 2 == 0:
       raise ValueError("No se puede realizar la división, la suma de los cuadrados de el divisor es 0")

    else:
        part_real = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0]) ** 2 + (b[1]) ** 2)
        part_img = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0]) ** 2 + (b[1]) ** 2)

    return (part_real, part_img)

def prettyprinting(c):

    return f"{c[0]} + {c[1]}i" if c[1] >0 else f"{c[0]} - {c[1]*-1}i"


def suma_complejos(a, b):
    part_real = a[0] + b[0]
    part_img = a[1] + b[1]

    return (part_real, part_img)


def resta_complejos(a, b):
    part_real = a[0] - b[0]
    part_img = a[1] - b[1]

    return (part_real, part_img)


def multiplicacion_complejos(a, b):
    part_real = a[0] * b[0] - a[1] * b[1]
    part_img = a[0] * b[1] + a[1] * b[0]

    return (part_real, part_img)


def modulo_complejos(a, b):
    modulo = math.sqrt(a ** 2 + b ** 2)

    return modulo


def conjugado_complejos(a, b):
    new_b = b * -1

    return (a, new_b)


def get_fase(a, b):
    fase_rad = math.atan2(b, a)

    fase = math.degrees(fase_rad)

    if fase < 0:

        fase += 360

    return fase


def get_polar_rep(a, b):
    mod = modulo_complejos(a, b)

    fase = get_fase(a, b)

    return (mod, fase)


def get_cart_rep(a, b):
    angulo_rad = math.radians(b)

    part_real = a * math.cos(angulo_rad)
    part_img = a * math.sin(angulo_rad)

    return (round(part_real,10), round(part_img, 10))


def main():
    while True:
        operacion = int(input("Qué operación entre números complejos desea realizar?\n"
                              "1. Suma\n"
                              "2. Resta\n"
                              "3. Multiplicación\n"
                              "4. División\n"
                              "5. Obtener el módulo de un número complejo\n"
                              "6. Obtener el conjugado de un número complejo\n"
                              "7. Obtener el ángulo/fase de un número en el plano complejo\n"
                              "8. Obtener la representación polar de un número complejo\n"
                              "9. Obtener la representación Cartesiana de un número complejo\n"))

        if operacion == 1:

            num1R = int(input("Ingrese la parte real del primer número: "))
            num1I = int(input("Ingrese la parte imaginaria del primer número: "))
            num2R = int(input("Ingrese la parte real del segundo número: "))
            num2I = int(input("Ingrese la parte imaginaria del segundo número: "))
            a = [num1R, num2R]
            b = [num1I, num2I]
            result = suma_complejos(a, b)
            print(result)

        elif operacion == 2:

            num1R = int(input("Ingrese la parte real del primer número: "))
            num1I = int(input("Ingrese la parte imaginaria del primer número: "))
            num2R = int(input("Ingrese la parte real del segundo número: "))
            num2I = int(input("Ingrese la parte imaginaria del segundo número: "))
            a = [num1R, num2R]
            b = [num1I, num2I]
            result = resta_complejos(a, b)
            print(result)

        elif operacion == 3:

            num1R = int(input("Ingrese la parte real del primer número: "))
            num1I = int(input("Ingrese la parte imaginaria del primer número: "))
            num2R = int(input("Ingrese la parte real del segundo número: "))
            num2I = int(input("Ingrese la parte imaginaria del segundo número: "))
            a = [num1R, num2R]
            b = [num1I, num2I]
            result = multiplicacion_complejos(a, b)
            print(result)

        elif operacion == 4:

            num1R = int(input("Ingrese la parte real del primer número: "))
            num1I = int(input("Ingrese la parte imaginaria del primer número: "))
            num2R = int(input("Ingrese la parte real del divisor: "))
            num2I = int(input("Ingrese la parte imaginaria del divisor: "))
            a = [num1R, num2R]
            b = [num1I, num2I]
            result = division_complejos(a, b)
            print(result)

        elif operacion == 5:

            a = int(input("Ingrese la parte real del número: "))
            b = int(input("Ingrese la parte imaginaria del número: "))

            result = modulo_complejos(a, b)
            print(result)

        elif operacion == 6:

            a = int(input("Ingrese la parte real del número: "))
            b = int(input("Ingrese la parte imaginaria del número: "))

            result = conjugado_complejos(a, b)
            print(result)

        elif operacion == 7:

            a = int(input("Ingrese la parte real del número: "))
            b = int(input("Ingrese la parte imaginaria del número: "))

            result = get_fase(a, b)
            print(result)

        elif operacion == 8:

            a = int(input("Ingrese la parte real del número: "))
            b = int(input("Ingrese la parte imaginaria del número: "))

            result = get_polar_rep(a, b)
            print(result)

        elif operacion == 9:

            a = float(input("Ingrese el módulo del número: "))
            b = float(input("Ingrese el ángulo/fase del número en grados: "))

            result = get_cart_rep(a, b)
            print(result)

        else:
            print("Opción no válida, por favor ingrese un número entre 1 y 9.")

        rep = input("¿Quiere seguir calculando? (si/no): ").strip().lower()
        if rep not in ("si", "sí"):
            break


if __name__ == "__main__":
    main()