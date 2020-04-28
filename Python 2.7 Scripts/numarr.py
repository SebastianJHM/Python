#!/usr/bin/python
import sys

def main( argv ):
    x=int(raw_input("Digite el numero: "))
    copia=x
    cont=0
    while (copia!=0):
        cont=cont+1
        copia=copia/10
    #elihw      
    m = 10
    n = 1
    S = []
    G = []
    for i in range (0,cont,1):
       S.append((x%m)/n)
       m=m*10
       n=n*10
    #rof
    for i in range (0,cont,1):
       G.append(S[cont-1-i])
    #rof
    print G


   #fed

    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
