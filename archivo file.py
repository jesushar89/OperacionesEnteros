class numeroEntero:
    def MDC(self,a,b):
        x = abs(a)
        y = abs(b)

        while y != 0:
            remainder = x % y
            x = y
            y = remainder
        return x

    def mcm(self, a, b):
        # mcd*mcm = a * b
        return a*b/self.MDC(a,b)

if __name__ == '__main__':
    numero1=int(input("primer numero: "))
    numero2=int(input("segundo numero: "))

    operacion = numeroEntero()
    print(f"MCD de {numero1} {numero2} es {operacion.MDC(numero1,numero2)}" )
    print(f"MCM de {numero1} {numero2} es {operacion.mcm(numero1, numero2)}")