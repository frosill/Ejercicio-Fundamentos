FROM python:3.9.12

COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/

RUN mkdir /app/General
RUN touch /app/General/general.csv
RUN mkdir /app/Homer
RUN touch /app/Homer/homer.csv
RUN mkdir /app/Lisa
RUN touch /app/Lisa/lisa.csv
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]