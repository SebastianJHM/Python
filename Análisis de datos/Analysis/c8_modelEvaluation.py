import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression, Ridge
## ****************************************************************************************************************
## MODEL EVALUATION
## ****************************************************************************************************************
## Learning objectives
## 1. Model evaluation
## 2. Over-fitting, Under-fitting and model selection
## 3. Ridge regression
## 4. Grid search
## ****************************************************************************************************************
## Question: How can you be certain your model work in the ral world and performs optimally?
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
    df.columns = headers   ## Add header automatically
    
    
    
    ## Convert numeric variable that appear in the dataframe like np.object into a numeric variables
    df["price"] = df["price"].replace('?', np.NaN)
    df["price"] = pd.to_numeric(df["price"])
    
    df["peak-rpm"] = df["peak-rpm"].replace('?', np.NaN)
    df["peak-rpm"] = pd.to_numeric(df["peak-rpm"])
   
    df["horsepower"] = df["horsepower"].replace('?', np.NaN)
    df["horsepower"] = pd.to_numeric(df["horsepower"])
    
    df["stroke"] = df["stroke"].replace('?', np.NaN)
    df["stroke"] = pd.to_numeric(df["stroke"])
    
    df["normalized-losses"] = df["normalized-losses"].replace('?', np.NaN)
    df["normalized-losses"] = pd.to_numeric(df["normalized-losses"])
    
    ## Delate Nan
    df.dropna(subset=["highway-mpg"], axis = 0, inplace = True)
    df.dropna(subset=["price"], axis = 0, inplace = True)
    
    ## ****************************************************************************************************************
    ## SPLIT DATA INTO RANDOM TRAIN AND TEST SUBSET
    ## A random percentage of the data group is dedicated to the model. And the complement
    ## is used to prrove the model.
    ## ****************************************************************************************************************
      
    ## x_train: data that will be used from the model correspondent to df["highway-mpg"]
    ## x_test: data that will be used from the testing correspondent to df["highway-mpg"]
    ## y_train: data that will be used from the model correspondent to df["price"]
    ## y_test: data that will be used from the testing correspondent to df["price"]
    x_train, x_test, y_train, y_test = train_test_split(df["highway-mpg"], df["price"], test_size = 0.3, random_state = 0)
    print(x_train, x_test, y_train, y_test)
    
    
    ## The next method make a number of split in the data. In this 4 splits. In the first
    ## use the first 25% of the data for prove and the next 75% from the model. In the next 
    ## split use, the second 25% for prove and the res of the model. So on, for the rest.
    lr = LinearRegression()
    x = np.array(df["highway-mpg"]).reshape(-1, 1)
    y = np.array(df["price"]).reshape(-1, 1)
    scores = cross_val_score(lr, x, y, cv=4)
    print(scores)
#fed
    
if __name__ == "__main__":
    principal(sys.argv)
#fi