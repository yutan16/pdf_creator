import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(f'./pdf_playground/{pdf}')
        print(pdf)
    merger.write('./pdf_playground/merged.pdf')


pdf_combiner(inputs)
