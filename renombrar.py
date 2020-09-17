import os 
import sys


def main(argv): 
    path = "C:\\Users\\USUARIO1\\Desktop\\Escritura 2386\\"
    for count, filename in enumerate(os.listdir(path)): 
        nombre = "Esc.2386 Pág" + str(count+1) + ".jpeg"
        src = path + filename 
        dst = path + nombre
        os.rename(src, dst)
    #rof
#fed

if __name__ == '__main__': 
    main(sys.argv)
#fi