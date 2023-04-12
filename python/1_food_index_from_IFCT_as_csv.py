import PyPDF2
import csv

# This script reads the content from page # 539 to page #572 (INDEX) in the 
# given IFCT PDF file and stores them in a csv file
# INPUT: IFCT.PDF
# OUTPUT: regionalNames.csv

# Open the PDF file and create a PDF reader object
with open('IFCT.pdf', mode='rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Specify the page range
    page_range = (539, 572)
    lines = []

    # Iterate over the specified pages
    for page_num in range(*page_range):
        page = reader.pages[page_num]
        # Extract the text from the PDF page
        text = page.extract_text()
        # Split the text into lines
        lines.extend(text.split('\n'))

    # Open the CSV file for writing
    with open('regionalNames.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the lines to the CSV file
        for line in lines:
            writer.writerow([line])