FROM python:3.7
RUN mkdir -p /webserver
WORKDIR /webserver
COPY ./requirements.txt /webserver
COPY ./server.py /webserver
COPY ./regioni /webserver

RUN pip install -r requirements.txt
CMD ["python", "server.py"]