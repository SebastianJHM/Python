def print_results_XLSX( workbook, nombre_hoja, arch, tiempo_ejecucion):
    
    ## Crear hoja
    worksheet = workbook.add_worksheet(nombre_hoja)
    
    x = [a.makespan for a in arch]
    y = [a.tardanza for a in arch]
    
    ## STYLES
    title = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1,
        'bg_color': '#8DB4E2'})
    
    cell_format_bold = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter'})
    cell_format = workbook.add_format({'align': 'center'})
    
    worksheet.merge_range(1, 1, 1, 3, "INSTANCIA", title)
    worksheet.merge_range(1, 5, 1, 10, "Tiempo de ejecución(s)", cell_format_bold)
    worksheet.merge_range(1, 11, 1, 12, round(tiempo_ejecucion,2), cell_format)
    row = 3
    for sol in arch:
        
        ## Imprimir secuencia
        col = 1
        worksheet.write(row, col, "Solución", cell_format_bold)
        worksheet.set_column(col, col, 9)
        col += 1
        for s in sol.secuencia:
            worksheet.write(row, col, s, cell_format)
            worksheet.set_column(col, col, 3) ## Width: set_column(first_col, last_col, width, cell_format, options)
            col += 1
        #rof
        
        worksheet.set_column(col, col, 3)
        
        ## Imprimir makespan
        col += 1
        worksheet.write(row, col, "Makespan", cell_format_bold)
        worksheet.set_column(col, col, 10)
        col += 1
        worksheet.write(row, col, sol.makespan, cell_format)
        worksheet.set_column(col, col, 6)
        
        col += 1
        worksheet.set_column(col, col, 3)
        
        ## Imprimir tardanza
        col += 1
        worksheet.write(row, col, "Tardanza", cell_format_bold)
        worksheet.set_column(col, col, 9)
        col += 1
        worksheet.write(row, col, sol.tardanza, cell_format)
        worksheet.set_column(col, col, 6)
        
        row += 1
    #rof
        
    
    len(arch[0].secuencia)
    
    ## Create a new scatter chart.
    chart1 = workbook.add_chart({'type': 'scatter'})
        
    chart1.add_series({
        'categories': [nombre_hoja, 3, len(arch[0].secuencia)+4, row-1, len(arch[0].secuencia)+4],
        'values':     [nombre_hoja, 3, len(arch[0].secuencia)+7, row-1, len(arch[0].secuencia)+7],
        'marker':     {'type': 'circle', 'size': 7},
        'data_labels': {'category': True,'value': True, 'position': 'right'},
        'y_axis': True,
    })
    
    
    # Add a chart title and some axis labels.
    chart1.set_title({'name': 'Makespan vs Tardanza'})
    chart1.set_x_axis({
        'name': 'Makespan', 
        'min': min(x)-3, 
        'major_gridlines': {'visible': True,'line': {'width': 1}}
    })
    chart1.set_y_axis({'name': 'Tardanza', 'min': min(y)-5})
    
    chart1.set_legend({'none': True})
    
    # Set an Excel chart style.
    chart1.set_style(2)
    
    # Insert the chart into the worksheet (with an offset).
    worksheet.insert_chart(row+1, 1, chart1, {'x_offset': 0, 'y_offset': 0})
    
#fed