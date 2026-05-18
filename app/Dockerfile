FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY ml_model.py .
COPY templates/ templates/
COPY data.json .

EXPOSE 5000

CMD ["python", "app.py"]
