import sys
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

## ****************************************************************************************************************
## MODEL DEVELOPMENT
## ****************************************************************************************************************
## Learning objectives
## 1. Simple and multiole linear regression
## 2. Model evaluation using visualization
## 3. Polinomial Reggresion and Pipelines
## 4. R - squared and MSE for In-Sample Evaluation
## 5. Prediction and decision making
## ****************************************************************************************************************
## Question: How can you detemrine a fair value for used car?
## ****************************************************************************************************************

def principal(argv):
    
    ## In this case the url points to the information on the web and path points to the local file
    ## The file is known to be of type .csv
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    path = "C:\\Users\\USUARIO1\\Desktop\\MyPython\\Análisis de datos\\Analysis\\Data Autos\\imports-85.data"
    
    ## Read data from an specific path. Header=None mean that data not include header
    df = pd.read_csv(path, header = None)
    
    ## ADD HEADER TO DATA SET
    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price" ]
    df.columns = headers   ## Add header automatically
    
    
    
    
    ## ****************************************************************************************************************
    ## MODEL DEVELOPMENT
    ## ****************************************************************************************************************
    ## A model can be thought as mathematical equation used to predict values given one or
    ## more other values
    ## ****************************************************************************************************************
        
    
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
    
    print(df.info())
    
    
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
    
    ## ****************************************************************************************************************
    ## SLR: Simple Linear Regression
    ## ****************************************************************************************************************
    ## Considering a linear dependency between 2 variables y and x. Related whit the next
    ## expression: y = bo + b1 * x. The library sklearn learn to get the parameters bo and b1
    ## ****************************************************************************************************************
    
    ## Decalre a linearRegression variable in lm
    lm = LinearRegression()
    x = df[["highway-mpg"]]
    y = df["price"]
    
    lm.fit(x, y)
    
    ## make a prediction of data
    yhat = lm.predict(x)
    # print(yhat)
    
    ## Beahavior of model after a value. For example, what happen whit the model after 55
    print(lm.predict(np.arange(1, 101, 5).reshape(-1, 1)))
   
    ## Get the parametes of quation
    b0 = lm.intercept_
    b1 = lm.coef_
    print(b0, b1[0])
    
    
    
    ## Calculate R^2
    ## If the values is close to 1. Then biggest is the fit of the model to the variable
    r2 = lm.score(x,y)
    print("Coeficiente de determinación: ", r2)
    
    ## Error plot
    sns.residplot(x=df["highway-mpg"], y=df["price"])
    plt.title("RESDIUAL OF REGRESSION: highway-mpg vs price")
    plt.ylim(0,)
    plt.show()
    
    ## Comparation between actual values and fitted values
    ax1 = sns.distplot(df["price"], hist=False, color="r", label="Actual Value")
    sns.distplot(yhat, hist=False, color="b", label="Fitted values", ax=ax1)
    plt.show()
    
    
    
    
    ## ****************************************************************************************************************
    ## MLR: Multiple Linear Regression
    ## ****************************************************************************************************************
    ## Considering a linear dependency of variable y and x1, x2, ...,xn . Related whit the next
    ## expression: y = bo + b1 * x1 + b2 * x2 + ... + bn * xn. The library sklearn learn to get the parameters bo and b1
    ## ****************************************************************************************************************
    
    df.dropna(subset=["horsepower"], axis = 0, inplace = True)
    df.dropna(subset=["curb-weight"], axis = 0, inplace = True)
    df.dropna(subset=["engine-size"], axis = 0, inplace = True)
    df.dropna(subset=["highway-mpg"], axis = 0, inplace = True)
    df.dropna(subset=["price"], axis = 0, inplace = True)
    
    lm = LinearRegression()
    x = df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
    y = df["price"]
    
    lm.fit(x, y)

    ## Get the parametes of quation
    b0 = lm.intercept_
    b = lm.coef_
    print("\n\n======= Values of the parameters MLR ============")
    print(b0, b)
    
    ## Price = b0 + b[0]*horsepower + b[1]*curb-weight + b[2]*engine-size + b[3]*highway-mpg




    ## ****************************************************************************************************************
    ## Polynomial Regression
    ## ****************************************************************************************************************
    ## Considering a linear dependency of variable y and x1, x2, ...,xn . Related whit the next
    ## expression: y = bo + b1 * x1*x2 + b2 * x2^2 + ... + bn * (xn)^3. The library sklearn learn to get the parameters bo and b1
    ## ****************************************************************************************************************
    print("\n\n\n\n ====== POLYNOMIAL REGR ESSION =============")
    
    pr = PolynomialFeatures(degree=2, include_bias=False)
    
    ## fit_transform: convert two variables x1 and x2 in x1, x2, x1*x2, x1^2, x2^2
    x = df[["horsepower", "curb-weight"]]
    x_polly = pr.fit_transform(x[["horsepower", "curb-weight"]])
    # print(x_polly)
    
    x_data = df[["horsepower", "highway-mpg"]]
    SCALE = StandardScaler()
    SCALE.fit(x_data[["horsepower", "highway-mpg"]])
    x_scale = SCALE.transform(x_data[["horsepower", "highway-mpg"]])
    
    # print(x_scale)
#fed
    
if __name__ == "__main__":
    principal(sys.argv)
#fi
