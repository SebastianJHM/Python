import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    
    ## ****************************************************************************************************************
    ## DATA NORMALIZATION - THE OBJECTIVE OF THE NORMALIZATION IS MAKE DATA WHIT DIFFERENT INTERVALES COMPARABLE
    ## ****************************************************************************************************************
    ## Thre options of data normalization
    ## 1. x_new = x_old / max(data)
    ## 2. x_new = ( x_old - min(data) ) / ( max(data) - min(data) )
    ## 3. x_new = ( x_old - desv(data) ) / mean(data) 
    ## ****************************************************************************************************************
    ## IN OUR EXAMPLE WE WILL NORMALIZATE THE FEATURES LENGHT, HEIGHT, WIDTH
    ## ****************************************************************************************************************
    
    print(df["length"])
    print(df["height"])
    print(df["width"])
    ## VARIABLE - LENGTH
    df["length"] = df["length"]/df["length"].max()
    df["height"] = (df["height"] - df["height"].min())/(df["height"].max() - df["height"].min())
    df["width"] = (df["width"] - df["width"].mean())/df["width"].std()
    
    print(df["length"])
    print(df["height"])
    print(df["width"])
    
    ## ****************************************************************************************************************
    ## BINNING DATA
    ## ****************************************************************************************************************
    ## Binning is grouping the values of variable in bins or categories
    ## Group a set of numerical values to bins
    ## Converts numeric into a categorical variables
    ## ****************************************************************************************************************
    ## EXAMPLE - INTRODUCE A VARIABLE TO REPRESENTATE BETTER THE PRICE
    ## ****************************************************************************************************************
    
    ## Convert price in a number variable
    df["price"] = df["price"].replace('?', np.NaN)
    df["price"] = pd.to_numeric(df["price"])
    
    ## Property of numpy, create a segmentation
    bins = np.linspace(min(df["price"]), max(df["price"]), 4)
    group_names = ["Low", "Medium", "High"]
    
    ## Create "price-binned" attribute
    df["price-binned"] = pd.cut(df["price"], bins, labels = group_names, include_lowest=True)
    print(df["price-binned"])
    
    ## Histogram of colum price
    plt.hist( df["price"] , bins=3)
    
    
    ## ****************************************************************************************************************
    ## EXAMPLE - CONVERT THE ATTRIBUTE "FUEL-TYPE" IN TWO ATTRIBUTES(GAS AND DIESEL)
    ## ****************************************************************************************************************
    ## .get_dummies(): gat a dataframe whit each value like a column. And the value of a column
    ## is 1 if the value is in the input attribute.
    ## For example, df["fuel-type"] have two possible values "gas" and "diesel". Then in 
    ## df2 save two colums gas and diesel. 1 if in df["fuel-type"] was gas and 0 else
    df2 = pd.get_dummies(df["fuel-type"])
    print(df2)
#fed



if __name__ == "__main__":
    principal(sys.argv)
#fi