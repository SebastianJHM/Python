from flask import Flask
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import requests
from flask import request
import json
import os
import datetime
import openpyxl
import io
from firebase import firebase
import uuid
import matplotlib.pyplot as plt
from io import BytesIO
import base64



firebase = firebase.FirebaseApplication('https://pmausers-58032.firebaseio.com', None)

app = Flask(__name__)
cors = CORS(app)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))



"""
RUTAS DE LA APLICACION:
    @app.route('/', methods=['GET']): prueba de funcion de la API
    @app.route('/post', methods=['POST']): ruta a la que se envian los archivos de cognos,rarias, forecast.id y date se hace todo el procesamiento
    @app.route('/reports', methods=['GET']): ruta para obtener historicos 
RUTAS DE USUARIOS
    @app.route('/users', methods=['GET']): obtiene el listado de usuarios
    @app.route('/users', methods=['POST']): escribe un usuario nuevo
    @app.route('/users/<string:codigo>', methods=['DELETE']): elimina un usuario en base a su codigo
    @app.route('/users', methods=['PUT']): actualiza un usuario
"""

"""******************************************************************************************************************************************************"""
@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return pedirUno()
"""******************************************************************************************************************************************************"""
@app.route('/post', methods=['POST'])
@cross_origin()
def post():

    archivoCognos = request.files["cognos"].read()
    archivoRarias = request.files["rarias"].read()
    archivoIppf = request.files["ippf"].read()
    identificacion = request.form.get('id')
    fecha = request.form.get('date')
    
    """##Lectura de Archivos
    Esta funcion lee cada uno de los archivos y guarda las tablas en 3 dataframes distintos
    también obtiene el identificador del proyecto
    """
    Forecast , Cognos_pivot , rarias , proyectoId = read_data(archivoIppf,archivoCognos,archivoRarias)

    """##Filtro de Proyectos (RARIAS)
    La segunda parte devuelve las 3 columnas necesarias para hacer el procesamiento del rarias. se le debe ingresar el nombre del proyecto y el dataFrame rarias.
    """
    Rarias_ready=filter_columns_rariasAll(rarias)

    """##Acondicionamiento (Forecast)
    Esta funcion trae las tres columnas de interes del archivo de Forecast apartir del mes solicitado (este mes se encuebta en el archivo cognos)
    """
    date = proyect_date(Cognos_pivot)
    Forecast_ready=filter_columns_forecast(Forecast , datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))
    #print(np.array(Forecast_ready['Hours']))
    Forecast_ready['Hours'] = Forecast_ready['Hours'].fillna('0').replace('','0')
    
    """##Normalizacion o Estandarizacion
    normalizar codigo de empleados (Remover errores en Id's de empleados)

    ###Normalizacion Forecast
    normalizar codigo de empleados (Forecast), quitar ultimos tres digitos del codigo de usuario
    """
    idForecast = Forecast_ready['CNUM (*)'].fillna('-1')
    Forecast_ready['CNUM (*)'] = idForecast.map(remove_AreaCode)
    
    print(Forecast_ready)
    for value in Forecast_ready['CNUM (*)']:
      if value == '-1':
        name = Forecast_ready[Forecast_ready['CNUM (*)']==value]['Name Employee']
        indice = Forecast_ready[Forecast_ready['CNUM (*)']==value]['Name Employee'].index
        Forecast_ready['CNUM (*)'][indice]= name
    
    

    """###Normalizacion RARIAS
    Normalizar codigo empleados (RARIAS), anadir cero a los codigos de empleado. Jose
    """
    idRarias = Rarias_ready['EMP NUM'].fillna('-1')
    Rarias_ready['CNUM (*)'] = idRarias.map(add_ZeroCode)

    """###Normalizacion Rate RARIAS
    Obtener rate empleados (RAREAS), (Obtiene el valor que mas se repite)
    Organiza el Dataframe, agrupando los Id y los codigos de pais (Elimina ',' del Rate).
    """
    RatesClasify = sum_RateEmployee(Rarias_ready)
    rarias_Unique = remove_MaxRepeat(RatesClasify)

    """##Conversion TRM"""
    TRM_Conversion(rarias_Unique)

    """##Generar Tabla Reconciliacion
    Acoplar las tres tablas limpias en una unica tabla final.
    """
    Cognos_DataFrame = pd.DataFrame(Cognos_pivot.to_records())
    mensajes= claseMensajes()
    Final_Table = leer(Cognos_DataFrame,Forecast_ready,rarias_Unique,mensajes)
    
    #Totalizar Tabla
    Final_Table = total_ReconciliationTable(Final_Table)
    print(np.array(Final_Table))
    #Generar Alertas de Cambios
    validation_band_rate(Forecast_ready,rarias_Unique,mensajes)
    #print(mensajes.devolverAlertas())
    
    #Generar JSON
    jsonFinal = json.loads(Final_Table.to_json( force_ascii=False))
    jsonFinal['Alertas'] = mensajes.devolverAlertas()
    jsonFinal['Errores'] = mensajes.devolverErrores()
    
    #Guardar Reporte
    postReport(identificacion, fecha, proyectoId ,  json.dumps(jsonFinal) )
    """##Convertidor JSON
    Esta funcion comvierte el dataframe a json para enviarlo a front.
    """
        
    return json.dumps(jsonFinal)
"""******************************************************************************************************************************************************"""
@app.route('/users', methods=['GET'])
@cross_origin()
def getUsers():
    result = firebase.get('/PMA/Users/', '')
    return result
"""******************************************************************************************************************************************************"""
@app.route('/users', methods=['POST'])
@cross_origin()
def postUser():
    data = {}
    content = request.get_json()
    #print(content)
    users = firebase.get('/PMA/Users/', '')
    userStr = str(users)
    #print(userStr)
    if userStr.find(content['codigo']) > -1:
        data['estado'] = 'error'
        data['mensaje'] = 'El usuario ya existe'
        json_data = json.dumps(data)
        return json_data
    else:
        if userStr.find(content['correo']) > -1:
            data['estado'] = 'error'
            data['mensaje'] = 'El correo ya esta en uso'
            json_data = json.dumps(data)
            return json_data
        else:
            data['estado'] = 'Ok'
            data['mensaje'] = 'El usuario se inserto correctamente'
            json_data = json.dumps(data)
            firebase.put('/PMA/Users', content['codigo'], content)
            
    return json_data
"""******************************************************************************************************************************************************"""
@app.route('/users/<string:codigo>', methods=['DELETE'])
@cross_origin()
def deleteUser(codigo):
    data = {}
    if firebase.get('/PMA/Users/'+codigo+'/admin', '') == 'false':
        firebase.delete('/PMA/Users/', codigo)
        data['estado'] = 'Ok'
        data['mensaje'] = 'El usuario se elimino correctamente'
        json_data = json.dumps(data)
        return json_data

    data['estado'] = 'error'
    data['mensaje'] = 'No puede eliminar administradores'
    json_data = json.dumps(data)
    return json_data
"""******************************************************************************************************************************************************"""
@app.route('/users', methods=['PUT'])
@cross_origin()
def putUser():
    data = {}
    content = request.get_json()
    firebase.put('/PMA/Users', content['codigo'], content)

    data['estado'] = 'Ok'
    data['mensaje'] = 'Usuario actualizado correctamente'
    json_data = json.dumps(data)
    return json_data
"""******************************************************************************************************************************************************"""
@app.route('/reports', methods=['GET'])
@cross_origin()
def getReports():
    result = firebase.get('/PMA/Reports/', '')
    return result
"""******************************************************************************************************************************************************"""
@app.route('/images', methods=['POST'])
@cross_origin()
def getImages():
    content = request.get_json()
    reporteId=content['reporteId']
    imagen=content['imagen']
    result = firebase.get('/PMA/Reports/', reporteId)
    jsonResult=json.loads(result['archivo'])
    jsonResult.pop('Alertas', None)
    jsonResult.pop('Errores', None)
   
    tabla=pd.read_json(json.dumps(jsonResult))
    tabla.drop(tabla.shape[0]-1,inplace=True)
        
    if imagen>0 and imagen <= 3:
       grafica = graphs_Reconcilationcompar(tabla,imagen)
    elif imagen>3 and imagen <= 6:
       grafica = graphs_Reconcilation(tabla,imagen-3)

    else:
       grafica = 'error'
    
    return grafica
"""******************************************************************************************************************************************************"""
@app.route('/specificReport', methods=['POST'])
@cross_origin()
def getSpecific():
    content = request.get_json()
    reporteId=content['reporteId']
    #print(reporteId)
    result = firebase.get('/PMA/Reports/', reporteId)    
    return result
"""******************************************************************************************************************************************************"""
@app.route('/validar', methods=['POST'])
@cross_origin()
def validarUsuario():
    data = {}
    content = request.get_json()
    #print(content)
    usuarios = firebase.get('/PMA/Users/', '')
    for user in usuarios:
        if user == content['codigo']:
            if usuarios[user]['pass'] == content['pass']:
                data['admin'] = usuarios[user]['admin']
                data['mensaje'] = 'ok'
                json_data = json.dumps(data)
                return json_data
    data['admin'] = 'error'
    data['mensaje'] = 'error'
    json_data = json.dumps(data)
    return json_data
 
"""******************************************************************************************************************************************************"""

"""##Funciones
Estas son las funciones usadas en cada una de las tareas.

Esta funcion obtiene el DataFrame apartir del archivo de texto "Rarias"
"""

def pedirUno():
    return "prueba get"

def convert_Rarias(nameRarias,columnsTable):

  lines= nameRarias.split('\n')
  column_num = []
  final_table = []
  for i in range(14,len(lines)):
      real_line = []

      if i==14:
          columns = lines[i].strip().split("  ")

          for j in columns:
              column_num.append(len(j))

      else:
          line = lines[i]
          count = 0
          count2=0
          for c in column_num:
              count+=2
              count2 = count + c
              real_line.append(line[count:count2].strip())
              count=count2
      final_table.append(real_line)
    
  tabla = pd.DataFrame(final_table,columns=columnsTable).fillna(value=pd.np.nan).replace(r'^\s*$', np.nan, regex=True).dropna(thresh=2).reset_index()

  return tabla
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def read_data(Forecast,Report_cognos,rariasName):
  # Read Forecast file
  xls_filelike = io.BytesIO(Forecast)
  workbook = openpyxl.load_workbook(xls_filelike, data_only=True)
  data = workbook['By Resource'].values
  Forecast = pd.DataFrame(data)
  colname= np.array(Forecast.iloc[13])
  Forecast.columns=colname
  Forecast = Forecast.drop([0,1,2,3,4,5,6,7,8,9,10,11,12,13],axis=0).reset_index()
  #print(Forecast)
  # Read Cognos file
  xls_filelike1 = io.BytesIO(Report_cognos)
  workbook = openpyxl.load_workbook(xls_filelike1, data_only=True)
  data1 = workbook['page'].values
  columns = next(data1)[0:]
  Cognos_claim = pd.DataFrame(data1,columns=columns)
  
  #Delete null spaces 
  Forecast = Forecast.dropna(subset= ['Key'],thresh=1)
  #obtencion de tabla dinamica 
  Cognos_pivot=pd.pivot_table(Cognos_claim,values = 'Hours', index = ['Account Id','Country Code','Employee Serial Number', 'Employee Name'], columns = ['Week Ending Date'],aggfunc=np.sum)
  Cognos_pivot['Total'] = Cognos_pivot.sum(axis=1)
  #Get Project
  Proyecto=Cognos_claim.loc[1][9].strip()

  #Convert rarias columns names
  columnsTable=['YEAR','MONTH','LEGAL CONTRACT ID','ACCTGRP ID','CUSTOMER NO','COUNTRY CD','EMP NUM','LAST NAME','DPT ID','WEEK ENDING DATE',
          'ACCOUNT ID','WORK ITEM ID','ACTIVITY CD','HOURS','RATE','BANDA','PESOS TOT CHRG','US TOT CHRG','EXCHG RATE','OVERTIME IND']
  rarias = convert_Rarias(rariasName.decode('UTF-8'),columnsTable)
  
  return Forecast ,Cognos_pivot , rarias , Proyecto
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def filter_proyect(rarias):
  proyects = rarias['ACCTGRP ID'].dropna()
  test=np.array(proyects)
  indice=proyects.index
  indice=np.append(indice,len(rarias))
  c=0
  for x in proyects:
    c=c+1
    test[c-1] = rarias.iloc[indice[c-1]:indice[c],:]
  return test
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def show_proyect(proyecto,archivo):
  proyectsnum = archivo['ACCTGRP ID'].dropna().reset_index(drop=True)
  aja = proyectsnum[proyectsnum == proyecto].index
  test = filter_proyect(archivo)
  proyect = test[aja]
  return proyect[0]
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def filter_columns_rarias(proyecto,archivo):
  data = show_proyect(proyecto,archivo)
  fil = data[['COUNTRY CD','EMP NUM','RATE','BANDA']]
  return fil
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def filter_columns_rariasAll(archivo):
  fil = archivo[['COUNTRY CD','EMP NUM','RATE','BANDA']]
  return fil

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def filter_columns_forecast(archivo,date):
    #print(date)
    
    fil = archivo[['CNUM (*)', 'Resource Lotus Notes ID (Opt)','Band Table - Cost Rate','Band Description (*)',date]]
    fil = fil.iloc[:,0:5]#.drop(fil.columns[[5]], axis='columns')
    fil.columns=['CNUM (*)', 'Name Employee','Band Table - Cost Rate','Band Description (*)','Hours']
    return fil
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def list_proyects(rarias):
  proyects = rarias['ACCTGRP ID'].dropna()
  return proyects
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Obtener mes del Reporte Cognos
def proyect_date(Cognos):
    t=Cognos.columns.values[0]
    if t.month<10:
        date=str(t.year)+'-0'+str(t.month)+'-01 00:00:00'
    else:
        date=str(t.year)+'-'+str(t.month)+'-01 00:00:00'
    return date
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
class claseMensajes(object):
    
    alertas = []
    errores = []

    def devolverAlertas(self):
        return self.alertas

    def devolverErrores(self):
        return self.errores

    def agregarAlertas(self, coso):
        self.alertas.append(coso)

    def agregarErrores(self, coso):
        self.errores.append(coso)

def leer(cognos, forecast, rates,claseEmbebida):

    solucion = pd.DataFrame([], columns=list(''))

    # For del Cognos
    for x in range(len(cognos.index)):
        idCognos = cognos.iloc[x]['Employee Serial Number']
        valor1 = cognos[cognos['Employee Serial Number'] == ''+idCognos+''].head(1).iloc[0]['Employee Name']
        valor2 = '0'#ERR20_NULL
        valor3 = 'ERR20_NULL'
        valor4 = 'ERR12_OPER'
        valor5 = cognos[cognos['Employee Serial Number'] == ''+idCognos+''].head(1).iloc[0]['Total']
        valor6 = 'ERR20_NULL'
        valor7 = 'ERR12_OPER'
        valor8 = 'ERR12_OPER'
        valor9 = 'ERR12_OPER'
        valor10 = 'ERR12_OPER'
        
        # Esta en Rarias?
        if len(rates[rates['EMP NUM'] == ''+idCognos+''].head(1)) != 0:
            valor2 = rates[rates['EMP NUM'] == ''+idCognos+''].head(1).iloc[0]['RATE']
            valor8 = int(float(valor5)*float(valor2))
            if float(valor2) <= 0:
               claseEmbebida.agregarAlertas({'id':''+idCognos+'','mensaje':'The Cognos/rarias is lower or equal to 0 check this value'})  
            elif float(valor2) <= 35000:
               claseEmbebida.agregarAlertas({'id':''+idCognos+'','mensaje':'The Cognos/rarias rate is lower than 35000 COP check this value'})
             
        else:
            valor8 = int(float(valor5)*float(valor2))
            claseEmbebida.agregarErrores({'id':''+idCognos+'','mensaje':'The user is in Cognos but not in Rarias, ask "Rate" to the project manager.'})
            
        # Esta en Forecast?
        if len(forecast[forecast['CNUM (*)'] == ''+idCognos+''].head(1)) != 0:
            valor3 = forecast[forecast['CNUM (*)'] == ''+idCognos+''].head(1).iloc[0]['Band Table - Cost Rate']
            valor6 = forecast[forecast['CNUM (*)'] == ''+idCognos+''].head(1).iloc[0]['Hours']
            valor7 = float(valor5)-float(valor6)
            valor9 = int(float(valor6)*float(valor3))
            
            #Validacion con codigo de error
            valor10 = float(valor8)-float(valor9)
              
            #Validacion con codigo de error
            valor4 = float(valor2)-float(valor3)
            
            if float(valor3) <= 0:
               claseEmbebida.agregarAlertas({'id':''+idCognos+'','mensaje':'The Forecast rate is lower or equal to 0 check this value'}) 
            elif float(valor3) <= 35000:
              claseEmbebida.agregarAlertas({'id':''+idCognos+'','mensaje':'The Forecast rate is lower than 35000 COP check this value'})
              #print(idCognos, valor3)
        else:
            valor3 = '0'
            valor9 = '0'
            valor6 = '0'#ERR62_FORC
            valor4 = float(valor2)-float(valor3)
            valor7 = float(valor5)-float(valor6)
            valor10 = float(valor8)-float(valor9)
            claseEmbebida.agregarAlertas({'id':idCognos,'mensaje':'The user is in Cognos but it is not Forecast, the employee is not planned in the project.'})
            
        solucion = solucion.append({'Id Employee' : ''+str(idCognos)+'','Employee Name' : ''+str(valor1)+'' , 'Rate (Cognos-Rarias)' : ''+str(valor2)+'', 'Rate (Forecast)' : ''+str(valor3)+'', 'Reconcilation Rate' : ''+str(valor4)+'', 'Claim (hours)' : ''+str(valor5)+'', 'Forecast (hours)' : ''+str(valor6)+'', 'Reconcilation Hours' : ''+str(valor7)+'', 'Labor Cost Claim' : ''+str(valor8)+'', 'Forecast Labor Cost' : ''+str(valor9)+'', 'Reconcilation Cost' : ''+str(valor10)+''} , ignore_index=True)
    print(forecast)
    # Ciclo Forecast
    for x in range(len(forecast.index)):
        idForecast = forecast.iloc[x]['CNUM (*)']
        print(idForecast)
        
        if len(rates[rates['EMP NUM'] == ''+idForecast+''].head(1)) == 0 and len(cognos[cognos['Employee Serial Number'] == ''+idForecast+''].head(1)) == 0:
            valor1 = forecast[forecast['CNUM (*)'] == ''+idForecast+''].head(1).iloc[0]['Name Employee']
            valor2 = '0'
            valor3 = forecast[forecast['CNUM (*)'] == ''+idForecast+''].head(1).iloc[0]['Band Table - Cost Rate']
            valor4 = float(valor2)-float(valor3)
            valor5 = '0'#ERR97_COGN
            valor6 = forecast[forecast['CNUM (*)'] == ''+idForecast+''].head(1).iloc[0]['Hours']
            valor7 = float(valor5)-float(valor6)#'ERR12_OPER'
            valor8 = '0'
            valor9 =  float(valor6)*float(valor3)#'ERR12_OPER'
            valor10 = float(valor8)-float(valor9)#'ERR12_OPER'
            solucion = solucion.append({'Id Employee' : ''+str(idForecast)+'','Employee Name' : ''+str(valor1)+'' , 'Rate (Cognos-Rarias)' : ''+str(valor2)+'', 'Rate (Forecast)' : ''+str(valor3)+'', 'Reconcilation Rate' : ''+str(valor4)+'', 'Claim (hours)' : ''+str(valor5)+'', 'Forecast (hours)' : ''+str(valor6)+'', 'Reconcilation Hours' : ''+str(valor7)+'', 'Labor Cost Claim' : ''+str(valor8)+'', 'Forecast Labor Cost' : ''+str(valor9)+'', 'Reconcilation Cost' : ''+str(valor10)+''} , ignore_index=True)
            claseEmbebida.agregarErrores({'id':idForecast,'mensaje':'The user is in Forecast but not in Rarias, ask (Rate) the project manager.'})

            if valor3 <= 0:
                claseEmbebida.agregarAlertas({'id':''+idForecast+'','mensaje':'The Forecast rate is lower or equal to 0 check this value'})
            elif float(valor3) <= 35000:
                claseEmbebida.agregarAlertas({'id':''+idForecast+'','mensaje':'The Forecast rate is lower than 35000 COP check this value'})
                #print(idForecast, valor3)
        #MODIFICAR
        
        elif len(cognos[cognos['Employee Serial Number'] == ''+idForecast+''].head(1)) == 0:
            valor1 = forecast[forecast['CNUM (*)'] == ''+idForecast+''].head(1).iloc[0]['Name Employee']
            #print(rates)
            #print(idCognos)
            valor2 = rates[rates['EMP NUM'] == ''+idForecast+''].head(1).iloc[0]['RATE']
            valor3 = forecast[forecast['CNUM (*)'] == ''+idForecast+''].head(1).iloc[0]['Band Table - Cost Rate']
            valor4 = float(valor2)-float(valor3)
            valor5 = 0
            valor6 = forecast[forecast['CNUM (*)'] == ''+idForecast+''].head(1).iloc[0]['Hours']
            valor7 = float(valor5)-float(valor6)
            valor8 = float(valor5)*float(valor2)
            valor9 = float(valor6)*float(valor3)
            valor10 = float(valor8)-float(valor9)
            solucion = solucion.append({'Id Employee' : ''+str(idForecast)+'','Employee Name' : ''+str(valor1)+'' , 'Rate (Cognos-Rarias)' : ''+str(valor2)+'', 'Rate (Forecast)' : ''+str(valor3)+'', 'Reconcilation Rate' : ''+str(valor4)+'', 'Claim (hours)' : ''+str(valor5)+'', 'Forecast (hours)' : ''+str(valor6)+'', 'Reconcilation Hours' : ''+str(valor7)+'', 'Labor Cost Claim' : ''+str(valor8)+'', 'Forecast Labor Cost' : ''+str(valor9)+'', 'Reconcilation Cost' : ''+str(valor10)+''} , ignore_index=True)
            claseEmbebida.agregarAlertas({'id':idForecast,'mensaje':'The user is in Forecast but it is not Cognos, the employee is not reporting hours.'})
            
            if float(valor2) <= 0:
               claseEmbebida.agregarAlertas({'id':''+idForecast+'','mensaje':'The Cognos/rarias rate is lower than 0 check this value'}) 
            elif float(valor2) <= 35000:
               claseEmbebida.agregarAlertas({'id':''+idForecast+'','mensaje':'The Cognos/rarias rate is lower than 35000 COP check this value'})
               #print(idForecast, valor3)
            if float(valor3) <= 0:
               claseEmbebida.agregarAlertas({'id':''+idForecast+'','mensaje':'The Forecast rate is lower or equal to 0 check this value'}) 
            elif float(valor3) <= 35000:
               claseEmbebida.agregarAlertas({'id':''+idForecast+'','mensaje':'The Forecast rate rate is lower than 35000 COP check this value'})
               #print(idForecast, valor3)
    return solucion
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funciones de normalizacion de datos.

def remove_AreaCode(id):
  return "".join((id[0:-3], id)[id=='-1'])
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def add_ZeroCode(id):
  return "".join(((id, '0'+id)[id[0].isdigit() and id[0] != '0'], id)[id=='-1'])
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def delete_Coma(value):
  return "".join(c for c in value if not c== ',')
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funciones de normalizacion de Rate.
def sum_RateEmployee(proyecto):
  dataRate = proyecto[['EMP NUM','COUNTRY CD','RATE','BANDA']]
  dataRate["RATE"] = dataRate['RATE'].fillna('-1').map(delete_Coma)+';'
  dataRate["BANDA"] = dataRate['BANDA'].fillna('-1').map(delete_Coma)+';'
  return dataRate.groupby(['EMP NUM','COUNTRY CD']).sum()
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def isaNumberF(cadena):
  validacion = False
  try:
    string = cadena.replace('.','')
    #Valida si es un digito y si es cero (Float)
    validacion = (string=='0.00', float(string)==0.0)[string.isdigit()]
  except:
    validacion = False
  return validacion
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def get_IndexMaxRepeat(RepeatElement,index):
  # Remover los punto y coma ';' de los valores
    indRate = [rate for rate in RepeatElement.split(';') ]
    indRate.pop()  #Remover ultimo elemento vacio

    # Obtener Cantidad Elementos Repetidos
    frecuenciaRate = [(indRate.count(w), 0)[isaNumberF(w)] for w in indRate] # En esta linea tambien se valida si el valor es un digito para pasarlo a 'float'
    rateFinal = frecuenciaRate.index(max(frecuenciaRate))

    return indRate[rateFinal]
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def remove_MaxRepeat(Rates):
  data = pd.DataFrame(columns=['EMP NUM','COUNTRY CD','RATE','BANDA'])

  for index in Rates.index.tolist():
    rateFinal = get_IndexMaxRepeat(Rates.loc[index].RATE,index)
    bandaFinal = get_IndexMaxRepeat(Rates.loc[index].BANDA,index)
    #Ingresar al DataFrame
    data = data.append({'EMP NUM': index[0],'COUNTRY CD': index[1],'RATE' :rateFinal,'BANDA':bandaFinal} , ignore_index=True)
  return data


"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def validation_band_rate(Forecast_ready,rarias_Unique,classMessage):
    
  if len(Forecast_ready) < len(rarias_Unique):
    for x in Forecast_ready['CNUM (*)']:
      for y in rarias_Unique['EMP NUM']:
        if x == y:
          #print(x)
          rate1 = float(Forecast_ready[Forecast_ready['CNUM (*)']==x]['Band Table - Cost Rate'])
          rate2 = float(rarias_Unique[rarias_Unique['EMP NUM']==y]['RATE'])

          band1 = str(Forecast_ready[Forecast_ready['CNUM (*)']==x]['Band Description (*)']).split('Band ')[1]
          band2 = str(rarias_Unique[rarias_Unique['EMP NUM']==y]['BANDA']).split(' SERVICE')[0].split('BAND')[1]

          #cases = 0

          if rate1 == rate2:
            if band2 in band1:
              classMessage.agregarAlertas({'id':''+x+'','mensaje':'success match'})
            else:
              classMessage.agregarAlertas({'id':''+x+'','mensaje':'The employee rate does not change, however band change'})
          else:
            if band2 in band1:
              classMessage.agregarAlertas({'id':''+x+'','mensaje':'The employee rate change, however band does not change'})
            else:
              classMessage.agregarAlertas({'id':''+x+'','mensaje':'The employee rate change and band change'})


def problema(Forecast_ready):
    y=-1
    index=0
    for x in Forecast_ready['CNUM (*)']:
        y=y-1
        if x==-1:
            Forecast_ready['CNUM (*)'][index]=y-1
        
        index=index+1  
        print('problema', index,y)
    return Forecast_ready['CNUM (*)']
            

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def postReport(codigo, fecha, nombreProyecto, archivo ):
    a = str(uuid.uuid4())
    a = a[:12]
    data = {}
    data = {'codigo':codigo,'fecha':fecha,'nombreProyecto':nombreProyecto, 'archivo':archivo,'reporteId': a}
    firebase.put('/PMA/Reports', a, data)
    return a

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def total_ReconciliationTable(ReconciliationTable):
  totalClaim = ReconciliationTable["Claim (hours)"].replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0).astype('float').sum()
  totalForecast = ReconciliationTable["Forecast (hours)"].replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0).astype('float').sum()
  totalReconcilation = ReconciliationTable["Reconcilation Hours"].replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0).astype('float').sum()
  totalLaborCost = ReconciliationTable["Labor Cost Claim"].replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0).astype('float').sum()
  totalForecastCost = ReconciliationTable["Forecast Labor Cost"].replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0).astype('float').sum()
  totalReconcilationCost = ReconciliationTable["Reconcilation Cost"].replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0).astype('float').sum()
  return ReconciliationTable.append({'Id Employee' : 'Grand Total','Employee Name' : '' , 'Rate (Cognos-Rarias)' : '', 'Rate (Forecast)' : '', 'Reconcilation Rate' : '', 'Claim (hours)' : ''+str(totalClaim)+'', 'Forecast (hours)' : ''+str(totalForecast)+'', 'Reconcilation Hours' : ''+str(totalReconcilation)+'', 'Labor Cost Claim' : ''+str(totalLaborCost)+'', 'Forecast Labor Cost' : ''+str(totalForecastCost)+'', 'Reconcilation Cost' : ''+str(totalReconcilationCost)+''} , ignore_index=True)

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
def graphs_Reconcilation(Final_Table,x):
  image = Final_Table.replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0)
  w=10
  h=10
  n_groups = len(image['Employee Name'])
  xnames = [name.upper() for name in np.array(image['Employee Name'])]
  
  if x == 1:
    # data to plot   
    means_guido = np.array(image['Reconcilation Cost'].astype('float'))


    # create plot
    fig, ax = plt.subplots(figsize=(w,h))
    index = np.arange(n_groups)
    bar_width = 0.55
    opacity = 0.8

    plt.barh(index + bar_width, np.array(means_guido), bar_width,
    alpha=opacity,
    color='b',
    label='Reconcilation Cost')

    plt.xlabel('Values')
    plt.ylabel('Person')
    plt.title('Scores by person')
    plt.yticks(index + bar_width, xnames,rotation=0)
    plt.legend()

    plt.tight_layout()
    
  
  elif x == 2:
    # data to plot
    means_guido = np.array(image['Reconcilation Rate'].astype('float'))

    # create plot
    fig, ax = plt.subplots(figsize=(w,h))
    index = np.arange(n_groups)
    bar_width = 0.55
    opacity = 0.8

    plt.barh(index + bar_width, np.array(means_guido), bar_width,
    alpha=opacity,
    color='g',
    label='Reconcilation Rate')

    plt.xlabel('Values')
    plt.ylabel('Person')
    plt.title('Scores by person')
    plt.yticks(index + bar_width, xnames,rotation=0)
    plt.legend()

    plt.tight_layout()
    
  elif x == 3:
    # data to plot
    means_guido = np.array(image['Reconcilation Hours'].astype('float'))

    # create plot
    fig, ax = plt.subplots(figsize=(w,h))
    index = np.arange(n_groups)
    bar_width = 0.55
    opacity = 0.8

    plt.barh(index + bar_width, np.array(means_guido), bar_width,
    alpha=opacity,
    color='r',
    label='Reconcilation Hours')

    plt.xlabel('Values')
    plt.ylabel('Person')
    plt.title('Scores by person')
    plt.yticks(index + bar_width, xnames,rotation=0)
    plt.legend()

    plt.tight_layout()
    
  figfile = BytesIO()
  plt.savefig(figfile, format='png')
  figfile.seek(0)  # rewind to beginning of file
  figdata_png = base64.b64encode(figfile.getvalue())
  #print(figdata_png) 
  return figdata_png

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""    
def graphs_Reconcilationcompar(Final_Table,x):
  
  image = Final_Table.replace('ERR20_NULL',0).replace('ERR12_OPER',0).replace('ERR69_RECO',0).replace('ERR79_RNRT',0).replace('ERR62_FORC',0).replace('ERR97_COGN',0)
  w=10
  h=10
  n_groups = len(image['Employee Name'])
  xnames = [name.upper() for name in np.array(image['Employee Name'])]
  
  if x == 1:    # data to plot
    means_frank = np.array(image['Claim (hours)'].astype('float'))
    means_guido = np.array(image['Forecast (hours)'].astype('float'))

    # create plot
    fig, ax = plt.subplots(figsize=(w,h))
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    
    plt.barh(index, means_frank, bar_width,
    alpha=opacity,
    color='g',
    label='Claim (hours)')

    plt.barh(index + bar_width, np.array(means_guido), bar_width,
    alpha=opacity,
    color='b',
    label='Forecast (hours)')

    plt.xlabel('Values')
    plt.ylabel('Person')
    plt.title('Hours-comparation by person')
    plt.yticks(index + bar_width, xnames,rotation=0)
    plt.legend()

    plt.tight_layout()
    #plt.show()
    
  elif x == 2:
   
    # data to plot
    means_frank = np.array(image['Forecast Labor Cost'].astype('float'))
    means_guido = np.array(image['Labor Cost Claim'].astype('float'))
    
    # create plot
    fig, ax = plt.subplots(figsize=(w,h))
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    
    plt.barh(index, means_frank, bar_width,
    alpha=opacity,
    color='g',
    label='Forecast Labor Cost')

    plt.barh(index + bar_width, np.array(means_guido), bar_width,
    alpha=opacity,
    color='b',
    label='Labor Cost Claim')

    plt.xlabel('Values')
    plt.ylabel('Person')
    plt.title('Scores by person')
    plt.yticks(index + bar_width, xnames,rotation=0)
    plt.legend()

    plt.tight_layout()
    #plt.show()
    
  elif x == 3:
    
    # data to plot
    means_frank = np.array(image['Rate (Cognos-Rarias)'].astype('float'))
    means_guido = np.array(image['Rate (Forecast)'].astype('float'))

    # create plot
    fig, ax = plt.subplots(figsize=(w,h))
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    
    plt.barh(index, means_frank, bar_width,
    alpha=opacity,
    color='g',
    label='Rate (Cognos-Rarias)')

    plt.barh(index + bar_width, np.array(means_guido), bar_width,
    alpha=opacity,
    color='b',
    label='Rate (Forecast)')

    plt.xlabel('Values')
    plt.ylabel('Person')
    plt.title('Scores by person')
    plt.yticks(index + bar_width, xnames,rotation=0)
    plt.legend()

    plt.tight_layout()
   # plt.show()
    
  figfile = BytesIO()
  plt.savefig(figfile, format='png')
  figfile.seek(0)  # rewind to beginning of file
  figdata_png = base64.b64encode(figfile.getvalue())
  #print(figdata_png)    
      
  return figdata_png
  

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

def TRM_Conversion(rarias_TRM):
  
  #Diccionario siglas
  valores = {'661' : 'COP', '613' : 'ARS' , '683' : 'USD' , '815' : 'PEN' , '655' : 'CLP' , '631' : 'BRL', '781' : 'MXN', '869' : 'UYU', '871' : 'VEF' }
  pais=rarias_TRM[['COUNTRY CD','RATE']].dropna()
  #Index del dataframe
  index=pais[pais['COUNTRY CD']!=661].index.tolist()
  #Request a la api de las monedas
  r = requests.get("https://api.worldtradingdata.com/api/v1/forex?base=COP&api_token=jZ4ddTM2UvH22meMAxUkKAVoVxodkuBAFOo71MgP6O0PuQgJQSQ2Z5QgivoD")
  #Recorrer indices en dataframe
  
  for x in index:
    if r.status_code == 200:
      data = r.json()['data']
      
    #Codigo pais  
    origen=pais['COUNTRY CD'][x]
    #Valor Rate pais
    valor=pais['RATE'][x]
    
    #Valores para multiplicar
    valorint = float(valor.replace(',',''))
    #Busca Codigo en Diccionario
    origen2str = valores.get(origen)
    
    #Busca el cambio de ese pais
    
    if origen2str != 'COP'and origen2str != 'VEF':
      #print(data)
      cambio = (data[origen2str])
      #Saca nuevo Rate
      nuevoRate = float(round((valorint / float(cambio))))
      #print(origen2str,valorint,cambio,nuevoRate)
      #Actualiza Dataframe
      rarias_TRM.set_value(x,'RATE',str(nuevoRate))
      #print("Cambiando Tasa ...")

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
    #app.run(host="9.86.158.250")
    #app.run()
    #app.run()
