import datetime
import time
import uuid
import pika
import json

#configuration of interval seconds
interval = 5

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

#queue name
queue_name = 'test_queue1'
channel.queue_declare(queue=queue_name)

try:
    while True:

        #Get current timestamp
        current_datetime = datetime.datetime.now()
        timestamp = current_datetime.timestamp()

        data = {
            "message_id": str(uuid.uuid4()),
            "created_on": timestamp
        }

        #convert the dictionary to a JSON string to be sent
        message = json.dumps(data)

        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Sent {message}")
        time.sleep(interval)

except KeyboardInterrupt:
    print("connection is closed by user...")

    #close connection
    connection.close()
