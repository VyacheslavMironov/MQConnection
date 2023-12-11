#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('mq_brooks', 'mq_brooks_22')
parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    # Проверка и отправка сообщения
    channel.queue_declare(queue='hello')
    print('[*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] Received  {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
except pika.exceptions.AMQPError as error:
    print("Произошла ошибка при установлении соединения с RabbitMQ:", str(error))
