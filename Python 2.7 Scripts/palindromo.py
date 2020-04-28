#!/usr/bin/python
import sys


def main( argv ):
    S = []
    x=int(raw_input("Digite el numero de elementos: "))
    for i in range (0,x,1):
        S.append(int(raw_input("Digite elemento: ")))
    #rof
    print S
    n=len(S)/2
    cont=0
    for i in range (0,n,1):
       if (S[i]==S[len(S)-1-i]):
           cont=cont+1
       #fi
    #rof
    if (cont==n):
        print "Es un palindromo"
    else:    
        print "No es un palindromo"
    #fi    
#fed

    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
