#!/usr/bin/python 
 
import random 
import sys 
 
 
def ImprimirMatriz( M ): 
    for i in range( len( M ) ): 
        for j in range( len( M[ i ] ) ): 
            print M[ i ][ j ], 
        # rof 
        print "" 
    # rof 
    print "-------------------------------------" 
# fed 
 
def genera( M,k ): 
    for i in range( k ): 
        x=random.randint( 0, len( M )-1 ) 
        y=random.randint( 0, len( M[ 0 ] ) -1 ) 
        while (M[x][y]==1): 
            x=random.randint( 0, len( M )-1 ) 
            y=random.randint( 0, len( M[ 0 ] ) -1 ) 
        #eliwh     
        M[x][y]=1 
    #rof 
    return M 
# fed 

def aleatoria_prob_menor(M,G):
    w=2
    a=[0,0]
    b=[]
    for i in range( len( M ) ): 
        for j in range( len( M[ i ] ) ): 
             if (M[i][j]<=w):
                 a=[i,j]
                 w=M[i][j]
             #fi
        #rof
    #rof
    x=M[a[0]][a[1]]
    c=[0,0]
    for i in range( len( M ) ): 
        for j in range( len( M[ i ] ) ): 
            if (M[i][j]==x):
                c=[i,j]
                b.append(c)
            #fi
        #rof
    #rof
    d=[]
    y=random.randint(0,len(b)-1)
    d=b[y]
    n=d[0]
    m=d[1]
    while (G[n][m]!="#"):
        y=random.randint(0,len(b)-1)
        d=b[y]
        n=d[0]
        m=d[1]
    #elihw
    return b[y]
#fed

def cuenta_alrededor(M,n,m):
    cont=0
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
    return cont
#fed


def cuenta_total(M,n,m):
    cont=0
    if (n-1>=0  and n-1<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1):
        cont=cont+1   
    #fi
    if (n-1>=0  and n-1<=len(M)-1 and m>=0 and m<=len(M[0])-1):
        cont=cont+1 
    #fi
    if (n-1>=0  and n-1<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1):
        cont=cont+1
    #fi
    if (n>=0  and n<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1):
        cont=cont+1
    #fi
    if (n>=0  and n<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1):
         cont=cont+1
    #fi
    if (n+1>=0 and n+1<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1):
        cont=cont+1
    #fi
    if (n+1>=0 and n+1<=len(M)-1 and m>=0 and m<=len(M[0])-1):
        cont=cont+1
    #fi
    if (n+1>=0  and n+1<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1):
        cont=cont+1
    #fi
    return cont
#fed

def actualiza_probabilidad(P,M,n,m,d,r):
    q=float(d)
    t=float(r)
    p=q/t
    if (n-1>=0  and n-1<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1):
        P[n-1][m-1]=P[n-1][m-1]+p   
    #fi
    if (n-1>=0  and n-1<=len(M)-1 and m>=0 and m<=len(M[0])-1):
        P[n-1][m]=P[n-1][m]+p
    #fi
    if (n-1>=0  and n-1<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1):
        P[n-1][m+1]=P[n-1][m+1]+p
    #fi
    if (n>=0  and n<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1):
        P[n][m-1]=P[n][m-1]+p
    #fi
    if (n>=0  and n<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1):
        P[n][m+1]=P[n][m+1]+p
    #fi
    if (n+1>=0 and n+1<=len(M)-1 and m-1>=0 and m-1<=len(M[0])-1):
        P[n+1][m-1]=P[n+1][m-1]+p
    #fi
    if (n+1>=0 and n+1<=len(M)-1 and m>=0 and m<=len(M[0])-1):
        P[n+1][m]=P[n+1][m]+p
    #fi
    if (n+1>=0  and n+1<=len(M)-1 and m+1>=0 and m+1<=len(M[0])-1):
        P[n+1][m+1]=P[n+1][m+1]+p
    #fi
#fed


def juega_solo(M,k):
    g=float(k)
    y= float(len(M)*len(M[0]))
    p=g/y
    print p
    P=[ [ p for x in range( len( M[ 0 ] ) ) ] for y in range( len( M ) ) ]
    G=[ [ "#" for x in range( len( M[ 0 ] ) ) ] for y in range( len( M ) ) ]
    x=True
    ImprimirMatriz(M)
    cont2=0
    while (x==True and cont2<=(len(M)*len(M[0])-k)):
        a=aleatoria_prob_menor(P,G)
        print a
        n=a[0]
        m=a[1]
        if (M[n][m]==0):
            d=cuenta_alrededor(M,n,m)
            G[n][m]=d
            ImprimirMatriz(G)
            r=cuenta_total(M,n,m)
            actualiza_probabilidad(P,M,n,m,d,r)
            cont2=cont2+1
        #fi

        if (M[n][m]==1):
            print("Perdiste")
            x=False
        #fi

        if (cont2==(len(M)*len(M[0])-k)):
            print("Felicidades. Ganaste")
            cont2=cont2+1
        #fi
    #elihw
# fed  



 
def main( argv ): 
    n_rows = int(raw_input("FILAS: ")) 
    n_cols = int(raw_input("COLUMNAS: ")) 
    k = int(raw_input("MINAS: ")) 
    A = [ [ 0 for x in range( n_cols ) ] for y in range( n_rows ) ] 
    B=genera(A,k) 
    juega_solo(B,k)
#fed 
 
 
 
     
if __name__ == "__main__": 
    main( sys.argv ) 
# fi 
 
## eof - programa_prueba.py

