import os 
import sys

def main(argv): 
    for count, filename in enumerate(os.listdir("C:\\Users\\USUARIO1\\Desktop\\Producción\\Notas")): 
        nombre ="Hoja " + str(count+1) + ".jpeg"
        src ="C:\\Users\\USUARIO1\\Desktop\\Producción\\Notas\\"+ filename 
        dst ="C:\\Users\\USUARIO1\\Desktop\\Producción\\Notas\\"+ nombre
        os.rename(src, dst)
    #rof
#fed

if __name__ == '__main__': 
    main(sys.argv)
#fi