import ntplib
import datetime
import os
from time import strftime
from time import ctime
#Realizo: Daniel Caballero Guerrero
#Num. Control: 17121013
#Obtener Hora de Inicio
print('--------Hora de inicio de la petición--------')
t1 = datetime.datetime.now()
HI = datetime.datetime.now().strftime('%H:%M:%S')
print (HI)
#Jalar tiempo del servidor
serv = "north-america.pool.ntp.org"
cliente_ntp = ntplib.NTPClient()
r = cliente_ntp.request(serv)
hora_actual = datetime.datetime.strptime(ctime(r.dest_time), "%a %b %d %H:%M:%S %Y")
#Hora de llegada de la peticion
print('--------Hora de llegada de la petición--------')
t2 = datetime.datetime.now()
hora_llegada = datetime.datetime.now().strftime('%H:%M:%S')
print  (hora_llegada)
#Obtener hora del servidor ntp
print("Respuesta del servidor ntp " + serv +  ": " + str(hora_actual) + "\n")
#Ajuste de Retraso
print('--------Ajuste de Retraso--------')
ajuste = ((t2 - t1) / 2)
print(ajuste)
#Obtener fecha y hora en la maquina
print ("\n--------Tiempo Actual de la maquina--------")
Tiempo_Maquina = datetime.datetime.now()
print( Tiempo_Maquina)
#Obtener hora con retraso
print("\n--------Tiempo del Servidor con Ajuste de Retraso--------")
horaConRetraso = hora_actual + ajuste
print(horaConRetraso)
#Acomodar el tiempo en la maquina
print("\n--------Ajuste--------")
Update = horaConRetraso.strftime('%m%d%H%M%Y %f')[:-6]
os.system('sudo date -u ' + Update)