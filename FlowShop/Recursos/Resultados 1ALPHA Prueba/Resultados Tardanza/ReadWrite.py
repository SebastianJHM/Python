import sys
from leer_instancias_pruebas import read_data_XLSX
import funciones_objetivo_prueba as fo
import xlsxwriter
from grasp_tardiness import GRASP_Tardiness
import fo_tardiness as fo_aux

def principal(argv):
    INSTANCIAS = read_data_XLSX()
    workbook = xlsxwriter.Workbook('Results_Tardiness.xlsx')
    for inst in INSTANCIAS:
        
        ## Parámetros de la instancia
        tp = inst.tiempos_procesamiento
        dd = inst.due_dates
        
        ## Obtener secuencia de Grasp_Makespan
        ALPHA = 0.5
        num_iteraciones = 30
        secuencia, secuencia_bl = GRASP_Tardiness(tp, dd, ALPHA, num_iteraciones)
        
        ## Matrices de tiempos de inicio y fin
        makespan, make_mat_i, make_mat_f = fo.calcular_makespan_blocking_secuencia(secuencia_bl, tp)
        tardanza, due_date_sec = fo.calcular_tardanza_blocking_secuencia(secuencia_bl, tp, dd)
        
        ## Imprimir archivo
        nombre_hoja = "Inst"+str(INSTANCIAS.index(inst)+1)
        imprimir_XLSX(workbook, nombre_hoja, secuencia, secuencia_bl, makespan, make_mat_i, make_mat_f, tardanza, due_date_sec, tp, dd)
    #rof
    workbook.close()
#fed

def imprimir_XLSX(workbook, nombre_hoja, secuencia, secuencia_bl, makespan, make_mat_i, make_mat_f, tardanza, due_date_sec, tp, dd):
    worksheet = workbook.add_worksheet(nombre_hoja)
    
    worksheet.set_column(1, 1, 9.5)
    
    cell_format_bold = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter'})
    cell_format = workbook.add_format({'align': 'center'})
    
    worksheet.merge_range("B2:D2", "FASE DE CONSTRUCCIÓN", cell_format_bold)
    worksheet.write("B3", "Secuencia", cell_format_bold)
    
    row = 2
    col = 2
    for s in secuencia:
        worksheet.write(row, col, s, cell_format)
        col += 1
    #rof
    worksheet.write("B4", "Tardanza", cell_format_bold)
    worksheet.write("C4", fo_aux.calcular_tardanza_blocking_secuencia(secuencia, tp, dd), cell_format)
    
    worksheet.write("B5", "Makespan", cell_format_bold)
    worksheet.write("C5", fo_aux.calcular_makespan_blocking_secuencia(secuencia, tp), cell_format)
    
    
    
    
    worksheet.merge_range("B7:D7", "FASE DE BUSQUEDA LOCAL", cell_format_bold)
    worksheet.write("B8", "Secuencia", cell_format_bold)
    
    row = 7
    col = 2
    for s in secuencia_bl:
        worksheet.write(row, col, s, cell_format)
        col += 1
    #rof
    worksheet.write("B9", "Tardanza", cell_format_bold)
    worksheet.write("C9", tardanza, cell_format)
        
    worksheet.write("B10", "Makespan", cell_format_bold)
    worksheet.write("C10", makespan, cell_format)
    
    
    
        
    row = 11
    col = 1
    worksheet.merge_range(row, col, row, col+4, "Matriz Tiempos Inicio", cell_format_bold)
    worksheet.merge_range(row, col+len(make_mat_i[0])+1, row, col+len(make_mat_i[0])+5, "Matriz Tiempos Finales", cell_format_bold)
    worksheet.merge_range(row, col+2*len(make_mat_i[0])+2, row, col+2*len(make_mat_i[0])+3, "Due Dates(SEC)", cell_format_bold)
    
    row += 1
    for i in range(len(make_mat_i)):
        col = 1
        col2 = 2 + len(make_mat_i[i])
        for j in range(len(make_mat_i[i])):
            worksheet.write(row, col, make_mat_i[i][j], cell_format)
            col += 1
            
            worksheet.write(row, col2, make_mat_f[i][j], cell_format)
            col2 += 1
        #rof      
        worksheet.merge_range(row, col2+1,row, col2+2, due_date_sec[i], cell_format)
        row += 1
    #rof
#fed


if __name__ == "__main__":
    principal(sys.argv)
#fi