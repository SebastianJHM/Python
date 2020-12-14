"""
Archivo corrupción.py

"""
import csv

def funcion1(path: str) -> dict:
    
    """
    Esta función recibe una dirección de archivo csv y 
    retorna un diccionario con la lectura especificada
    """
    
    # Guardar y leer archivo
    file = open(path, "r", encoding="utf-8")
    datos = list(csv.reader(file))
    
    # Leer csv en formato especificado
    paises = {}
    for dato in datos[1:]:
        pais = dato[0]
        if not pais in paises:
            paises[pais] = [{"anho": int(dato[1]), "puntaje": int(dato[2]), "puesto": int(dato[3]), "error_estandar": float(dato[4])}]
        else:
            paises[pais].append({"anho": int(dato[1]), "puntaje": int(dato[2]), "puesto": int(dato[3]), "error_estandar": float(dato[4])})
    
    # Ordenar datos de cada país por año
    for pais in list(paises.keys()):
        paises[pais].sort(key= lambda i: i["anho"])
        
    return paises
    
def funcion2(paises: dict, pais_buscado: int, anho_buscado: int) -> int:
    
    """
    Esta función recibe el diccionario principal países, 
    el nombre de un país y un año de interés, y retorne 
    un entero con el puntaje IPC que recibió el país en dicho año.
    """
    if pais_buscado in paises:
        for registro in paises[pais_buscado]:
            if anho_buscado == registro["anho"]:
                return registro["puntaje"]
        return -2
    else:
        return -1

def funcion3(paises: dict, pais_buscado: int, anho_i: int, anho_f: int) -> list:

    """
    Esta función recibe un diccionario principal de países, un año de inicio, un año
    final, y el nombre de un país de interés, y retorna una lista de diccionarios con 
    los puntajes IPC que recibió dicho país en ese rango de años.
    """

    resultado = []
    if pais_buscado in paises:
        for registro in paises[pais_buscado]:
            if registro["anho"] >= anho_i and registro["anho"] <= anho_f:
                resultado.append({"anho": registro["anho"], "puntaje": registro["puntaje"]})
    return resultado

def funcion4(paises: dict, anho_buscado: int) -> dict:
    
    """
    Esta función recibe como parámetro el diccionario principal
    de países y un año de interés, y retorne un diccionario,
    cuyas llaves son los nombres de los países y los valores 
    son los respectivos puntajes IPC en el año de interés.
    """
    
    diccionario = {}
    
    for pais in paises:
        for registro in paises[pais]:
            if anho_buscado == registro["anho"]:
                diccionario[pais] = registro["puntaje"]
    
    return diccionario

def funcion5(paises: dict, anho_buscado: int, puesto_buscado: int) -> list:

    """
    Esta función recibe como parámetro el diccionario principal de países, un puesto 
    de interés y un año de interés, y retorna una lista de diccionarios, que contenga 
    la información de los países que obtuvieron ese puesto en dicho año.
    """

    resultado = []
    for pais in list(paises.keys()):
        for registro in paises[pais]:
            if registro["anho"] == anho_buscado and registro["puesto"] == puesto_buscado:
                resultado.append({"pais": pais, "puntaje": registro["puntaje"]})
    return resultado

def funcion6(paises: dict) -> list:
    
    """
    Esta función recibe como parámetro el diccionario principal
    de países, y retorne una lista de cadenas de caracteres, que
    contenga los nombres de todos los países que se han encontrado
    en las cinco (5) primeras posiciones del ranking mundial al
    menos una vez a lo largo de todos los años.
    """
    
    paisestop5 = []
    
    for pais in paises:
        for registro in paises[pais]:
            if registro["puesto"] <= 5:
                if not pais in paisestop5:
                    paisestop5.append(pais)
    
    return paisestop5

def funcion7(paises: dict, pais_buscado: int) -> int:
 
    """
    Esta función recibe como parámetro el diccionario principal de países y 
    el nombre de un país de interés, y retorne un entero con el error estándar 
    promedio del país.
    """
    
    if pais_buscado in paises:
        acum = 0
        cont = 0
        for registro in paises[pais_buscado]:
            acum += registro["error_estandar"]
            cont += 1
        return int(round(acum/cont))
    else:
        return -1
    
def funcion8(paises: dict) -> float:
    
    """
    Esta función recibe como parámetro el diccionario principal de países y retorne 
    un el error estándar promedio de todos los países.
    """
    
    acum = 0
    cont = 0
    for pais in list(paises.keys()):
        acum += funcion7(paises, pais)
        cont += 1
        
    return acum/cont

def funcion9(paises: dict) -> list:
    
    """
    Esta función recibe como parámetro el diccionario principal de países y retorne 
    una lista de diccionarios con la información de los peores países
    """
    
    puntajes = []
    for pais in list(paises.keys()):
        for registro in paises[pais]:
            puntajes.append(registro["puntaje"])
            
    min_ = min(puntajes)
    resultado = []
    for pais in list(paises.keys()):
        for registro in paises[pais]:
            if registro["puntaje"] == min_:
                resultado.append({"pais": pais, "anho": registro["anho"], "puesto": registro["puesto"], "puntaje": registro["puntaje"]})
    return resultado

def funcion10(paises: dict, pais_buscado: str) -> int:
    
    """
    Esta función recibe como parámetro el diccionario principal
    de países y el nombre de un país de interés, y retorne un
    entero con el cambio que ha tenido el país en el ranking mundial.
    """
    
    pos_min = 1000
    pos_max = 0
    
    if pais_buscado in paises:
        for registro in paises[pais_buscado]:
            if registro["puesto"] <= pos_min:
                pos_min = registro["puesto"]
            if registro["puesto"] >= pos_max:
                pos_max = registro["puesto"]
        return pos_max-pos_min
    return -1

def funcion11(paises: dict) -> dict:
    
    """
    Esta función recibe el diccionario principal de países y
    retorne un diccionario con el país que tuvo el mayor cambio
    en el histórico del ranking.
    """
    
    cambio = 0
    nombre = ""
    
    for pais in paises:
        valor = funcion10(paises,pais)
        if (valor >= cambio):
            cambio = valor
            nombre = pais
    respuesta = {"pais": nombre, "cambio": cambio}
    return respuesta
    
# def principal():
#     paises = cargar_datos("ICM.csv")
#     funcion4(paises, 2014)
#     funcion6(paises)
#     valor = funcion11(paises)
    
# if __name__ == "__main__":
#     principal()