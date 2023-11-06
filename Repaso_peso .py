import random as r
class Persona():
  __nombre =  ""
  __edad = 0
  __DNI = ""
  __sexo = "Hombre"
  __peso = 0
  __altura = 0
  def __init__(self, nombre, edad, sexo, peso, altura):
    self.__nombre =  nombre
    self.__edad   = edad
    self.__sexo   = sexo
    self.__peso   = peso
    self.__altura = altura
    self.generarDNI()
  def esMayorEdad(self):
    return self.__edad >= 18
  def generarDNI(self):
    for i in range(8):
      self.__DNI += str(r.randint(0, 9))
  def calcularIMC(self):
    imc = self.__peso / pow(self.__altura, 2)
    if imc < 20:
      return -1
    elif imc <= 25:
      return 0
    else:
      return 1
  def getInformacion(self):
    print(f'''
              nombre: {self.__nombre}
              edad: {self.__edad}
              DNI: {self.__DNI}
              sexo: {self.__sexo}
              peso: {self.__peso}
              altura: {self.__altura}''')
  def getNombre(self):
    return self.__nombre
  def setNombre(self, nombre):
    self.__nombre = nombre

nombre = ""
while not(nombre != ""):
  nombre = input("Ingrese nombre : ")
edad = -1
while not(edad > 5):
  edad = int(input("Ingrese edad : "))
sexo = ""
while not(sexo == "Hombre" or sexo == "Mujer"):
  sexo = input("Ingrese sexo : ")
peso = -1
while not(peso > 30):
  peso = float(input("Ingrese peso : "))
altura = -1
while not(altura > 0.5):
  altura = float(input("Ingrese altura : "))
persona = Persona(nombre, edad, sexo, peso, altura)
if persona.calcularIMC() == -1:
  print("Peso ideal")
elif persona.calcularIMC() == 0:
  print("Debajo del peso ideal")
else:
  print("SObrepeso")
if persona.esMayorEdad():
  print("Es mayor de edad")
else:
  print("Es menor de edad")
persona.getInformacion()