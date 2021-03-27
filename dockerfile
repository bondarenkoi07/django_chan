FROM python:3.6.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000

