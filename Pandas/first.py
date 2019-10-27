import pandas as pd
import sys


def principal( argv ):
    ## Important that the file was separated by ","

    ## Read file csv
    f_csv = "file_csv.csv"
    a = pd.read_csv( f_csv )
    print(a)

    ## Read the name of the column and take the column
    b = a[['x']]
    print(b)

    ## Especific value
    print(a.loc[5])
    print(a.loc[a.index[[2]], 'x'])
    print(a.loc[a.index[[5, 7]], 'x'])
    
    ## Return specific position like a matrix
    print(a.iloc[0,0])
    print(a.iloc[[1,7], a.columns.get_indexer(['x', 'z'])])
    
#fed





if __name__ == "__main__":
    principal( sys.argv )
#fi