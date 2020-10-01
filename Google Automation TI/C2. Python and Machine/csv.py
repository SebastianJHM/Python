import sys
import csv

def principal( argv ):
    ## Read CSV
    path = "C:\\Users\\USUARIO1\\Desktop\\MyPython\\Google Automation TI\\C2. Python and Machine\\Police_Department_Incidents_-_Previous_Year__2016_.csv"
    f = open(path)
    csv_f = csv.reader(f)
    # for x in csv_f:
    #     print(x)
    
    path = "subvenciones-educacion2016.csv"
    with open(path, encoding='latin1') as f:
        x = list(csv.reader(f))
        for data in x[1::]:
            print(data)
        
    #htiw
   
    ## Write csv file
    hosts = [["worksation.local", "192.4.567.6"], ["webserver.cloud", "10.2.5.6"]]
    with open("hosts.csv", "w") as hosts_csv:
        writer = csv.writer(hosts_csv)
        writer.writerows(hosts)
        
        
    ## Read csv as a dictionary
    path = "subvenciones-educacion2016.csv"
    with open(path, encoding='latin1') as archivo_csv:
        dict_lector = csv.DictReader(archivo_csv)
        for linea in dict_lector:
            # print(linea)
            print("Asociación: {}, NIF: {}, Impuestos: {}".format(linea["ASOCIACION"], linea["NIF"], linea["IMPUESTOS"]))
    #htiw
    
    
    myDictionary = [
        {"id" : -1, "name" : "sid", "dataTypeName" : "meta_data", "fieldName" : "sid", "position" : 0,"renderTypeName" : "meta_data"},
        {"id" : -1, "name" : "sid", "dataTypeName" : "meta_data", "fieldName" : "sid", "position" : 0,"renderTypeName" : "meta_data"},
        {"id" : -1, "name" : "sid", "dataTypeName" : "meta_data", "fieldName" : "sid", "position" : 0,"renderTypeName" : "meta_data"},
        {"id" : -1, "name" : "sid", "dataTypeName" : "meta_data", "fieldName" : "sid", "position" : 0,"renderTypeName" : "meta_data"}
    ]
    keys = ["id", "name", "dataTypeName", "fieldName", "position", "renderTypeName"]
    with open("writeCSV.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames = keys)
        writer.writeheader()
        writer.writerows(myDictionary)
    
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi