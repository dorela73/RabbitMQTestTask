import pika
import json
import os

amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

def callback(str, method, properties, body):
    message = json.loads(body)
    print(f"Received {message}")

connection = pika.BlockingConnection(url_params)

channel = connection.channel()

queue_name = 'test_queue1'
channel.queue_declare(queue=queue_name)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()