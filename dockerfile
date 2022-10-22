FROM python:3.9.12

COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/

RUN mkdir /app/General
RUN mkdir /app/Personajes

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]