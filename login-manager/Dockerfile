FROM python:3.7
RUN mkdir -p /webserver
WORKDIR /webserver
COPY ./requirements.txt .
COPY ./login.py .
COPY ./img .
COPY ./login .
COPY ./admin.json .
COPY ./admin-area.json .
COPY ./admin-regione.json .
RUN pip install -r requirements.txt
CMD ["python", "login.py"]