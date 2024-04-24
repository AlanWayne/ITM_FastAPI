# from sqlalchemy import Column
from models import Document, Documents_text
from sqlalchemy.orm import Session
from fastapi import UploadFile
from os.path import expanduser, abspath
from os import remove, getcwd, listdir
from celery import Celery
from PIL import Image
from pytesseract import pytesseract
from config import REDIS_HOST, REDIS_PORT

celery = Celery(
    "tasks",
    broker=f"redis://{REDIS_HOST}:{REDIS_PORT}",
    backend=f"redis://{REDIS_HOST}:{REDIS_PORT}",
)


def upload_doc(file: UploadFile, db: Session):
    # temp_path = expanduser("./")
    temp_path = f"/app/Documents/{file.filename}"
    document = Document(path=temp_path)

    try:
        with open(temp_path, "wb") as f:
            f.write(file.file.read())
        db.add(document)
        db.commit()
        db.refresh(document)
    except Exception as exception:
        print(exception)

    return document


def remove_doc(id: int, db: Session):
    document = db.query(Document).filter(Document.id == id).first()

    try:
        remove(document.path)
    except Exception as exception:
        print("No such file: " + str(exception))

    try:
        db.query(Documents_text).filter(Documents_text.id_doc == id).delete()
    except Exception as exception:
        print("No analys was performed on this file" + str(exception))

    try:
        db.query(Document).filter(Document.id == id).delete()
    except Exception as exception:
        print("No data about such file: " + str(exception))

    db.commit()

    return document


def analyse_doc(id: int, db: Session):
    image_path = db.query(Document).filter(Document.id == id).first().path

    try:
        text_result = image_to_text.delay(image_path).get()
        if text_result != 1:
            document_text = Documents_text(id_doc=id, text=text_result)
            db.add(document_text)
            db.commit()
            db.refresh(document_text)
    except Exception as exception:
        print("Analyse doc: " + str(exception))

    return 0


@celery.task
def image_to_text(path):
    text = 1
    try:
        print(f"DIRECTORY: {listdir(getcwd())}")
        image = Image.open(path)
        pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
        text = pytesseract.image_to_string(image)
    except FileNotFoundError as e:
        print(f"ABS: {abspath(getcwd())}")
    
    return text


def get_text(id: int, db: Session):
    return db.query(Documents_text).filter(Documents_text.id_doc == id).first().text
