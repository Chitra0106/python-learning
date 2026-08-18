
f = open("test.txt")
p = open(r"C:\Users\mailc\OneDrive\Desktop\lemonLawCommands.json", 'rt')
content = p.read()
print(content)
o=open("ll.txt","w")
o.write(content)
o.close()
p.close()
f.close()
#Append to an existing file
f= open("test.txt","a")
string = '''  this is for appending '''
f.write(string)
 # the below is to read the excel
from openpyxl import load_workbook
wb = load_workbook(r"C:\Users\mailc\OneDrive\Desktop\UiPath_Learning_8_Week_Roadmap.xlsx")
sheet = wb.active
print(sheet["A1"].value)