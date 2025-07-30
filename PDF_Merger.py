from PyPDF2 import PdfWriter 
merger = PdfWriter()  
n = int(input("Enter the number of PDFs to merge: "))
pdfs = []
for i in range(n):
    name = input(f"Enter the name of PDF {i+1}: ")
    pdfs.append(open(name, 'rb'))
for pdf in pdfs:
    merger.append(pdf)
merger.write(open("merged_pdf.pdf", 'wb'))
merger.close()





















