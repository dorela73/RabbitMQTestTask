# basic python image
FROM python:3.12.4

# install pika to access rabbitmq
RUN pip install pika

# Prints out
ENV PYTHONUNBUFFERED=1

# declare the source directory
WORKDIR /usr/src/app/producer

# copy the file
COPY  producer.py .

# start command
CMD [ "python", "producer.py" ]