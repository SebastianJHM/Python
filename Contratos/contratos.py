"""
Archivo contratos.py
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg

def requerimiento0(path: str) -> dict:
    """
    Esta función recibe una dirección de archivo csv y 
    retorna un dataframe.
    """
    df = pd.read_csv(path)
    return df

def requerimiento1(df: pd.DataFrame) -> pd.DataFrame:
    """
    Requerimiento 1
    Esta función recibe el dataframe y devuelve un nuevo dataframe
    con los 10 contratos más costosos.
    """
    ## Procesamiento de datos
    df1 = df.loc[:, ["NombreEntidad", "Departamento", "ProveedorAdjudicado", "ValordelContrato"]]
    df1.sort_values(by = "ValordelContrato", ascending = False, inplace = True)
    df1.reset_index(drop = True, inplace = True)
    
    return df1.loc[0:9]

def requerimiento2(df: pd.DataFrame) -> None:
    """ 
    Requerimiento 2
    Esta función recibe el dataframe y grafica los 10 departamentos con
    mayor valor pendiente por pagar.
    """
    ## Procesamiento de datos
    df1 = df.loc[:, ["Departamento", "ValorPendientedePago"]]
    df2 = df1.groupby(["Departamento"]).sum()
    df2.sort_values(by = "ValorPendientedePago", ascending = False, inplace = True)
    df2 = df2.iloc[0:10]
    
    ## Graficar
    mpl.style.use("ggplot")
    ax = df2.plot(kind="barh", figsize=(7,7))
    plt.title("Departamentos más deudores")
    plt.xlabel("Valor pendiente de pago")
    plt.ylabel("Departamento")
    ax.invert_yaxis()
    plt.show()
    
def requerimiento3(df: pd.DataFrame, min_value: int, max_value: int) -> None:
    """
    Requerimiento 3
    Esta función recibe el dataframe, un valor mínimo y un valor máximo y 
    devuelve una gráfica de tipo boxplot, usando la columna ValordelContrato 
    y es agrupada por los datos de acuerdo con la columna Rama
    """
    ## Procesamiento de datos
    df1 = df.loc[:, ["Rama", "ValordelContrato"]]
    df1 = df1.set_index("Rama")
    d = {}
    ramas = list(set(df1.index))
    ramas.sort()
    for rama in ramas:
        l = list(df1.loc[rama, :]["ValordelContrato"])
        l = [x for x in l if x <= max_value and x >= min_value]
        d[rama] = l
    df2 = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
    
    ## Graficar
    mpl.style.use("ggplot")
    df2.plot(kind='box', figsize=(8, 6))
    plt.title("Valor del contrato por ramas")
    plt.xlabel("Rama Contratadora")
    plt.ylabel('Valor del contrato')
    plt.show()
    
def requerimiento4(df: pd.DataFrame) -> None:
    """
    Requerimiento 4
    Esta funcion recibe el dataframe y realiza un grafico de tipo pie que
    muestra la reparticion porcentual del valor total de los contratos del 
    Estado entre las diferentes ramas que los celebran 
    """
    ## Procesamiento de datos
    df1 = df.loc[:, ["Rama", "ValordelContrato"]]
    df2 = df1.groupby(["Rama"]).sum()
    
    ## Graficar
    mpl.style.use("ggplot")
    df2['ValordelContrato'].plot(kind='pie',
                            figsize=(10, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=0,     # start angle 90° (Africa)
                            shadow=False,       # add shadow      
                            pctdistance=1.15,
                            labels=None,
                            )
    plt.axis('equal')
    plt.title("Distribución de valor de contrato por Rama")
    plt.legend(labels=df2.index, loc='upper left')
    plt.show()
    
def requerimiento5(df: pd.DataFrame) -> None:
    """
    Requerimiento 5
    Esta funcion recibe el dataframe y realiza un grafico de tipo KDE para 
    estimar la funcion de densidad de probabilidad de una variable aleatoria,
    que en este caso, se trata del valor en millones de pesos de un contrato.
    """
    ## Procesamiento de datos
    df1 = df["ValordelContrato"].loc[df["ValordelContrato"] < 100]
    
    ## Graficar
    mpl.style.use("ggplot")
    df1.plot(kind='kde')
    plt.title("Distribución de valores de los contratos")
    plt.xlabel("Valor del contrato")
    plt.ylabel("Densidad de probabilidad")
    plt.xlim(0,100)
    plt.show()
    
def requerimiento6(df: pd.DataFrame) -> None:
    """
    Requerimiento 6
    Esta función recibe un dataframe y devuelve una matriz de los departamentos
    vs sectores. Esta matriz en la primera fila (fila 0) tiene los nombres de cada
    uno de los diferentes sectores de inversión definidos en la columna Sector del
    DataFrame, mientras que la primera columna (columna 0) tiene los nombres de los
    departamentos tal como están definidos en la columna Departamento del DataFrame.
    """
    ## Procesamiento de datos
    df1 = df.loc[:, ["Departamento", "Sector", "ValordelContrato"]]
    df1 = df1.set_index("Departamento")
    
    ## Departamentos y Sectores
    departamentos = list(df1.index.unique())
    departamentos.remove("No Definido")
    sectores = list(df1["Sector"].unique())
    
    ## Construcción de Matriz
    MATRIZ = []
    MATRIZ.append(sectores)
    for departamento in departamentos:
        fila = [departamento] + [0] * len(sectores)
        MATRIZ.append(fila)
        
    for i, departamento in enumerate(departamentos):
        df_departamento = df1.loc[departamento, :].groupby(["Sector"]).sum()
        for sector in df_departamento.index:
            for sector2 in sectores:
                if sector == sector2:
                    j = sectores.index(sector2)
                    MATRIZ[i+1][j+1] = df_departamento.loc[sector, "ValordelContrato"]    
    
    return MATRIZ

def requerimiento7(MATRIZ: list, buscar: str) -> tuple:
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
    gasto_total = {}
    for j in range(len(MATRIZ[0])):
        acum = 0
        for i in range(1,len(MATRIZ)):
            acum += MATRIZ[i][j+1]
        gasto_total[MATRIZ[0][j]] = acum
    
    
    if buscar == "menor":
        sector = min(gasto_total, key=lambda k: gasto_total[k])
                    
    if buscar == "mayor":
        sector = max(gasto_total, key=lambda k: gasto_total[k])

    respuesta = (sector, gasto_total[sector])

    return respuesta

def requerimiento8(MATRIZ: list, departamento: str) -> float:
    """ 
    Requerimiento 8
    Esta función consiste en calcular el valor total de los contratos de un departamento 
    a partir de la matriz. Para esto, el usuario debe indicar el nombre del departamento 
    a consultar y suministrar la matriz de departamentos vs sectores.
    """
    for i in range(1, len(MATRIZ)):
        if MATRIZ[i][0] == departamento:
            acum = 0
            for j in range(1,len(MATRIZ[0])):
                acum += MATRIZ[i][j]
    return acum

def requerimiento9(MATRIZ: list) -> dict:
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
    departamentos = [MATRIZ[i][0] for i in range(1, len(MATRIZ))]
    
    gasto_total_departamento = {}
    for departamento in departamentos:
        gasto_total_departamento[departamento] = requerimiento8(MATRIZ, departamento)
    
    gasto_total_departamento_10 = {k: v for k, v in sorted(gasto_total_departamento.items(), key=lambda item: item[1], reverse=True)[:10]}
    
    df = pd.DataFrame.from_dict(gasto_total_departamento_10,orient='index',columns=['Gasto'])
    
    ## Graficar
    mpl.style.use("ggplot")
    df.plot(kind="bar", figsize=(7,4))
    plt.title("Departamentos con mayor gasto")
    plt.xlabel("Departamento")
    plt.ylabel("Valor total del gasto")
    plt.show()
    
    return gasto_total_departamento_10
    
def cargar_coordenadas(nombre_archivo: str) -> dict:
    """ 
    Esta función devuelve las coordenadas en el mapa de cada departamento
    """
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    titulos = archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos

def requerimiento10(MATRIZ: list, sector: str) -> None:
    """
    Requerimiento 10
    Este último requerimiento de la aplicación consiste en calcular los 5 departamentos más 
    dedicados a un sector. La dedicación de un departamento a un sector se calcula obteniendo 
    el porcentaje del gasto total del departamento.
    """
    ## Procesamiento de datos
    departamentos = [MATRIZ[i][0] for i in range(1, len(MATRIZ))]
    gasto_total_departamento = {}
    for departamento in departamentos:
        gasto_total_departamento[departamento] = requerimiento8(MATRIZ, departamento)
    
    departamentos_dedicados_sector = {}
    for j in range(len(MATRIZ[0])):
        if MATRIZ[0][j] == sector:
            for i in range(1,len(MATRIZ)):
                departamentos_dedicados_sector[MATRIZ[i][0]] = MATRIZ[i][j+1]/gasto_total_departamento[MATRIZ[i][0]]
    
    departamentos_dedicados_sector_5 = {k: v for k, v in sorted(departamentos_dedicados_sector.items(), key=lambda item: item[1], reverse=True)[:5]}
    departamentos_dedicados_sector_5 = {k: v for k, v in departamentos_dedicados_sector_5.items() if v != 0}
    
    ## Parámetros de gr´rafico
    coordenadas = cargar_coordenadas("coordenadas.txt")
    colors = [
        [0.94, 0.10, 0.10],
        [0.94, 0.10, 0.85],
        [0.10, 0.50, 0.94],
        [0.34, 0.94, 0.10],
        [0.99, 0.82, 0.09],
    ]
    
    ## Graficar mapa
    mapa = mpimg.imread("mapa.png").tolist()
    plt.imshow(mapa)
    for i, departamento in enumerate(list(departamentos_dedicados_sector_5.keys())):
        plt.scatter([coordenadas[departamento][1]], [coordenadas[departamento][0]], color=colors[i], marker="s", s=13)
    plt.show()
    
if __name__  == "__main__":
    path = "2019.csv"
    df = requerimiento0(path)
    df1 = requerimiento1(df)
    # requerimiento2(df)
    # requerimiento3(df, 1, 10)
    # requerimiento4(df)
    # requerimiento5(df)
    # MATRIZ = requerimiento6(df)
    # requerimiento7(MATRIZ, "mayor")
    # requerimiento8(MATRIZ, "Vaupes")
    # requerimiento9(MATRIZ)
    # requerimiento10(MATRIZ, 'Ley de Justicia')