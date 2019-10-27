from datetime import datetime
from datetime import date

today = date.today()
now = datetime.now()

def mi_formato( date ):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dia = date.day
    mes = months[ date.month - 1 ]
    annos = date.year
    message = "{} de {} del {}".format(dia,mes,annos)
    return message
#fed

months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

libros_list = [
    {"autor": "Gabriel García Márquez", "nombre": "Cien años de soledad", "fecha": now },
    {"autor": "Robert Louis Stevenson", "nombre": "Dr. Jekill y Hyde", "fecha": mi_formato(now) },
    {"autor": "Gabriel García Márquez", "nombre": "El amor en los tiempos del colera", "fecha": "{} de {} del {}".format(now.day,months[now.month - 1],now.year)},
    {"autor": "Jesús de Nazareth", "nombre": "La Biblia", "fecha": "{} de {} del {}".format(now.day,months[now.month - 1],now.year) },
    {"autor": "Predro Franco", "nombre": "Rosario Tijeras", "fecha": "{} de {} del {}".format(now.day,months[now.month - 1],now.year) }
]