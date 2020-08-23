import sys
import pandas as pd
import numpy as np

## ----------------------------------------------------------------------------------------
## |                                PANDAS INSIGHTS OF DATASET                            |
## ----------------------------------------------------------------------------------------
## |      PANDAS TYPE           |      NATIVE PYTHON TYPE           |     DESCRIPTION     |
## ----------------------------------------------------------------------------------------
## |        object              |           string                  | numbers and strings |
## |        int64               |           int                     |   integers numbers  |
## |        float64             |           float                   |    real numbers     |
## | datetime64, timedelta[ns]  | N/A(See datetime module's Python) |     time data       |            
## ----------------------------------------------------------------------------------------

def principal(argv):
    ## In this case the url points to the information on the web and path points to the local file
    ## The file is known to be of type .csv
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    path = path = "C:\\Users\\USUARIO1\\Desktop\\MyPython\\Análisis de datos\\Analysis\\Data Autos\\imports-85.data"
    
    df = pd.read_csv(url, header = None) 
    
    ## ADD HEADER TO DATA SET
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price" ]
    df.columns = headers   ## Add header automatly

    ## df.dtypes: print the pandas type of column
    print("\n\n============ df.dtypes ============")
    print(df.dtypes)
    
    ## df.describe(): if the column is a number, then the function return a statistical summary
    ## count, mean, std, min, 25%, 50%, 75%, max
    print("\n\n============ df.describe() ============")
    print(df.describe())
    ## Include a summary of all the categories of the table, if it is possible.
    ## Unique is the number of differents values in the column
    ## top: is the most frequently object
    ## freq: is the number that appear the top element in the object
    
    print("\n\n============ df.describe(include='all') ============")
    print(df.describe(include="all"))
    
    ## Make a summary of each datetime of a column    
    print("\n\n============ df.info() ============")
    print(df.info())
#fed

if __name__ == "__main__":
    principal(sys.argv)
#fi