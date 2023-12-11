#!/usr/bin/env python
import sys
import pika

credentials = pika.PlainCredentials('mq_brooks', 'mq_brooks_22')
parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))
    print(f"[x] Sent {message}")

except pika.exceptions.AMQPError as error:
    print("Произошла ошибка при установлении соединения с RabbitMQ:", str(error))
