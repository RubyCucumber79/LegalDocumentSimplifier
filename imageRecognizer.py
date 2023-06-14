import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\SHAHNAWZ KHAN\AppData\Local\Programs\Tesseract-OCR\tesseract'
from PIL import Image

img = Image.open('zz.PNG')
text = tess.image_to_string(img)


with open('ocr_text.txt', 'a') as file:
    file.write(text + '\n')

print(text)
