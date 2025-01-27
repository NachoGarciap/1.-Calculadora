import math


class Calculadora:

    # constructor
    def __init__(self):
        self.resultado_anterior = None  # Atributo para guardar el resultado anterior

    # OPERACIONES
    def sumar(self, numero1, numero2):
        self.resultado_anterior = numero1 + numero2
        return self.resultado_anterior

    def restar(self, numero1, numero2):
        self.resultado_anterior = numero1 - numero2
        return self.resultado_anterior

    def multiplicar(self, numero1, numero2):
        self.resultado_anterior = numero1 * numero2
        return self.resultado_anterior

    def dividir(self, numero1, numero2):
        if numero2 != 0:
            self.resultado_anterior = numero1 / numero2
            return self.resultado_anterior
        else:
            return 'Error: No se puede dividir entre 0'

    def potencia(self, numero1, numero2):
        self.resultado_anterior = numero1 ** numero2
        return self.resultado_anterior

    def raiz_cuadrada(self, numero1):
        if numero1 >= 0:
            self.resultado_anterior = math.sqrt(numero1)
            return self.resultado_anterior
        else:
            return 'Error: No se puede calcular la raíz cuadrada de un número negativo'

    # MENU
    def mostrar_menu(self):
        while True:
            print('*****CALCULADORA*****')
            print('1. Sumar')
            print('2. Restar')
            print('3. Multiplicar')
            print('4. Dividir')
            print('5. Potencia')
            print('6. Raiz Cuadrada')
            print('7. Salir')

            try:
                opcion = int(input('Introduce una opción del 1 al 5:'))

                # Opción de salida
                if opcion == 7:
                    print('Saliendo de la calculadora...')
                    break

                # Si es una opción que no entra entre el 1 y el 5
                if opcion < 1 or opcion > 7:  # Si la opción no está en el rango válido
                    print('Opción inválida, intentalo de nuevo.')
                    continue  # Volver a mostrar el menú sin hacer nada más

                # Usar el resultado anterior si existe
                if self.resultado_anterior is not None:
                    print(f"El resultado anterior es: {self.resultado_anterior}")
                    numero1 = self.resultado_anterior
                else:
                    numero1 = float(input('Introduce el numero 1:'))

                if opcion == 6:
                    numero2 = None
                else:
                    numero2 = float(input('Introduce el numero 2:'))

                # Operaciones
                if opcion == 1:
                    print(f'El resultado de la suma es: {self.sumar(numero1, numero2)}')

                elif opcion == 2:
                    print(f'El resultado de la resta es: {self.restar(numero1, numero2)}')

                elif opcion == 3:
                    print(f'El resultado de la multiplicación es: {self.multiplicar(numero1, numero2)}')

                elif opcion == 4:
                    print(f'El resultado de la división es: {self.dividir(numero1, numero2)}')

                elif opcion == 5:
                    print(f'El resultado de la potencia es: {self.potencia(numero1, numero2)}')

                elif opcion == 6:
                    print(f'El resultado de la raiz cuadrada es: {self.raiz_cuadrada(numero1)}')

            # Por si ponemos algún valor no numérico aceptado
            except ValueError:
                print('Por favor, introduce un número válido.')
