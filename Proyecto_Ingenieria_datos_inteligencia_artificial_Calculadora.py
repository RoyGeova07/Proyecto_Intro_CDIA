from fractions import Fraction

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self,  otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __sub__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador - otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __mul__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __truediv__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        resultado = Fraccion(nuevo_numerador, nuevo_denominador)
        resultado.simplificar()
        return resultado

    def __eq__(self, otra_fraccion):
        return (self.numerador / self.denominador) == (otra_fraccion.numerador / otra_fraccion.denominador)

    def __lt__(self, otra_fraccion):
        return (self.numerador / self.denominador) < (otra_fraccion.numerador / otra_fraccion.denominador)

    def __gt__(self, otra_fraccion):
        return (self.numerador / self.denominador) > (otra_fraccion.numerador / otra_fraccion.denominador)

def capturar_nombre():
    return input("Ingrese su nombre: ")

def mostrar_menu():
    print("\nMenu:")
    print("1. Sumar fracciones")
    print("2. Restar fracciones")
    print("3. Multiplicar fracciones")
    print("4. Dividir fracciones")
    print("5. Comparar fracciones")
    print("6. Salir")

def obtener_fraccion():
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    return Fraccion(numerador, denominador)

def main():
    print("Bienvenido a la Calculadora de Fracciones")
    nombre = capturar_nombre()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            fraccion1 = obtener_fraccion()
            fraccion2 = obtener_fraccion()
            resultado = fraccion1 + fraccion2
            print("El resultado de la suma es:", resultado.numerador, "/", resultado.denominador)

        elif opcion == '2':
            fraccion1 = obtener_fraccion()
            fraccion2 = obtener_fraccion()
            resultado = fraccion1 - fraccion2
            print("El resultado de la resta es:", resultado.numerador, "/", resultado.denominador)

        elif opcion == '3':
            fraccion1 = obtener_fraccion()
            fraccion2 = obtener_fraccion()
            resultado = fraccion1 * fraccion2
            print("El resultado de la multiplicacion es:", resultado.numerador, "/", resultado.denominador)

        elif opcion == '4':
            fraccion1 = obtener_fraccion()
            fraccion2 = obtener_fraccion()
            resultado = fraccion1 / fraccion2
            print("El resultado de la division es:", resultado.numerador, "/", resultado.denominador)

        elif opcion == '5':
            fraccion1 = obtener_fraccion()
            fraccion2 = obtener_fraccion()
            if fraccion1 == fraccion2:
                print("Las fracciones son iguales")
            elif fraccion1 < fraccion2:
                print("La primera fraccion es menor que la segunda")
            else:
                print("La primera fraccion es mayor que la segunda")

        elif opcion == '6':
            print("Gracias por usar la Calculadora de Fracciones, hasta luego", nombre)
            break

        else:
            print("Opcion invalida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    main() 
