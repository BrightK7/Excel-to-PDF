from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
logo = ImageReader('https://www.google.com/images/srpr/logo11w.png')

canvas = Canvas('output.pdf', pagesize=letter)
canvas.drawImage(logo, 10, 10,width=100,height=100, mask='auto')
canvas.showPage()
canvas.save()