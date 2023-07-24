=========================Emvironment
system: 
    windows10
pip:
    pytesseract 0.3.10
    PyMuPDF     1.22.5
    Pillow      10.0.0
software:
    tesseractOCR w64-5.3.1

        install tesseractOCR and add to system variable, check tutorial, add chi-sim language pack,
    change <tesseract_cmd = 'path'> in pytesseract.py, path = 'Tesseract location\Tesseract-OCR/tesseract.exe'
        after install, make sure tesseract_demo.py can run

=========================File
Demo.png: test image 
tesseract_demo.py:      OCR Demo
pdf_segment.py:         using PyMuPDF to segment PDF and save as png image file
segment_OCR.py:         2 mode that pdf2txt or image2txt after pdf_segment 
