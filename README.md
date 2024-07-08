# RabbitMQTestTask
Send and receive message(JSON) between producer and consumer by RabbitMQ

# Installation
1. Install RabbitMQ (Note: If Erlang is not installed, need to install it at first)
2. Install neccessary package by this command: "pip install -r requirements.txt"

# Test project
1. Run cosumer.py and it will print log 'Waiting for messages...'.
2. Run producer.py and it will print log 'Sent {message}' in every 5 seconds.