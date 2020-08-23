import sys

def principal( argv ):
    ## ******************************************************************************
    ## MATPLOTLIB ARCHITECTURE
    ## ******************************************************************************
    ## 1. Backend Layer
    ## ******************************************************************************
    ## 1.1. Figure Canvas: matplotlib.backend_bases.FigureCanvas
    ##      Encompasses the area on which the figure is drawn
    ## 1.2. Renderer: matplotlib.backend_bases.Renderer
    ##      Knows how to draw on the FigureCanvas
    ## 1.3. Event: matplotlib.backend_bases.Event
    ##      Handles user inputs such as keyboard strokes and mouse clicks
    ## ******************************************************************************
    ## 2. Artist Layer
    ## ******************************************************************************
    ## 2.1. Primitive: Line 2D, Rectangle, Circle and Text
    ## 2.2. Composite: axis, tick, axes and figure
    ## ******************************************************************************
    
    ## HISTOGRAM PLOT
    ## Complete form
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    
    fig = Figure()
    Canvas = FigureCanvas(fig)
    
    ## Generate 10000 random numbers
    import numpy as np
    x = np.random.randn(10000)
    
    ax = fig.add_subplot(111) ## Create and axes artist
    ax.hist(x, 100) ## Generate a histogram of the 1000 numbers
    
    ## Add a title of the figure and save it
    ax.set_title("Normal distribution whit $\mu = 0, \sigma = 1$")
    fig.savefig("matplotlib_histogram_1.png")
    
    ## Easy form
    import matplotlib.pyplot as plt
    y = np.random.randn(10000)
    plt.hist(y, 30)
    plt.title(r"Normal distribution whit $\mu = 0, \sigma = 1$")
    plt.savefig("matplotlib_histogram_2.png")
    plt.show()
    
    
    
    ## GRAPH DATAFRAME
    import pandas as pd
    data = [[8880, 5123], [8670, 6682], [8147, 3308], [7338, 1863], [5704, 1527]]
    df = pd.DataFrame(data, columns = ["india", "china"], index = [1980, 1981, 1982, 1983, 1984])
    
    df.plot(kind="line")
    plt.show()
    
    df["india"].plot(kind="hist")
    plt.show()
    
    
    
    
    ## DATAFRAME
    ## Paths of the file of data analysis
    url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx"
    path = "C:\\Users\\USUARIO1\\Desktop\\MyPython\\Análisis de datos\\Visualization\\Canada.xlsx"
    
    df = pd.read_excel(url, sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
    df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
    
    
    
    ## LINE PLOTS *********
    ## Line plot is a type plot which displays a series of data points connected by straight line
    ## Get a vector whit the index whre appear Haiti in the column of countries
    index_Haiti = df[df["Country"]=="Haiti"].index.values
    ## Print a plot 
    years = list(range(1980,2014))
    df.loc[index_Haiti[0], years].plot(kind="line")
    plt.title("Immigration from Haiti")
    plt.xlabel("Years")
    plt.ylabel("Number of immigrates")
    plt.show()
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi