"""
Ejercicio nivel 3: Indice de Corrupcion Mundial.
Interfaz basada en consola para la interaccion con el usuario.

Temas:
* Instrucciones repetitivas.
* Listas
* Diccionarios
* Archivos
@author: Cupi2
"""


import corrupcion as cor

def ejecutar_cargar_datos() -> dict:
    
    """Solicita al usuario- que ingrese el nombre de un archivo CSV con los datos de los paises y los carga.
    Retorno: dict
        El diccionario de paises con la informacion del archivo.
    """
    
    paises = None
    archivo = input(
        "Por favor ingrese el nombre del archivo CSV con los paises: ")
    paises = cor.funcion1(archivo)
    if len(paises) == 0:
        print("El archivo seleccionado no es valido. No se pudieron cargar los paises")
    else:
        print("Se cargaron los siguientes paises a partir del archivo.")
        for key in paises.keys():
            print(key)
        #rof
    #fi
    
    return paises

#fed

def ejecutar_buscar_puntaje_pais_anho(paises: dict) -> None:
    
    """ 
    Ejecuta la opcion de buscar el puntaje de un pais en un anho dado.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "El puntaje de (nombre del pais) en el (anho) es: (puntaje)"
    En caso de que la funcion del modulo devuelva -1, se debe mostrar el siguiente mensaje:
    "No se encontro el pais (pais) en el diccionario"
    En caso de que la funcion del modulo devuelva -2, se debe mostrar el siguiente mensaje:
    "No hay puntaje para ese pais en ese anho"
    """
    paises = cor.funcion1("IndiceCorrupcionMundial.csv") 
    
    pais = input("Ingrese el pais de su interes:")
    anho = int(input("Ingrese el anho de su interes: "))
    
    valor = cor.funcion2(paises, pais, anho)
    
    if (valor == -1):
        print("No se encontro el pais ", pais, " en el diccionario")
    
    else:
        if (valor == -2):
            print("No hay puntaje para ese pais en ese anho")
        else:
            print("El puntjae de ", pais, " en el ", anho, " es: ", valor)
    print("\n")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_buscar_puntajes_pais_rango_anho(paises: dict) -> None:
    """ Ejecuta la opcion de buscar los puntajes de un pais
    en un rango especifico de anhos.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "Los puntajes de (nombre del pais) entre (anho menor) y (anho mayor)
    son: (puntajes)".
    En caso de que la funcion del modulo devuelva una lista vacia, se debe mostrar el siguiente mensaje:
    "No se encontraron puntajes para ese pais en ese rango"
    """

    pais = input("Ingrese el pais de su interes:")
    aniomenor = int(input("Ingrese el limite inferior del rango en anhos: "))
    aniomayor = int(input("Ingrese el limite superior del rango en anhos: "))
    
    valores = cor.funcion3(paises, pais, aniomenor, aniomayor)

    if valores == []:
        print("No se encontraron puntajes para ese pais en ese rango")
    else:
        print("Los puntajes de ", pais, " entre ", aniomenor, " y ", aniomayor, " son: ",)
        for valor in valores:
            print(valor["puntaje"], end=" ")
        print("\n")
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_buscar_puntajes_paises_anho(paises: dict) -> None:
    """ Ejecuta la opcion de buscar los puntajes de todos los paises en un anho dado.
     El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "Los puntajes de los paises en el (anho) son: (diccionario)".
    En caso de que la funcion del modulo devuelva un diccionario vacio, se debe mostrar el siguiente mensaje:
    "No se encontraron puntajes para en ese anho"
    """

    anio = int(input("Ingrese el anho de su interes: "))
    
    resultado = cor.funcion4(paises, anio)
    
    if resultado == {}:
        print("\nNo se encontraron puntajes para en ese anho")
    else:
        print(f"\nLos puntajes de los paises en el {anio} son: {resultado}")
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_buscar_paises_puesto_anho(paises: dict) -> None:
    """ Ejecuta la opcion de buscar los paises en un puesto especifico y en un anho dado.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "Los paises en el puesto (puesto) en el (anho) son: (paises)".
    En caso de que la funcion del modulo devuelva una lista vacia, se debe mostrar el siguiente mensaje:
    "No se encontraron paises en ese puesto y en ese anho."
    """
    anio = int(input("Ingrese el anho de su interes: "))
    puesto = int(input("ingrese el puesto de su interes: "))
    
    resultado = cor.funcion5(paises, anio, puesto)
    
    if resultado == []:
        print("No se encontraron paises en ese puesto y en ese anho.")
    else:
        print(f"\nLos paises en el puesto {puesto} en el {anio} son:")
        for r in resultado:
            print(r["pais"], end=", ")
        print("\n")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_mejores_paises(paises: dict) -> None:
    """ Ejecuta la opcion de buscar los mejores paises.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "Los mejores paises son: (paises)".
    """
    resultado = cor.funcion6(paises)
    print("\nLos mejores paises son:")
    for r in resultado:
        print(r, end=", ")
    print("\n")
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_error_estandar_promedio_pais(paises: dict) -> None:
    """ Ejecuta la opcion de calcular el error estandar promedio de un pais dado.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "El error estandar promedio de (pais) es: (error estandar promedio)".
    En caso de que la funcion del modulo devuelva -1, se debe mostrar el siguiente mensaje:
    "No se encontro el pais (pais) en el diccionario"
    """

    pais = input("Ingrese el pais de su interes:")
    
    valor = cor.funcion7(paises, pais)
    
    if (valor == -1):
        print("No se encontro el pais ", pais, " en el diccionario.")
    else:
        print("El error estandar promedio de ", pais, " es: ", valor)
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado)


def ejecutar_error_estandar_promedio_todos_paises(paises: dict) -> None:
    """ Ejecuta la opcion de calcular el error estandar promedio de todos los paises a partir
    del error estandar promedio de cada pais.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "El error estandar promedio de todos los paises es: (error estandar promedio)".
    """
    
    valor = cor.funcion8(paises)
    
    print("El error estandar promedio de todos los paises es: ", valor)
    
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_peores_paises(paises: dict) -> None:
    """ Ejecuta la opcion de buscar los peores paises.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "Los peores paises son: (paises separados por comas)".
    """
    
    valores = cor.funcion9(paises)
    print("Los peores paises son: ")
    
    datos = []
    for valor in valores:
        if not valor["pais"] in datos:
            datos.append(valor["pais"])
    
    for dato in datos:
        print(dato, end=", ")
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_calcular_cambio_pais(paises: dict) -> None:
    """ Ejecuta la opcion de calcular el cambio de un pais.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "El cambio del pais es de (cambio) puestos".
    En caso de que la funcion del modulo retorna -1, se debe mostrar el siguiente mensaje:
    "No se encontro el pais (pais) en el diccionario"
    """
    pais = input("Ingrese el pais de su interes: ")
    
    valor = cor.funcion10(paises, pais)
    
    if valor == -1:
        print("No se encontro el pais ", pais, " en el diccionario.")
    else:
        print("El cambio del pais es de ", valor, " puestos.")
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def ejecutar_buscar_pais_mayor_cambio(paises: dict) -> None:
    """ Ejecuta la opcion de buscar el pais con mayor cambio.
    El mensaje que se le muestra al usuario debe tener el siguiente formato:
    "El pais con mayor cambio es (pais) con un cambio de (cambio) puestos".
    """
    valor = cor.funcion11(paises)
    print("El pais con mayor cambio es ", valor["pais"], " con un cambio de ",valor["cambio"], " puestos.")
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def mostrar_menu():
    """Imprime las opciones de ejecucion disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar el archivo del indice de corrupcion mundial")
    print("2. Consultar el puntaje de corrupcion de un pais en un anho")
    print("3. Consultar los puntajes de corrupcion de un pais en un rango de anhos")
    print("4. Consultar los puntajes de corrupcion de todos los paises en un anho dado")
    print("5. Consultar los paises de un puesto en un anho dado")
    print("6. Consultar los mejores paises (con menor corrupcion)")
    print("7. Consultar el error estandar promedio de un pais")
    print("8. Consultar el error estandar promedio de todos los paises")
    print("9. Consultar los peores paises (con mayor corrupcion)")
    print("10. Consultar el cambio de un pais dado")
    print("11. Consultar el pais con mayor cambio")
    print("12. Salir de la aplicacion")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    paises = ejecutar_cargar_datos()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            paises = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_buscar_puntaje_pais_anho(paises)
        elif opcion_seleccionada == 3:
            ejecutar_buscar_puntajes_pais_rango_anho(paises)
        elif opcion_seleccionada == 4:
            ejecutar_buscar_puntajes_paises_anho(paises)
        elif opcion_seleccionada == 5:
            ejecutar_buscar_paises_puesto_anho(paises)
        elif opcion_seleccionada == 6:
            ejecutar_mejores_paises(paises)
        elif opcion_seleccionada == 7:
            ejecutar_error_estandar_promedio_pais(paises)
        elif opcion_seleccionada == 8:
            ejecutar_error_estandar_promedio_todos_paises(paises)
        elif opcion_seleccionada == 9:
            ejecutar_peores_paises(paises)
        elif opcion_seleccionada == 10:
            ejecutar_calcular_cambio_pais(paises)
        elif opcion_seleccionada == 11:
            ejecutar_buscar_pais_mayor_cambio(paises)
        elif opcion_seleccionada == 12:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
