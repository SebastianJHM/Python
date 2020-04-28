#!/usr/bin/phyton
#enconding: utf-8
import sys
import random
import math

def picas(vec,y):
    vec1=[0,0,0,0]
    m=10
    n=1
    for i in range (0,4,1):
        vec1[3-i]=(y%m)/n
        m=m*10
        n=n*10
    #rof
    cont2=0
    for i in range (0,4,1):
       cont1=0
       for j in range (0,4,1):
          if (vec[i]==vec1[j] and i!=j and vec[i]!=vec1[i]):
             cont1=cont1+1
          #fi
       #rof
       if (cont1>0):
          cont2=cont2+1
       #fi
    #rof
    return cont2
# fed
       	


def fijas(vec,y):
    vec1=[0,0,0,0]
    m=10
    n=1
    for i in range (0,4,1):
        vec1[3-i]=(y%m)/n
        m=m*10
        n=n*10
    #rof
    cont=0
    for i in range (0,4,1):
        if (vec[i]==vec1[i]):
           cont=cont+1
        #fi
    #rof
    return cont
# fed

def main( argv ):
    x=int(raw_input("Digite el numero a hallar: "))
    vec=[0,0,0,0]
    m=10
    n=1
    for i in range (0,4,1):
        vec[3-i]=(x%m)/n
        m=m*10
        n=n*10
    #rof
    print vec
    j=0
    while (j!=4):
        y=int(raw_input("Digite el numero: "))
        j=fijas(vec,y)
        k=picas(vec,y)
        if (j==4):
           print "Felicidades; encontraste el numero"
        else:
           print "El numero de fijas es: ", j
           print "El numero de picas es: ", k
        #fi
   #elihw
#fed

if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py






