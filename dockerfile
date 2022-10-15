FROM python:3.9.1

COPY python_code/main.py .

RUN mkdir /General
RUN mkdir /Homer
RUN mkdir /Lisa

CMD ["python", "main.py"]