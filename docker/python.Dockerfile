FROM python:3.10.13-alpine3.19

RUN pip install --no-cache pika==1.0.1

ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/app

# CMD ["python", "/var/www/app/send.py"]
ENTRYPOINT [ "python" ]