from fastapi import APIRouter, File, UploadFile
from PIL import Image
from models.files import Files
from pytesseract import pytesseract
from config.db import conn
from os import getcwd
from docs import tags_metadata
import io
from typing import List

pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

test = APIRouter()

@test.get('/test', response_model=str, tags=["Test"])
def testing():
    """
    It takes an image, converts it to text, and returns the text
    :return: The text that is in the image.
    """
    im = Image.open(getcwd()+'/Pruebame.png')
    texto = pytesseract.image_to_string(im)
    return texto

@test.post('/submit', response_model= str, tags=["Test"])
async def submit_image(file: UploadFile = File(...),):
    """
    It takes an image file as input, and returns the text in the image as output
    
    :param file: UploadFile = File(...)
    :type file: UploadFile
    :return: The text that was extracted from the image.
    """
    image = Files()
    image.name = file.filename
    image.data = await file.read()
    id = conn.local.testimage.insert_one(image).inserted_id
    with Image.open(io.BytesIO(await file.read())) as pic:
        texto = pytesseract.image_to_string(pic)
    return str({texto, id})

@test.post('/submit_more', response_model= dict(), tags=["Test"])
async def submit_images(files: List[UploadFile]):
    """
    It takes a list of files, reads them, and returns a dictionary of the file names and their text
    
    :param files: List[UploadFile]
    :type files: List[UploadFile]
    :return: A dictionary with the filename as the key and the text as the value.
    """
    res = dict()
    for file in files:
        with Image.open(io.BytesIO(await file.read())) as pic:
            res[file.filename] = pytesseract.image_to_string(pic)
    return res