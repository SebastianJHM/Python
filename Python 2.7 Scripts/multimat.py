#!/usr/bin/python

import random
import sys

def Multimat(M,n,m,G,t,q ):
    if (m!= t or n!=q):
        print ("Ingrese matrices multiplicables")
    # fi
    H = [ [ 0 for x in range( n ) ] for y in range( q ) ]
    if (m==t and n==q):
        for i in range( len( M ) ):
            for j in range( len( M ) ):
                acum=0
                for k in range ( len( M[ i ] ) ):
                    acum=acum+M[ i ][ k ]*G[ k ][ j ]
                # rof
                H[ i ][ j ]=acum
            # rof
        # rof
    # fi
    return H
# fed



def ImprimirMatriz( M ):
    for i in range( len( M ) ):
        for j in range( len( M[ i ] ) ):
            print M[ i ][ j ], 
        # rof
        print( "\n" )
    # rof
    print( "-------------------------------------" )
# fed

def main( argv ):
    
    n = 5
    m = 10
    t = 10
    q = 5 

    A = [ [ 0 for x in range( m ) ] for y in range( n ) ]
    B = [ [ 0 for x in range( q) ] for y in range(t  ) ]
    
    for i in range( n):
        for j in range( m ):
            A[ i ][ j ] = random.randint( 0, 9 ); 
        # rof
    # rof

    for i in range( t ):
        for j in range( q ):
            B[ i ][ j ] = random.randint( 0, 9 ); 
        # rof
    # rof
    
    ImprimirMatriz( A )
    ImprimirMatriz( B )
    H = Multimat(A,n,m,B,t,q)
    ImprimirMatriz( H )
#fed



    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
