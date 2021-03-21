import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "hI"
print(sheet.title)
sheet["A4"].value = "seessese"
workbook.save("C:\\Users\\Admin\\Documents\\pys1.xlsx")
