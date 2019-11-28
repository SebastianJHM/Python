import sys
import json
 
def primo( x: int ):
    cont = 0
    for i in range(1,x+1):
        if ( x % i == 0 ):
            cont = cont + 1
        #fi
    #rof

    if (cont == 2):
        b = True
    else:
        b = False 
    #fi

    return b
#fed

def separar( t ):
    pos = [0]
    cont = 0
    for x in t:
        cont = cont + 1
        if ( x == " " ):
            pos.append(cont)
        #fi
    #rof
    pos.append(len(t)+1)
    print(pos)
    final = []
    for i in range(0,len(pos)-1):
        print(t[pos[i]:pos[i+1]-1])
        final.append(t[pos[i]:pos[i+1]-1])
    #rof

    return final
#fed


def principal( argv ):
    vec = [1,2,3,4,5,6,7,8,9]
    result = []
    for x in vec:
        y = primo(x)
        if ( y == True ):
            result.append("Primo")
        else:
            result.append("No es Primo")
        #fi
    #rof
    print(result)

    text = "Este es el texto que hay que separar"
    list1 = separar(text)
    print(list1)
#fed


if __name__ == "__main__":
    principal( sys.argv )
# fi