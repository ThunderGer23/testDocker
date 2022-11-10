# 

FROM python

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

ENV PYHTONUNBUFFERED=1
RUN apt-get update \
  && apt-get -y install tesseract-ocr \ # required for pytesseract

RUN apt-get -y install ffmpeg libsm6 libxext6 # required for opencv

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

#FROM python

# 
#WORKDIR /code

# 
#COPY ./requirements.txt /code/requirements.txt

# 
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
#COPY ./ /code

# 
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
