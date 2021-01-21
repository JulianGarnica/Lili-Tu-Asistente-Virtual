from mostrar_alerta import mostrar_alerta_wind
from datetime import date
from datetime import datetime
import sys
import os
import pandas as pd
import urllib.parse

def agregar_calendario(cadena, today, now):

    indice_dia_c = cadena.index('recordar')+9 #obtenemos la posición del carácter c
    indice_dia_h = cadena.index('de')-1 #obtenemos la posición del carácter h

    indice_mes_c = cadena.index('de')+3 #obtenemos la posición del carácter c
    indice_mes_h = cadena.index('a las')-1 #obtenemos la posición del carácter h

    indice_horas_c = cadena.index('a las')+6 #obtenemos la posición del carácter c
    indice_horas_h = cadena.index('con')-1 #obtenemos la posición del carácter h

    indice_minutos_c = cadena.index('con')+4 #obtenemos la posición del carácter c
    indice_minutos_h = cadena.index('minutos')-1 #obtenemos la posición del carácter h

    indice_acerca_c = cadena.index('acerca de')+10 #obtenemos la posición del carácter c

    subcadena_dia = cadena[indice_dia_c:indice_dia_h]
    subcadena_mes = cadena[indice_mes_c:indice_mes_h]
    subcadena_horas = cadena[indice_horas_c:indice_horas_h]
    subcadena_minutos = cadena[indice_minutos_c:indice_minutos_h]
    subcadena_acerca = cadena[indice_acerca_c:]

    try:
        #Obtener número mes
        array_mes = ("enero","febrero","marzo","abril","mayo","junio","Julio","agosto","septiembre","octubre","noviembre","diciembre")
        if subcadena_mes in array_mes: mes=array_mes.index(subcadena_mes)+1 
        else: raise Exception("El mes es incorrecto")

        #Validar día
        array_dias_mes = (31,29,31,30,31,30,31,31,30,31,30,31)
        if int(subcadena_dia) <= array_dias_mes[mes-1]:
            dia = int(subcadena_dia)
            if dia < 10:
                dia = f"0{dia}"
        else: raise Exception("El día es incorrecto")

        #Validar hora
        if int(subcadena_horas) <= 24: hora = int(subcadena_horas)
        else: raise Exception("La hora está incorrecta")

        #Validar minutos
        if int(subcadena_minutos) <= 60: 
            minuto = int(subcadena_minutos)
        else: raise Exception("Los minutos están incorrectos")

        try:
            fecha = f"{format(today.year)}-{mes}-{dia}"
            hora = f"{hora}:{minuto}"

            fecha_final = f"fecha: {fecha} hora: {hora}"

            path = "calendario.csv"
            columnas = ['fecha','tema']
            data1 = [[fecha_final, subcadena_acerca]]
            df1 = pd.DataFrame(data1, columns=columnas)

            df1.to_csv(path, index=None, mode="a", header=not os.path.isfile(path))

            print(str(fecha_final),str(subcadena_acerca))

        except:
            print("Error:",sys.exc_info()[1])
    except:
        print("Error:",sys.exc_info()[1])


def buscar_calendario(today, now):
    hora_actual = str(f"{format(now.hour)}:{format(now.minute)}")
    fecha_hora = str(f"fecha: {str(today)} hora: {hora_actual}")
    print(fecha_hora)
    path = "calendario.csv"
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    #print(data['fecha'])

    #print(data['tema'])
    try:
        tema = df[df['fecha']==fecha_hora]['tema']
        tema = tema.to_string(index=False)
        #print(tema['0'])
        if(tema == "Series([], )"):
            raise Exception("No hay tareaas")
        mostrar_alerta_wind("¡Tienes tarea pendiente!",tema)
    except:
        print("No hay tareas")


#agregar_calendario("recordar 5 de noviembre a las 15 con 3 minutos acerca de darle comida , xdal gato xd", today, now)
#buscar_calendario(today, now)