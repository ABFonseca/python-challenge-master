FROM python:3

COPY . /app
WORKDIR /app


RUN pip install flask


ENTRYPOINT ["python", "main.py"]




