FROM python:3.11

WORKDIR /app/

COPY ./requirements.txt /app/
COPY ./.env.dev /app/
RUN pip install --no-cache-dir -r requirements.txt

