import openpyxl
 
doc = openpyxl.load_workbook ("datos.xlsx")
hoja = doc.get_sheet_by_name("peliculas")
 
 
 
l=[]
for row in hoja.iter_rows():
    peliculas = row[0].value
    l.append(peliculas)
 
print l