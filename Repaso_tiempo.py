class Hora():
  __hora = 0
  __minuto = 0
  __segundo = 0
  def __init__(self, hora, minuto, segundo):
    self.setHora(hora, minuto, segundo)
  def setHora(self, hora, minuto, segundo):
    if hora > 23 or hora < 0:
      hora = 0
    if minuto > 59 or minuto < 0:
      minuto = 0
    if segundo > 59 or segundo < 0:
      segundo = 0
    self.__hora = hora
    self.__minuto = minuto
    self.__segundo = segundo
  def getHora(self):
    return [self.__hora, self.__minuto, self.__segundo]
  def imprimirHora(self):
    print(f"{self.__hora}:{self.__minuto}:{self.__segundo}")
  def getSegundos(self):
    return self.__hora*3600+ self.__minuto*60+ self.__segundo
  def getHora(self):
    return self.__hora
  def getMinuto(self):
    return self.__minuto
  def getSegundo(self):
    return self.__segundo

hora = 0
horas = []
while not(hora == -1):
  hora = int(input("Ingresar Hora: "))
  if hora == -1:
    break
  minuto = int(input("Ingresar Minuto: "))
  segundo = int(input("Ingresar Segundo: "))
  horas.append(Hora(hora, minuto, segundo))

#for hora in horas:
#hora.imprimirHora()

def incrementarHora(hora):
  seg = hora.getSegundo() + 1
  min = hora.getMinuto()
  hor = hora.getHora()
  if seg == 60:
    seg = 0
    min += 1
    if min == 60:
      min = 0
      hor+=1
      if hor == 24:
        hor = 0
  hora.setHora(hor, min, seg)
  return hora
for i in range(len(horas)):
  horas[i] = incrementarHora(horas[i])
  horas[i].imprimirHora()

for hora in horas:
  print(f"Horas: {23 - hora.getHora() } Minutos: {59 - hora.getMinuto() } Segundos: {59 - hora.getSegundo() }")

mini = horas[0]
maxi = horas[0]
for hora in horas:
  if hora.getSegundos() > maxi.getSegundos():
    maxi =hora
  if hora.getSegundos() < mini.getSegundos():
    mini = hora
segMin = mini.getSegundos()
segMax = maxi.getSegundos()
intervalo = segMax - segMin
hora = intervalo // 3600
intervalo = intervalo % 3600
minutos = intervalo // 60
segundos = intervalo % 60
print(f"{hora}:{minutos}:{segundos}")