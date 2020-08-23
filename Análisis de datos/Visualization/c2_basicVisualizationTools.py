import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


def principal( argv ):
    
    mpl.style.use(['ggplot'])
    
    ## DATAFRAME
    ## Paths of the file of data analysis
    url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx"
    path = "C:\\Users\\USUARIO1\\Desktop\\MyPython\\Análisis de datos\\Visualization\\Canada.xlsx"
    
    df = pd.read_excel(path, sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
    df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
    
    years = list(range(1980, 2014))
   
    
   
    ## Create a copy of the dataframe including only the years
    df_years = df[years].copy()
    ## Create a new column whit the horizontal sum of df_years and add a total column
    df['Total'] = df_years.sum(axis=1)
   
    ## Sort data using total inmigration criteria
    df.sort_values(['Total'],  ascending = False, axis = 0, inplace = True)
    ## Create a dataframe whit the top 5 countries
    df_top5 = df.head(5)
    ## Transpose the dataframe including only years
    df_top5_t = df_top5[years].transpose()
    ## Assign the name of the 5 top countries to the column of the dataframe
    df_top5_t.columns = df["Country"].head(5)
    
    
    
    
    ## AREA PLOT ***********************
    df_top5_t.plot(kind="area")
    plt.title("Immigration trend of top 5 countries")
    plt.xlabel("Years")
    plt.ylabel("Number of immigrates")

    ax = plt.subplot(111)
    
    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.45, -0.16), fancybox=True, shadow=False, ncol=1)
    
    plt.show()
    
    
    
    
    ## HISTOGRAM ***********************
    count, bin_edges = np.histogram(df[2013])
    
    df[2013].plot(kind="hist", xticks = bin_edges, figsize=(8, 5))
    plt.title("HISTOGRAM OF IMMIGRATION FROM 195 COUNTRIES IN 2013")
    plt.xlabel("Nummber of countries")
    plt.ylabel("Number of immigrates")
    plt.tick_params(axis='x', which='major', labelsize=8.2)
    plt.xticks(rotation=0)
    
    plt.show()
    
    
    ## BAR CHART ***********************
    
    years = list(range(1980, 2014))
    
    
    index_Iceland = df[df["Country"]=="Iceland"].index.values
    
    df_iceland = df.loc[index_Iceland[0], years]
    
    df_iceland.plot(kind="bar")
    plt.title("ICELAND IMMIGRANTS TO CANADA FROM 1980 TO 2013")
    plt.xlabel("Year")
    plt.ylabel("Number of immigrates")
    
    
    
    
    plt.show()
    
    
    
    
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi