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
    ## DESCRIPTIVE STATISTICS
    ## ****************************************************************************************************************
    ## Describe the basic feature of data
    ## Giving short summaries about the sample and measures of the data
    ## ****************************************************************************************************************
    
    ## General descriptive statistic
    print(df.describe())
    print(df["symboling"].describe())
    df["price"] = df["price"].replace('?', np.NaN)
    df["price"] = pd.to_numeric(df["price"])
    print(df["price"].describe())
    
    
    ## Count categories in categorical values
    print("========= value_counts =========")
    drive_wheels_count = df["drive-wheels"].value_counts()
    print(drive_wheels_count)
    
    ## Chart boxplot (diagrama de caja y bigote): Library seaborn
    print("====== BOXPLOT: DRIVE-WHEELS VS PRICE ===========")
    sns.boxplot(x = "drive-wheels", y = "price", data = df)
    plt.show()
    
    ## Scatter-Plot
    print("====== SCATTER: ENGINE-SIZE VS PRICE ===========")
    axis_y = df["engine-size"]
    axis_x = df["price"]
    plt.scatter(axis_x,axis_y)
    plt.show()
    
    ## Groupby
    ## Get a copy of the dataframe whit the attributes "drive-wheels", "body-style", "price"
    print("========== df-test =============")
    df_test = df[["drive-wheels", "body-style", "price"]]
    print(df_test)
    ## The function groupby make an agroupation of all passible groups between "drive-wheels"
    ## and "body-style". Gropby return the value of another funtion indicated. In this case
    ## mean(). The attribute as_index if is True allow to access dataframe df_group#["", ""]
    ## If is false, allow to access dataframe like df_group[0]
    print("========== df-group =============")
    df_group = df_test.groupby(["drive-wheels", "body-style"], as_index = False).mean()    
    print(df_group)
    
    ## Convert the grouping data_fram in a table
    print("========== df-pivot =============")
    df_pivot = df_group.pivot(index="drive-wheels", columns="body-style")
    print(df_pivot)

    ## Plot of color to measure and representate de price for a categorie ("drive-wheels", "body-style")
    plt.pcolor(df_pivot, cmap="Reds")
    print(df_pivot.index)
    print(df_pivot.columns)
    ## Change the names of the label axis
    plt.yticks(np.arange(0.5, len(df_pivot.index), 1), df_pivot.index)
    plt.xticks(np.arange(0.5, len(df_pivot.columns), 1), [x[1] for x in df_pivot.columns])
    plt.colorbar()
    plt.show()
    
    ## ANOVA
    df_anova = df[["make", "price"]]
    grouped_anova = df_anova.groupby(["make"])
    
    print("\n\n\n======== Mean of each make =============")
    df_g = df_anova.groupby(["make"], as_index = True).mean()
    print(df_g)
    
    categorie = df_g.index
    price_categorie = df_g["price"]
    plt.bar(categorie, price_categorie)
    plt.xticks(rotation='vertical')
    plt.title("MEAN OF EACH MAKE")
    plt.show()

          
    ## Stats is a function of library SciPy
    ## if the pvalue is less 0.05 then the mean of the categories are differents
    print("\n======== Comparation between Honda and Subaru =============")
    anova_results_l1 = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("subaru")["price"])
    print(anova_results_l1)
    
    print("\n======== Comparation between Honda and Jaguar =============")
    anova_results_l2 = stats.f_oneway(grouped_anova.get_group("honda")["price"], grouped_anova.get_group("jaguar")["price"])
    print(anova_results_l2)
#fed
    
if __name__ == "__main__":
    principal(sys.argv)
#fi