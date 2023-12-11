#!/usr/bin/env python
import time
import pika

credentials = pika.PlainCredentials('mq_brooks', 'mq_brooks_22')
parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    # Проверка и отправка сообщения
    channel.queue_declare(queue='task_queue', durable=True)
    print('[*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] Received  {body}")
        time.sleep(len(body))
        print('[x] Done')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback)
    channel.start_consuming()
except pika.exceptions.AMQPError as error:
    print("Произошла ошибка при установлении соединения с RabbitMQ:", str(error))
