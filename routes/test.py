from fastapi import APIRouter
from PIL import Image
from pytesseract import pytesseract
from os import getcwd

pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

test = APIRouter()

@test.get('/test')
def testing():
    im = Image.open(getcwd()+'/Pruebame.png')
    texto = pytesseract.image_to_string(im)
    return texto

