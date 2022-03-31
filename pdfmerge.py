import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Concatenate PDF files.')
    parser.add_argument('input_files', nargs='+',
                        help='Input PDF files to concatenate')
    parser.add_argument('--output', dest='output', default="merged.pdf",
                        help='Output file name (default: "merged.pdf")')

    args = parser.parse_args()
    merge_pdfs(args.input_files, output=args.output)
