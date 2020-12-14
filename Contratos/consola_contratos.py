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


import contratos as con

def ejecutar_cargar_datos() -> dict:
    
    """
    Requerimiento 0
    Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de los paises y los carga.
    Retorno: DataFrame
    """
    
    df = None
    archivo = input(
        "Por favor ingrese el nombre del archivo CSV con los paises: ")
    df = con.requerimiento0(archivo)
    if len(df) == 0:
        print("El archivo seleccionado no es valido.")
    else:
        print("Se cargo correctamente el archivo.")
    #fi
    
    return df

def ejecutar_contratos_mas_costosos(df):
    
    """
    Requerimiento 1
    Esta función recibe el dataframe y devuelve un nuevo dataframe
    con los 10 contratos más costosos.
    """

    df1 = con.requerimiento1(df) 
    
    print("A continuación se presentan los 10 contratos más costosos")
    print("\n")
    print(df1)

def ejecutar_deuda_por_departamento(df) -> None:

    """ 
    Requerimiento 2
    Esta función recibe el dataframe y grafica los 10 departamentos con
    mayor valor pendiente por pagar.
    """

    con.requerimiento2(df)

def ejecutar_valor_total_contratos_por_rama(df) -> None:

    """
    Requerimiento 3
    Esta función recibe el dataframe, un valor mínimo y un valor máximo y 
    devuelve una gráfica de tipo boxplot, usando la columna ValordelContrato 
    y es agrupada por los datos de acuerdo con la columna Rama
    """

    minimo = int(input("Ingrese el límite inferior: "))
    maximo = int(input("Ingrese el límite superior: "))
    
    con.requerimiento3(df,minimo,maximo)

def ejecutar_reparticion_porcentual_valor_total_contratos_por_rama(df) -> None:

    """
    Requerimiento 4
    Esta funcion recibe el dataframe y realiza un grafico de tipo pie que
    muestra la reparticion porcentual del valor total de los contratos del 
    Estado entre las diferentes ramas que los celebran 
    """
    con.requerimiento4(df)
    
def ejecutar_distribucion_valores_contratos(df) -> None:

    """
    Requerimiento 5
    Esta funcion recibe el dataframe y realiza un grafico de tipo KDE para 
    estimar la funcion de densidad de probabilidad de una variable aleatoria,
    que en este caso, se trata del valor en millones de pesos de un contrato.
    """
    con.requerimiento5(df)

def ejecutar_construccion_matriz_departamentos_vs_sectores(df):

    """
    Requerimiento 6
    Esta función recibe un dataframe y devuelve una matriz de los departamentos
    vs sectores. Esta matriz en la primera fila (fila 0) tiene los nombres de cada
    uno de los diferentes sectores de inversión definidos en la columna Sector del
    DataFrame, mientras que la primera columna (columna 0) tiene los nombres de los
    departamentos tal como están definidos en la columna Departamento del DataFrame.
    """

    matriz = con.requerimiento6(df)
    print(matriz)

def ejecutar_sectores_estado_inversion_contratos(df) -> None:

    """
    Requerimiento 7
    Este requerimiento debe calcular en cuáles sectores el estado ha gastado más y
    menos dinero teniendo en cuenta todos los contratos celebrados en cada sector. 
    Para esto, el usuario debe indicar si desea conocer el sector de mayor gasto o
    el sector de menor gasto y suministrar la matriz de departamentos vs. sectores. 
    La función que implemente esta opción debe retornar una tupla que tenga en la 
    primera posición el nombre del sector y en la segunda posición el valor total
    de los contratos.
    """
    
    matriz = con.requerimiento6(df)
    valor = str(input("Digite ""mayor"" si desea conocer el sector de mayor gasto o ""menor"" si desea conocer el sector de menor gasto: "))
    tupla = con.requerimiento7(matriz,valor)
    
    print("La tupla es la siguiente: ", tupla)

def ejecutar_valor_total_contratos_departamento(df) -> None:

    """ 
    Requerimiento 8
    Esta función consiste en calcular el valor total de los contratos de un departamento 
    a partir de la matriz. Para esto, el usuario debe indicar el nombre del departamento 
    a consultar y suministrar la matriz de departamentos vs sectores.
    """
    matriz = con.requerimiento6(df)
    valor = str(input("Digite el departamento que desea consultar: "))
    valores = con.requerimiento8(matriz,valor)
    print("El departamento ", valor, " tiene un valor total de contratos por ", valores)

def ejecutar_departamento_mayor_gasto(df) -> None:
    
    """
    Requerimiento 9
    Esta función debe mostrar cuáles son los 10 departamentos que tienen un mayor gasto. 
    Esto es, los 10 departamentos con el mayor valor total de sus contratos. Se retornará 
    un diccionario cuyas llaves son los nombres de los 10 departamentos con mayor gasto, 
    y los valores son sus respectivos totales. Una vez obtenidos los 10 departamentos con 
    mayor gasto, se debe mostrar la información en una gráfica de barras. Para la construcción 
    de esta gráfica, primero construiremos un nuevo DataFrame a partir del diccionario que 
    se acaba de genera.
    """

    matriz = con.requerimiento6(df)
    con.requerimiento9(matriz)

def ejecutar_departamentos_mas_dedicados_sector(df) -> None:

    """
    Requerimiento 10
    Este último requerimiento de la aplicación consiste en calcular los 5 departamentos más 
    dedicados a un sector. La dedicación de un departamento a un sector se calcula obteniendo 
    el porcentaje del gasto total del departamento.
    """

    matriz = con.requerimiento6(df)
    sector = str(input("Digite el sector que desea evaluar: "))
    con.requerimiento10(matriz,sector)
    # TODO: complete el codigo haciendo el llamado a la funcion del modulo que
    #  implementa este requerimiento e imprimiendo por pantalla el resultado


def mostrar_menu():
    """
    Imprime las opciones de ejecucion disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar el archivo")
    print("2. Consultar los contratos más costosos")
    print("3. Consultar la deuda por departamento")
    print("4. Consultar el valor total de los contratos por cada rama")
    print("5. Consultar la repartición porcentual del valor total de los contratos entre las diferentes ramas del Estado")
    print("6. Consultar la distribución de los valores de los contratos")
    print("7. Consultar la construcción de la matriz de departamentos vs sectores")
    print("8. Consultar los sectores en los que el estado invierte más y menos, de acuerdo al valor de sus contratos")
    print("9. Consultar el valor total de los contratos de un departamento")
    print("10. Consultar los departamentos con mayor gasto")
    print("11. Consultar los departamentos más dedicados a un sector")
    print("12. Salir de la aplicacion")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    df = ejecutar_cargar_datos()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opcion: "))
        if opcion_seleccionada == 1:
            df = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_contratos_mas_costosos(df)
        elif opcion_seleccionada == 3:
            ejecutar_deuda_por_departamento(df)
        elif opcion_seleccionada == 4:
            ejecutar_valor_total_contratos_por_rama(df)
        elif opcion_seleccionada == 5:
            ejecutar_reparticion_porcentual_valor_total_contratos_por_rama(df)
        elif opcion_seleccionada == 6:
            ejecutar_distribucion_valores_contratos(df)
        elif opcion_seleccionada == 7:
            ejecutar_construccion_matriz_departamentos_vs_sectores(df)
        elif opcion_seleccionada == 8:
            ejecutar_sectores_estado_inversion_contratos(df)
        elif opcion_seleccionada == 9:
            ejecutar_valor_total_contratos_departamento(df)
        elif opcion_seleccionada == 10:
            ejecutar_departamento_mayor_gasto(df)
        elif opcion_seleccionada == 11:
            ejecutar_departamentos_mas_dedicados_sector(df)
        elif opcion_seleccionada == 12:
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")


# PROGRAMA PRINCIPAL
iniciar_aplicacion()
