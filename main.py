class CalculadoraMCD:
    def __init__(self, numero1: int = 0, numero2: int = 0):
        self.numero1 = abs(numero1)
        self.numero2 = abs(numero2)

    def ingresar_datos(self, numero1: int, numero2: int):
        self.numero1 = abs(numero1)
        self.numero2 = abs(numero2)

    def calcular_mcd(self) -> int:
        a = self.numero1
        b = self.numero2
        while b != 0:
            a, b = b, a % b
        return a


# Ejemplo de uso
if __name__ == "__main__":
    calculadora = CalculadoraMCD()

    # Ingresar datos
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    calculadora.ingresar_datos(num1, num2)
    mcd = calculadora.calcular_mcd()
    print(f"El MCD de {num1} y {num2} es: {mcd}")
