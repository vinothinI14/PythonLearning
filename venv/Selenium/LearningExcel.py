from openpyxl import load_workbook

filepath = "C:\\Users\\ADMIN\\Desktop\\SampleTest.xlsx"
Dict = {}
wrBook = load_workbook(filepath)
sheet = wrBook.active
rowsCount = sheet.max_row
colsCount = sheet.max_column
print(sheet.cell(row=1,column=3).value)
sheet.cell(row=2,column=3).value = 300
print(sheet.cell(row=2,column=3).value)

#Printing values with specific condition
for r in range(1,rowsCount+1):
    if sheet.cell(row=r,column=1).value == "Three":
        for j in range(1,colsCount+1):
            print(sheet.cell(row=r,column=j).value)

#Adding values into dict at runtime

for r in range(1,rowsCount+1):
    if sheet.cell(row=r, column=1).value == "Two":
        for c in range(1,colsCount+1):
            Dict[sheet.cell(row=1,column=c).value] = sheet.cell(row=r, column=c).value
print(Dict)



