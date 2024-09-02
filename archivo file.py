class numeroEntero:
    def MDC(self,a,b):
        x = abs(a)
        y = abs(b)

        while y != 0:
            remainder = x % y
            x = y
            y = remainder

        return x
if __name__ == '__main__':
    numero1=int(input("primer numero: "))
    numero2=int(input("segundo numero: "))

    operacion = numeroEntero()
    print(f"MCD de {numero1} {numero2} es {operacion.MDC(numero1,numero2)}" )