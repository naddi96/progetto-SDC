FROM python:3.7
RUN mkdir -p /webserver
WORKDIR /webserver
COPY ./requirements.txt .
COPY ./server.py .
COPY ./regioni ./regioni

RUN pip install -r requirements.txt
CMD ["python", "server.py"]