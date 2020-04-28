#!/usr/bin/python

import sys

## -------------------------------------------------------------------------
def Codificar( letra ):
    a = ord( 'a' )
    z = ord( 'z' )
    A = ord( 'A' )
    Z = ord( 'Z' )
    c = ord( letra )

    r = c
    if ( a <= c ) and ( c <= z ):
        r = ( ( ( c - a ) + 13 ) % ( z - a + 1 ) ) + a
    elif ( A <= c ) and ( c <= Z ):
        r = ( ( ( c - A ) + 13 ) % ( Z - A + 1 ) ) + A
    # fi
    return chr( r )
# fed

## -------------------------------------------------------------------------
def Decodificar( letra ):
    a = ord( 'a' )
    z = ord( 'z' )
    A = ord( 'A' )
    Z = ord( 'Z' )
    c = ord( letra )

    r = c
    if ( a <= c ) and ( c <= z ):
        i = ( c - a ) - 13
        if i < 0:
            r = z + i + 1
        else:
            r = a + i
        # fi
    elif ( A <= c ) and ( c <= Z ):
        i = ( c - A ) - 13
        if i < 0:
            r = Z + i + 1
        else:
            r = A + i
        # fi
    # fi
    return chr( r )
# fed

## -------------------------------------------------------------------------
def Rot13( msg ):
    enc = ""
    for i in range( len( msg ) ):
        enc = enc + Codificar( msg[ i ] )
    # rof
    return enc
# fed

## -------------------------------------------------------------------------
def AntiRot13( enc ):
    msg = ""
    for i in range( len( enc ) ):
        msg = msg + Decodificar( enc[ i ] )
    # rof
    return msg
# fed

## -------------------------------------------------------------------------
def main( argv ):
    ## Crear mensaje
    msg = "Dabale arroz a la zorra el abad"

    ## Encriptar
    enc = Rot13( msg )

    ## Decriptar
    msg2 = AntiRot13( enc )

    ## Mostrar los resultados
    print ("Mensaje original :", msg)
    print ("Encriptado       :", enc)
    print ("Mensaje          :", msg2)
#fed

if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - rot13.py
