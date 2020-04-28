#!/usr/bin/python

import random
import sys


def transpone(M,r,s):
    G = [ [ 0 for x in range( r ) ] for y in range( s ) ]
    for i in range( len( G ) ):
        for j in range( len( G[ i ] ) ):
            G[ i ][ j ]=M[ j ][ i ]
        # rof
    # rof
    return G
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

    ## Crear numero a adivinar
    n_rows = 5
    n_cols = 10

    A = [ [ 0 for x in range( n_cols ) ] for y in range( n_rows ) ]
    B = [ [ 0 for x in range( n_cols ) ] for y in range( n_rows ) ]
    C = [ [ 0 for x in range( n_cols ) ] for y in range( n_rows ) ]

    for i in range( n_rows ):
        for j in range( n_cols ):
            A[ i ][ j ] = random.randint( 0, 9 );
            B[ i ][ j ] = random.randint( 0, 9 );
            C[ i ][ j ] = random.randint( 0, 9 );
        # rof
    # rof
    ImprimirMatriz( A )
    G = transpone( A,n_rows,n_cols )
    ImprimirMatriz( G )
#fed



    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
