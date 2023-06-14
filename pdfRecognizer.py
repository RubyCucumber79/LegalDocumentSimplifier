from pdf2image import convert_from_path
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\SHAHNAWZ KHAN\AppData\Local\Programs\Tesseract-OCR\tesseract'
#from pytesseract import image_to_string
from PIL import Image

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file,500,poppler_path=r'C:\Program Files (x86)\poppler-23.05.0\Library\bin')

def convert_image_to_text(image):
    text = tess.image_to_string(image)
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        text = convert_image_to_text(img)
        final_text += text

        # Append the OCR text to the file
        with open("ocr_text.txt", "a") as file:
            file.write(text)

        # Uncomment the following lines if you want to print the OCR text for each page
        # print("Page n°{}".format(pg))
        # print(text)

    return final_text
path_to_pdf = '1.pdf'
print(get_text_from_any_pdf(path_to_pdf))
