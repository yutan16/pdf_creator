import PyPDF2

with open('./pdf_playground/dummy.pdf', 'r') as my_pdf:
    print(my_pdf)

# You have to make the mode 'rb' for open to read it through binary (or PyPDF2 can't read it)
with open('./pdf_playground/dummy.pdf', 'rb') as my_pdf:
    reader = PyPDF2.PdfFileReader(my_pdf)
    page1 = reader.getPage(0)
    page1.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page1)
    print(reader.numPages)
    with open('./pdf_playground/rotate_dummy.pdf', 'wb') as file:
        writer.write(file)
