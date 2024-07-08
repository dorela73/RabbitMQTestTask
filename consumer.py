import pika
import json

def callback(str, method, properties, body):
    message = json.loads(body)
    print(f"Received {message}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

queue_name = 'test_queue1'
channel.queue_declare(queue=queue_name)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()