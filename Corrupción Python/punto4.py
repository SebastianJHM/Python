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
    
def punto4(paises, pos):
    
    respuesta = []
    for pais in paises:
        decisor = False
        for registro in paises[pais]:
            if registro["puesto"] > pos:
                decisor = True
        if decisor == False:
            respuesta.append(pais)
    
    return respuesta


def principal():
    paises = funcion1("ICM.csv")
    punto4(paises, 10)
    
if __name__ == "__main__":
    principal()