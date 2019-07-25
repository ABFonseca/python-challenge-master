FROM python:3

COPY . /app
WORKDIR /app
EXPOSE 8085

RUN pip install flask


ENTRYPOINT ["python", "main.py"]




