FROM python:3.7-slim


RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

ADD . /code
WORKDIR /code

CMD ["python", "app.py"]