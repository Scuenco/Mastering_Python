# Adding a Watermark with PyPDF2
import PyPDF2

def pdf_watermark():
    reader = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    writer = PyPDF2.PdfFileWriter() #creates a write object in memory
    pages = reader.getNumPages()

    for i in range(pages):
        page = reader.getPage(i)
        page.mergePage(watermark.getPage(0)) 
        writer.addPage(page)

    with open('watermarked.pdf', 'wb') as watermarked:
        writer.write(watermarked)

pdf_watermark()

