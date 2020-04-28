#!/usr/bin/python

import random
import sys


def verifica(R):
    x=1
    for i in range( len( R ) ):
        for j in range( len( R[ i ] ) ):
            if (R[i][j]==1):
                cont1=-1 
                for k in range (8) :
                    if (R[i][k]==1):
                        cont1=cont1+1
                    #fi
                #rof      
                cont2=-1        
                for l in range (8) :
                    if (R[l][j]==1):
                        cont2=cont2+1
                    #fi
                #rofn=1
                n=1
                cont3=0
                while (i+n<=7 and i+n>=0 and j+n<=7 and j+n>=0):
                    if (R[i+n][j+n]==1):
                        cont3=cont3+1
                    #fi
                    n=n+1
                #elihw
                n=1
                cont4=0
                while (i-n<=7 and i-n>=0 and j+n<=7 and j+n>=0):
                    if (R[i-n][j+n]==1):
                        cont4=cont4+1
                    #fi
                    n=n+1
                #elihw
                n=1
                cont5=0
                while (i+n<=7 and i+n>=0 and j-n<=7 and j-n>=0):
                    if (R[i+n][j-n]==1):
                        cont5=cont5+1
                    #fi
                    n=n+1
                #elihw
                n=1
                cont6=0
                while (i-n<=7 and i-n>=0 and j-n<=7 and j-n>=0):
                    if (R[i-n][j-n]==1):
                        cont6=cont6+1
                    #fi
                    n=n+1
                #elihw
                if (cont1!=0 or cont2!=0 or cont3!=0 or cont4!=0 or cont5!=0 or cont6!=0 ):
                    x=2
                #fi
            #fi      
        #rof
    #rof
    return x
                    
#fed

def genera( C ):
    y=0
    cont=0
    for a in range( 8 ):
        for b in range( 8 ):
            for c in range( 8 ):
                for d in range( 8 ):
                    for e in range( 8 ):
                        for f in range( 8 ):
                            for g in range( 8 ):
                                for h in range( 8 ):
                                    C[0][a]=1
                                    C[1][b]=1
                                    C[2][c]=1
                                    C[3][d]=1
                                    C[4][e]=1
                                    C[5][f]=1
                                    C[6][g]=1
                                    C[7][h]=1
                                    y=verifica(C)
                                    if (y==1):
                                       cont=cont+1
                                       ImprimirMatriz( C )
                                       print cont
                                    #fi
                                    C=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
                                      ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
                                #rof
                            #rof   
                        #rof
                    #rof   
                #rof
            #rof
        #rof
    #rof   
                    
# fed

def ImprimirMatriz( M ):
    for i in range( len( M ) ):
        for j in range( len( M[ i ] ) ):
            print M[ i ][ j ],
        # rof
        print ""
    # rof
    print "-------------------------------------"
# fed


def main( argv ):

    ## Crear numero a adivinar
    n_rows = 8
    n_cols = 8
    A = [ [ 0 for x in range( n_cols ) ] for y in range( n_rows ) ]
    M=[[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1]
       ,[0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0]]
    A=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
       ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    #ImprimirMatriz( A)
    #y=verifica(A)
    genera(A)
    #print y
#fed
    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
