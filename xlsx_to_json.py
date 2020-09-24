import pandas,xlrd,sys,PyPDF2
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import ImageReader

  
wb = xlrd.open_workbook(sys.argv[1]) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 

logo = ImageReader('https://www.google.com/images/srpr/logo11w.png')
for j in range (1,sheet.nrows):
    left_size = 72
    height_size = 792
    canvas = Canvas("%s.pdf"%(sheet.cell_value(j, 2)),pagesize=LETTER)
    for i in range(1,sheet.ncols):
        add_str = ""
        if i == 1:
            add_str = "Email: "
        elif i == 2:
            add_str = "Name: "
        elif i == 3:
            add_str = "Phone Number: "
            canvas.drawString(left_size, height_size-30*i, add_str+str(int(sheet.cell_value(j, i))))
            continue
        elif i == 4:
            add_str = "Gender: "
        elif i == 5:
            add_str = "Height: "
        elif i == 6:
            add_str = "Age: "
            canvas.drawString(left_size, height_size-30*i, add_str+str(int(sheet.cell_value(j, i))))
            continue
        elif i == 7:
            add_str = "Skin Tone: "
        elif i == 8:
            canvas.drawString(left_size, height_size-30*i, sheet.cell_value(j, i))
        elif i == 9:
            add_str = "Colour of tattoo: "
        elif i == 10:
            canvas.drawImage(logo, left_size, height_size-30*i-100,width=100,height=100, mask='auto')
            height_size -= 100
            continue
        elif i == 11:
            add_str = "Placement on your body and approximate size: "
        elif i == 12:
            canvas.drawImage(logo, left_size, height_size-30*i-100,width=100,height=100, mask='auto')
            height_size -= 100
            continue
        elif i == 13:
            add_str = "Budget: "
        print(i,type(sheet.cell_value(1, i)))
        canvas.drawString(left_size, height_size-30*i, add_str+sheet.cell_value(j, i))
    canvas.save()
