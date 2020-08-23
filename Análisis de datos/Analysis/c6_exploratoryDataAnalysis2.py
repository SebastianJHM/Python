import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## ****************************************************************************************************************
## EXPLORATORY DATA ANALISYS
## ****************************************************************************************************************
## Preliminary step in data analysis to:
## 1. Summarize main characteristics of the data
## 2. Gain better understandin of the data set
## 3. Uncover relationships between variables
## 4. Extraxt importan variables
## ****************************************************************************************************************
## Question: What ares the characteristics that have the most impact of the price car?
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
    
    
    ## ****************************************************************************************************************
    ## CORRELATION
    ## ****************************************************************************************************************
    ## Perason-correlation
    ## --------------------------------------------------------
    ## Correlation coefficient
    ## --------------------------------------------------------
    ## Close to +1: large positive relationship
    ## Close to -1: large negative relationship
    ## Close to 0: No relation
    ## --------------------------------------------------------
    ## --------------------------------------------------------
    ## P-VALUE
    ## --------------------------------------------------------
    ## p-value < 0.01: strong certainty
    ## p-value < 0.05: moderate certainty
    ## p-value < 0.1: weak certainty
    ## p-value > 0.1: no certainty
    ## --------------------------------------------------------
    
    ## General descriptive statistic
    print(df.describe())
    print(df["symboling"].describe())
    df["price"] = df["price"].replace('?', np.NaN)
    df["price"] = pd.to_numeric(df["price"])
    print(df["price"].describe())
    
    # Correlation
    
    ## Engine-size vs Price
    ## Preparing Data
    df.dropna(subset=["engine-size"], axis = 0, inplace = True)
    df.dropna(subset=["price"], axis = 0, inplace = True)
    ## Plot to visualizate the correlation between engine-size and price
    ## The plot show positive correlation
    sns.regplot(x="engine-size", y="price", data=df)
    plt.title("engine-size vs price")
    plt.ylim(0,)
    plt.show()
    ## Calculate pearson coefficient, p_value
    pearson_coef, p_value = stats.pearsonr(df["engine-size"], df["price"])
    print("Pearson-Coefficient: ", pearson_coef, " P-VALUE: ", p_value)
    
    
    
    ## High-mpg vs Price
    ## Preparing Data
    df.dropna(subset=["highway-mpg"], axis = 0, inplace = True)
    df.dropna(subset=["price"], axis = 0, inplace = True)
    ## Plot to vizualize the correlation bettween highway-mpg and price
    ## The plot show negative correlation
    sns.regplot(x="highway-mpg", y="price", data=df)
    plt.title("highway-mpg vs price")
    plt.ylim(0,)
    plt.show()
    ## Calculate pearson coefficient, p_value
    pearson_coef, p_value = stats.pearsonr(df["highway-mpg"], df["price"])
    print("Pearson-Coefficient: ", pearson_coef, " P-VALUE: ", p_value)
    
    
    
    
    ## Peak-mpg vs Price
    ## Preparing Data
    ## convert "peak-rpm" in a numeric variable
    df["peak-rpm"] = df["peak-rpm"].replace('?', np.NaN)
    df["peak-rpm"] = pd.to_numeric(df["peak-rpm"])
    df.dropna(subset=["peak-rpm"], axis = 0, inplace = True)
    df.dropna(subset=["price"], axis = 0, inplace = True)
    ## Plot to vizualize the correlation bettween highway-mpg and price
    ## The plot show doesn't exist correlation
    sns.regplot(x="peak-rpm", y="price", data=df)
    plt.title("peak-rpm vs price")
    plt.ylim(0,)
    plt.show()
    ## Calculate pearson coefficient, p_value
    pearson_coef, p_value = stats.pearsonr(df["peak-rpm"], df["price"])
    print("Pearson-Coefficient: ", pearson_coef, " P-VALUE: ", p_value)
    
    
    
    
    ## Horsepower vs Price
    ## Preparing Data
    df["horsepower"] = df["horsepower"].replace('?', np.NaN)
    df["horsepower"] = pd.to_numeric(df["horsepower"])
    df.dropna(subset=["horsepower"], axis = 0, inplace = True)
    df.dropna(subset=["price"], axis = 0, inplace = True)
    ##Plot
    sns.regplot(x="horsepower", y="price", data=df)
    plt.title("horsepower vs price")
    plt.ylim(0,)
    plt.show()
    
    ## Calculate pearson coefficient, p_value
    pearson_coef, p_value = stats.pearsonr(df["horsepower"], df["price"])
    print("Pearson-Coefficient: ", pearson_coef, " P-VALUE: ", p_value)
    
    ## Convert "stroke" and "normalized-losses" to nueric variables
    df["stroke"] = df["stroke"].replace('?', np.NaN)
    df["stroke"] = pd.to_numeric(df["stroke"])
    df["normalized-losses"] = df["normalized-losses"].replace('?', np.NaN)
    df["normalized-losses"] = pd.to_numeric(df["normalized-losses"])
    
    ## Build the matrix of correlation and p-values from the numeric variables in the datafram
    matrix_pearson_coef = []
    matrix_p_value = []
    labels = []
    for col1 in df.columns:
        if (df[col1].dtype == np.int64 or df[col1].dtype == np.float64):
            labels.append(col1)
            c = []
            p = []
            for col2 in df.columns:
                if (df[col2].dtype == np.int64 or df[col2].dtype == np.float64):
                    df.dropna(subset=[col1], axis = 0, inplace = True)
                    df.dropna(subset=[col2], axis = 0, inplace = True)
                    pearson_coef, p_value = stats.pearsonr(df[col1], df[col2])
                    c.append(pearson_coef)
                    p.append(p_value)
                #fi
            #rof
            matrix_pearson_coef.append(c)
            matrix_p_value.append(p)
        #fi
    #rof
    
    ## Plot of colors measure the correlation between two variables
    plt.pcolor(matrix_pearson_coef, cmap="Reds")
    plt.yticks(np.arange(0.5, len(labels), 1), labels)
    plt.xticks(np.arange(0.5, len(labels), 1), labels, rotation='vertical')
    plt.colorbar()
    plt.title("Correlation between 2 variables")
    plt.show()
    
    ## Plot of colors measure the p-values between two variables
    plt.pcolor(matrix_p_value, cmap="RdBu_r")
    plt.yticks(np.arange(0.5, len(labels), 1), labels)
    plt.xticks(np.arange(0.5, len(labels), 1), labels, rotation='vertical')
    plt.colorbar()
    plt.title("Correlation between 2 variables")
    plt.show()
#fed
    
if __name__ == "__main__":
    principal(sys.argv)
#fi