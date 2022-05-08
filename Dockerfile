FROM python:3.9.12-alpine
WORKDIR /server
COPY requirements.txt /server/
RUN pip install -r requirements.txt
COPY . .