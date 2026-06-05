import pypdf as m

def decorator(func):
    def greet(*args, **kwargs):
        print("Welcome to the PDF Merger!")
        return func(*args, **kwargs)
    return greet

@decorator
def merge_pdfs(pdf_list,output):
    pdf_list = input("Enter the names of the PDF files you want to merge (comma separated): ").split(",")
    output = input("Enter the name of the output PDF file (with .pdf extension): ")

    merger = m.PdfWriter()
    while True:    
        for pdf in pdf_list:
            if pdf == "BITS012547.pdf":
                pass
            else:
                merger.append(pdf)
        
        merger.write(output)
    
merge_pdfs(pdf_list=None, output=None)
