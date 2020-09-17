import sys
from leer_instancias_pruebas import read_data_XLSX
import xlsxwriter
from grasp_tardiness import GRASP_Tardiness
import fo_tardiness as fo
import time

def principal(argv):
    INSTANCIAS = read_data_XLSX()
    
    num_alphas = 5
    ALPHAS = [round(i*(1/num_alphas),3) for i in range(num_alphas+1)]
    print(ALPHAS)
    
    for a in ALPHAS:
        workbook = xlsxwriter.Workbook('Results_Tardiness ALPHA('+str(a)+').xlsx')
        ti = time.time()
        for inst in INSTANCIAS:
            ## Parámetros de la instancia
            tp = inst.tiempos_procesamiento
            dd = inst.due_dates
            num_trabajos = len(tp)
            num_maquinas = len(tp[0])
            
            ## Obtener secuencia de Grasp_Makespan
            ALPHA = a
            t_max = 1 * num_trabajos * num_maquinas
            repeticiones = 10
            minimo = 10000000000000
            print("AlPHA: ", a, "; Inst:", INSTANCIAS.index(inst))
            for _ in range(repeticiones):
                t1 = time.time()
                s, s_bl = GRASP_Tardiness(tp, dd, ALPHA, t_max)
                f = fo.calcular_tardanza_blocking_secuencia(s_bl, tp, dd)
                print(f)
                if( f < minimo ):
                    minimo = f
                    secuencia = s
                    secuencia_bl = s_bl
                    tiempo_funcion = time.time() - t1
                #fi
            #rof
            print("----------------------------")
            
            ## Indicadores
            makespan = fo.calcular_makespan_blocking_secuencia(secuencia, tp)
            tardanza = fo.calcular_tardanza_blocking_secuencia(secuencia, tp, dd)
            makespan_bl = fo.calcular_makespan_blocking_secuencia(secuencia_bl, tp)
            tardanza_bl = fo.calcular_tardanza_blocking_secuencia(secuencia_bl, tp, dd)
            
            ## Imprimir archivo
            nombre_hoja = "Inst"+str(INSTANCIAS.index(inst)+1)
            imprimir_XLSX(workbook, nombre_hoja, secuencia, secuencia_bl, makespan, tardanza, makespan_bl, tardanza_bl, tiempo_funcion)
        #rof
        tt = time.time() - ti
        worksheet = workbook.add_worksheet("TIEMPO TOTAL")
        worksheet.merge_range(1, 1, 1, 3, "Tiempo total de ejecución")
        worksheet.merge_range(1, 4, 1, 5, round(tt,2))
        workbook.close()
        workbook.close()
    #rof
#fed

def imprimir_XLSX(workbook, nombre_hoja, secuencia, secuencia_bl, makespan, tardanza, makespan_bl, tardanza_bl, tiempo_funcion):
    worksheet = workbook.add_worksheet(nombre_hoja)
    
    worksheet.set_column(1, 1, 9.5)
    worksheet.set_column(2, 100, 4)
    
    cell_format_bold = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter'})
    cell_format = workbook.add_format({'align': 'center'})

    worksheet.merge_range("B2:F2","FASE DE CONSTRUCCIÓN", cell_format_bold)
    worksheet.write("B3", "Secuencia", cell_format_bold)
    
    
    row = 2
    col = 2
    for s in secuencia:
        worksheet.write(row, col, s, cell_format)
        col += 1
    #rof
    worksheet.write("B4", "Makespan", cell_format_bold)
    worksheet.merge_range("C4:D4", makespan, cell_format)
    
    worksheet.write("B5", "Tardanza", cell_format_bold)
    worksheet.merge_range("C5:D5", tardanza, cell_format)
    

    worksheet.merge_range("B7:F7", "FASE DE BUSQUEDA LOCAL", cell_format_bold)
    worksheet.write("B8", "Secuencia", cell_format_bold)
    
    row = 7
    col = 2
    for s in secuencia_bl:
        worksheet.write(row, col, s, cell_format)
        col += 1
    #rof
    worksheet.write("B9", "Makespan", cell_format_bold)
    worksheet.merge_range("C9:D9", makespan_bl, cell_format)
    
    worksheet.write("B10", "Tardanza", cell_format_bold)
    worksheet.merge_range("C10:D10", tardanza_bl, cell_format)
    
    worksheet.merge_range("B12:F12", "TIEMPO DE EJECUCIÓN (seg):", cell_format_bold)
    worksheet.merge_range("G12:H12", tiempo_funcion, cell_format)
#fed


if __name__ == "__main__":
    ti = time.time()
    principal(sys.argv)
    print("TIEMPO TOTAL DEL PROGRAMA: ", time.time()-ti)
#fi