#!/usr/bin/python

import random
import sys


def ImprimirMatriz( M ):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j],end=' ')
        #rof
        print()
    # rof
    print("-------------------------------------")
# fed

def genera( M,k ):
    for i in range( k ):
        x=random.randint( 0, len(M)-1)
        y=random.randint( 0, len(M[0])-1)
        while (M[x][y]==1):
            x=random.randint( 0, len(M)-1)
            y=random.randint( 0, len(M[0])-1-1 )
        #eliwh    
        M[x][y]=1
    #rof
    return M
# fed

def juega(M,k):
    G=[ [ '#' for x in range( len( M[0] ) ) ] for y in range( len(M) ) ]
    ImprimirMatriz( G )
    x = True
    y= len(M)*len(M[0])
    cont2=0
    while (x==True and cont2<=(y-k)):
        n=int(input("Digite posicion fila: "))
        m=int(input("Difite posicion columna: "))
        cont=0
        if (M[n][m]==0):
            if (n-1>=0  and n-1<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1 and M[n-1][m-1]==1):
                cont=cont+1   
            #fi
            if (n-1>=0  and n-1<=len(M)-1 and m>=0 and m<=len(M[0])-1 and M[n-1][m]==1):
                cont=cont+1 
            #fi
            if (n-1>=0  and n-1<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1 and M[n-1][m+1]==1):
                cont=cont+1
            #fi
            if (n>=0  and n<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1 and M[n][m-1]==1):
                cont=cont+1
            #fi
            if (n>=0  and n<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1 and M[n][m+1]==1):
                cont=cont+1
            #fi
            if (n+1>=0 and n+1<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1 and M[n+1][m-1]==1):
                cont=cont+1
            #fi
            if (n+1>=0 and n+1<=len(M)-1 and m>=0 and m<=len(M[0])-1 and M[n+1][m]==1):
                cont=cont+1
            #fi
            if (n+1>=0  and n+1<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1 and M[n+1][m+1]==1):
                cont=cont+1
            #fi
            cont2=cont2+1
            G[n][m]=cont
            ImprimirMatriz(G)
        #fi   
        if (M[n][m]==1):
            print("Perdiste")
            x=False
        #fi
        if (cont2==(y-k)):
            print("Felicidades. Ganaste")
            cont2=cont2+1
        #fi 
    #elihw
# fed



def main( argv ):
    n_rows = int(input("FILAS: "))
    n_cols = int(input("COLUMNAS: "))
    k = int(input("MINAS: "))
    A = [ [ 0 for x in range( n_cols ) ] for y in range( n_rows ) ]
    B=genera(A,k)
    juega(B,k)
#fed



    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
