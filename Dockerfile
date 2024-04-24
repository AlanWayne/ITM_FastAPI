FROM python:3.9-slim

# RUN mkdir -p /app/Documents

WORKDIR /app

COPY requirements.txt .

RUN apt-get update

RUN apt-get install -y tesseract-ocr

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
