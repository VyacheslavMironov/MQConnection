#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('mq_brooks', 'mq_brooks_22')
parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(f"[x] Sent 'Hello World!'")
    connection.close()

except pika.exceptions.AMQPError as error:
    print("Произошла ошибка при установлении соединения с RabbitMQ:", str(error))