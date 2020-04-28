#!/usr/bin/python

import random
import sys

## -------------------------------------------------------------------------
def MultiplicarEscalar( M, s ):
    R = M
    for i in range( len( M ) ):
        for j in range( len( M[ i ] ) ):
            R[ i ][ j ] = M[ i ][ j ] * s
        # rof
    # rof
    return R
# fed

## -------------------------------------------------------------------------
def SumarMatrices( A, B ):
    C = A
    for i in range( len( A ) ):
        for j in range( len( A[ i ] ) ):
            C[ i ][ j ] = A[ i ][ j ] + B[ i ][ j ]
        # rof
    # rof
    return C
# fed

## -------------------------------------------------------------------------
def ImprimirMatriz( M ):
    for i in range( len( M ) ):
        for j in range( len( M[ i ] ) ):
            print M[ i ][ j ],
        # rof
        print ""
    # rof
    print "-------------------------------------"
# fed

## -------------------------------------------------------------------------
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

    D = MultiplicarEscalar( A, 10 )
    E = SumarMatrices( B, C )
    ImprimirMatriz( D )
    ImprimirMatriz( E )
#fed
    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
