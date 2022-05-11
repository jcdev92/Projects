import openpyxl
 
doc = openpyxl.load_workbook ("webs.xlsx")
hoja = doc.get_sheet_by_name("webs")
 
 
 
webs=[]
for row in hoja.iter_rows():
    pages = row[1].value
    webs.append(pages)

print(webs)