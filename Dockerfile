FROM python:3.11-slim

WORKDIR /app

ENV TZ=Asia/Kolkata

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/app.py
COPY model.pkl /app/model.pkl
EXPOSE 7860

CMD ["python", "app.py"]