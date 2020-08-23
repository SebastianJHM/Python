import sys
import pandas as pd
import numpy as np

## ****************************************************************************************************************
## DATA WRANGLING - PRE-PROCESSING DATA IN PYTHON
## ****************************************************************************************************************
## Learning objetives:
## 1. Identify and handle missing values
## 2. Data formatting
## 3. Data normalization(centering/scaling)
## 4. Data binning: binning creates a biggeer categories from a set od values
## ****************************************************************************************************************
 
def principal(argv):
    
    ## In this case the url points to the information on the web and path points to the local file
    ## The file is known to be of type .csv
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    path = path = "C:\\Users\\USUARIO1\\Desktop\\MyPython\\Análisis de datos\\Analysis\\Data Autos\\imports-85.data"
    
    ## Read data from an specific path. Header=None mean that data not include header
    df = pd.read_csv(path, header = None)
    
    ## ADD HEADER TO DATA SET
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price" ]
    df.columns = headers   ## Add header automatly
    
    ## Access to a column of data
    print("======== Data of the column symboling =============")
    print(df["symboling"])
    
    ## Sum 1 from all values of a string
    print("======== Data of the column symboling plass 1 =============")
    df["symboling"] = df["symboling"] + 1
    print(df["symboling"])
    
    ## =====================================================================================================
    ## 1. Missing value
    ## Missing values occur when in a observation not has been sorted a value in a variable
    ## Could be represente by Nan, ?, -1, etc.
    ## How to deal whit the missind data?
    ## opc1: Drop the missing data: drop the observation or drop the variable
    ## opc2: Replace the missing value with the average of the entire variable
    ##       Replace the missing value with the mode(categorical variables)
    ##       Replace whit other function. Example devaluation of the price.
    ## opc3: Leave the missing data as missing data.
    
    ## If we have differents variable the best form is consider each column as an individual case.
    ## For example, the column normalized-losses should be content numbers data but the data is presented
    ## like text. 

    ## VARIABLE - NORMALIZED-LOSSES
    ## Method: replace missing value whit the mean of the column
    ## The first step is converte de missinf value in a missing number in this case -1.
    ## Next, convert all the colum to number an finally, convert -1 in np.NaN. The last
    ## is to get the mean whitout the missing value and relece.
    df["normalized-losses"] = df["normalized-losses"].replace('?', '-1')
    df["normalized-losses"] = pd.to_numeric(df["normalized-losses"])
    df["normalized-losses"] = df["normalized-losses"].replace(-1, np.NaN)
 
    ## Then we get the mean and replace in all missing values.   
    mean = df["normalized-losses"].mean()
    df["normalized-losses"] = df["normalized-losses"].replace(np.NaN, mean)
    
    
    
    
    ## VARIABLE - PRICE
    ## Method: replace missing value whit the mean of the attribute make. If make is audi, the just is used the data of audi
    ## First replace the data ? whit np.NaN 
    df["price"] = df["price"].replace('?', np.NaN)
    df["price"] = pd.to_numeric(df["price"])
    
    print("==========================================================")
    for i in list(df.index):
        if( str(df["price"][i]) == 'nan' ):
            marca = df["make"][i]
            acum = 0
            cont = 0
            for j in list(df.index):
                if ( str(df["make"][j]) == marca and str(df["price"][j]) != 'nan' ):
                    acum = acum + df["price"][j]
                    cont = cont + 1
                #fi
            #rof
            
            mean  = acum / cont
            df.loc[i, "price"] = mean
        #fi
    #rof
    
    
    
    ## VARIABLE - STROKE
    ## Method: remove the complete row that in the atributte "stroke" the value be '?'
    ## First replace the data ? whit np.NaN 
    ## The function .dropna remove all the rows whit NaN. axis = 0 mean that is the row
    ## inplace = True is necessary to make the change effective. Not include if we want 
    ## make a prove
    df["stroke"] = df["stroke"].replace('?', np.NaN)
    df.dropna(subset=["stroke"], axis = 0, inplace = True)
    
    
    ## VARIABLE - CITY-MPG
    ## Convert mpg to "L/100kkm"
    ## For each value divide and replace
    df["city-mpg"] = 235 / df["city-mpg"]
    ## Rename the name of the atributte
    df.rename(columns={"city-mpg":"city-L/100km"},inplace = True)
    
    
    print(df.head(len(df)))
    print(df["city-L/100km"])
    
    
    
#fed



if __name__ == "__main__":
    principal(sys.argv)
#fi