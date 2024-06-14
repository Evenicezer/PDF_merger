import PyPDF2

def merge_pdfs(file1, file2, output_file):
    '''merges two files into one'''
    with open(file1, 'rb') as f1:
        pdf1 = PyPDF2.PdfReader(f1)

        # Open the second PDF file
        with open(file2, 'rb') as f2:
            pdf2 = PyPDF2.PdfReader(f2)

            # Create a new PDF writer object
            writer = PyPDF2.PdfWriter()

            # Merge the pages from the first PDF
            for page_num in range(len(pdf1.pages)):
                page = pdf1.pages[page_num]
                writer.add_page(page)

            # Merge the pages from the second PDF
            for page_num in range(len(pdf2.pages)):
                page = pdf2.pages[page_num]
                writer.add_page(page)

            # Write the merged PDF to the output file
            with open(output_file, 'wb') as output:
                writer.write(output)

# Example usage
merge_pdfs(r"pdf_1", r"pdf_2", 'merged.pdf')
