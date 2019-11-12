import sys
import csv
import json

def principal( argv ):
    path = "C:\\Users\\SebastianHerrera\\Desktop\\Python\\ReadCSVandJSON\\subvenciones-educacion2016.csv"
    with open(path, encoding='latin1') as archivo_csv:
        dict_lector = csv.DictReader(archivo_csv)
        #  next(dict_lector, None)  # Se salta la cabecera
        importe_total = 0
        cont = 0
        for linea in dict_lector:
            importe_str = linea["IMPUESTOS"]
            print(importe_str)
            importe = float(importe_str)
            importe_total = importe_total + importe
            cont = cont + 1
        #rof
        print('El promedio es ', importe_total/cont)
    #htiw

    print("\n-------- JSON ------------")
    path = "ReadCSVandJSON\\datosColombia.json"
    with open(path, encoding="utf8") as fich:    
        datos = json.load(fich)    
        ## print(datos["meta"]["view"]["columns"])
        contMenos1 = 0
        contOtro = 0
        for x in datos["meta"]["view"]["columns"]:
            if x["id"] == -1:
                contMenos1 = contMenos1 + 1
            else:
                contOtro = contOtro + 1
            #fi
        #rof
        print("La cantidad de elemnto con id -1 es:", contMenos1)
        print("La cantidad de elemnto con otro id es:", contOtro)
    #htiw

#fed






if __name__ == "__main__":
    principal( sys.argv )
#fi