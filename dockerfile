FROM python:3.9.1

COPY python_code/main.py usr/local/

RUN mkdir usr/local/General
RUN mkdir usr/local/Homer
RUN mkdir usr/local/Lisa

CMD ["python", "main.py"]