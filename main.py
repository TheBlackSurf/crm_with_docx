from pdf2docx import Converter

pdf_file = '/home/grzegorz/crm_test/crm/pdf.pdf'
docx_file = '/home/grzegorz/crm_test/crm/pdf.docx'
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()