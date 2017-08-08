import openpyxl

filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.worksheets[0]

data = []
for row in sheet.rows:
	data.append([
			row[0].value,
			row[10].value
	])
print(data[0], data[1], data[2])
del data[0]
del data[1]
del data[2]
print(data[0], data[1], data[2])

data = sorted(data, key=lambda x:x[1])

for i, a in enumerate(data):
	if(i >= 5): break
	print(i+1, a[0], int(a[1]))
