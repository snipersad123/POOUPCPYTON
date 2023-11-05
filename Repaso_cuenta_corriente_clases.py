class CuentaCorriente():
    __dni = ""
    __nombre = ""
    __distrito = ""
    __telefono = ""
    __saldo = 0.0
    def __init__(self, dni, nombre, distrito, telefono, saldo):
        self.__dni = dni
        self.__nombre = nombre
        self.__distrito = distrito
        self.__telefono = telefono
        self.__saldo = saldo
    def retirarDinero(self, monto):
        self.__saldo -= monto
    def ingresarDinero(self, monto):
        self.__saldo += monto
    def consultaCuenta(self):
        print(f"Dni: {self.__dni} \nNombre: {self.__nombre} \ndistrito: {self.__distrito} \nTelefono: {self.__telefono} \nSaldo: {self.__saldo}")
    def saldoNegativo(self):
        return self.__saldo < 0
    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre
    def getdistrito(self):
        return self.__distrito
    def gettelefono(self):
        return self.__telefono
    def getsaldo(self):
        return self.__saldo
    def setdni(self,dni):
        self.__ = dni

dni = " "
cuentas = []
while not(dni == ""):
    dni = " "
    while not(len(dni) == 8 or dni == ""):
        dni = input("Ingrese DNI: ")
    if dni != "":

        nombre = ""
        while not(len(nombre) > 0):
            nombre = input("Ingrese nombre: ")

        distrito = ""
        while not(len(distrito) > 0):
            distrito = input("Ingrese distrito: ")

        telefono = ""
        while not(len(telefono) > 0):
            telefono = input("Ingrese telefono: ")

        saldo = -1
        while not(saldo > 0):
            saldo = float(input("Ingrese saldo: "))
        cuentas.append(CuentaCorriente(dni, nombre, distrito, telefono, saldo))

def buscarCuenta(dni, cuentas):
    for i in range(len(dni)):
        if cuentas[i].getdni() == dni:
            return i
    return -1
dniDeposita = " "
while not(len(dniDeposita) == 8):
    dniDeposita = input("Ingrese DNI deposita: ")
dniRetira = " "
while not(len(dniRetira) == 8):
    dniRetira = input("Ingrese DNI retira: ")
saldo = -1
while not(saldo > 0):
    saldo = float(input("Ingrese saldo: "))
indiceDeposita = buscarCuenta(dniDeposita, cuentas)
indiceRetira = buscarCuenta(dniRetira, cuentas)

if indiceDeposita != -1 and indiceRetira != -1:
    cuentas[indiceRetira].retirarDinero(saldo)
    cuentas[indiceRetira].ingresarDinero(saldo)

#for cuenta in cuentas:
  #cuenta.consultarCuenta()

sumSaldo = 0
cantDis = 0
distrito = ""
while not(len(distrito) > 0):
    distrito = input("Ingrese distrito: ")
for cuenta in cuentas:
    if cuenta.getdistrito() == distrito:
        sumSaldo = cuenta.getsaldo()
        cantDis += 1
if cantDis != 0:
    print("El promedio es: ",sumSaldo/cantDis)

letra = ""
while not(len(letra) == 1):
  letra = input("Ingrese letra: ")
for cuenta in cuentas:
  if cuenta.getnombre()[0] == letra:
    cuenta.consultarCuenta()

aux = cuentas[0]
for cuenta in cuentas:
  if cuenta.getsaldo() > aux.getsaldo():
    aux = cuenta
aux.consultarCuenta()