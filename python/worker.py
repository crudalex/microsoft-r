#!/usr/bin/env python

import time

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")


credentials = pika.PlainCredentials('atwlam', '60004c24')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
