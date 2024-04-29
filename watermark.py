import PyPDF2


def watermark_pdf(pdf, watermark_pdf):
    watermark = PyPDF2.PdfFileReader(
        open(f'./pdf_playground/{watermark_pdf}', 'rb'))
    reader = PyPDF2.PdfFileReader(open(f'./pdf_playground/{pdf}', 'rb'))
    writer = PyPDF2.PdfFileWriter()
    i = 0
    for i in range(reader.numPages):
        page = reader.pages[i]
        page.mergePage(watermark.pages[0])
        writer.addPage(page)
    with open('./pdf_playground/watermarked.pdf', 'wb') as file:
        writer.write(file)


watermark_pdf('merged.pdf', 'wtr.pdf')
