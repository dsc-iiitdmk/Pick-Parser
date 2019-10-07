from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 

#pytesseract.pytesseract.tesseract_cmd = "/usr/share/tesseract-ocr/4.00/tessdata"

def generate_images_and_text_from_pdf(PDF_file,target_dir):
    pages = convert_from_path(PDF_file, 500)
    image_counter = 1

    for page in pages:
        filename = target_dir+"/page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG') 
        image_counter = image_counter + 1

    filelimit = image_counter-1

    outfile = target_dir+"/out_text.txt"

    f = open(outfile, "w",encoding="utf-8") 

    for i in range(1, filelimit + 1): 
        filename = target_dir+"/page_"+str(i)+".jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        text = text.replace('-\n', '') 
        f.write(text) 

    f.close()
