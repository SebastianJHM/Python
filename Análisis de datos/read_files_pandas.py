import sys
import pandas as pd
import numpy as np

## READ DATA WITH PANDAS
## In order to read data with pandas two attributes must be indicated:
## 1. Format: .csv, .xlsx, .json, .hdf
## 2. File: computer, online

def principal(argv):
    ## In this case the url points to the information on the web and path points to the local file
    ## The file is known to be of type .csvv
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    path = "C:\\Users\\USUARIO1\\Desktop\\Python\\Análisis de datos\\Data Autos\\imports-85.data"
    
    df = pd.read_csv(path, header = None) ## La función read_csv asume que el texto viene con encabezado
    
    ## The head(n) function returns the first n data
    ## The tail(n) function returns the last n data data
    print("============ PRINT ALL ============")
    print(df.head(len(df)))
    print("============ PRINT 2 LAST ROWS OF DATA SET ============")
    print(df.tail(2))
    

    ## ADD HEADER TO DATA SET
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price" ]
    df.columns = headers   ## Add header automatly
    #print(df.head(2))
    
    ## This the way to convert the data in a matrix. 
    ## df.index = RangeIndex(start=0, stop=205, step=1) ; list(df.index) = [0,...,205]
    ## df.columns = Int64Index([ 0,  1, ... , 24, 25],dtype='int64') ; list(df.columns) = [0,...,25]
    ## The form to read df is [col][row]
    data_matrix = []
    for row in list(df.index):
        rows = []
        for col in list(df.columns):
            rows.append(df[col][row])
        #rof
        data_matrix.append(rows)
    #rof
    print("\n\n============ PRINT MATRIX OF DATA ============")
    print(np.array(data_matrix))
    
    ## SAVE PARTIAL RESULTS IN CSV FILE. Not is necessary create the file in the folder, only
    ## indicate the name in the path
    path2 = "C:\\Users\\USUARIO1\\Desktop\\Python\\Análisis de datos\\automobile.csv"
    df.to_csv(path2)
#fed



if __name__ == "__main__":
    principal(sys.argv)
#fi