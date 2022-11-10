from fastapi import APIRouter
from PIL  import Image
from pytesseract  import pytesseract
pytesseract.tesseract_cmd = r''

test = APIRouter()

@test.get('/test')
def test():
    im = Image('../Pruebame.png')
    texto = pytesseract.image_to_string(im)
    return texto

