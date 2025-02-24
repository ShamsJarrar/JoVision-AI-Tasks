from PIL import Image
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

try:
    path = sys.argv[1]
    pic = Image.open(path)

    image_text = pytesseract.image_to_string(pic)
    print("Image Text:")
    print(image_text)

except Exception as e:
    print(f"Error: {e}")