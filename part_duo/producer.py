import pika
import json
import random
from faker import Faker

from models import Contact
import connect


fake = Faker()

# Підключення до RabbitMQ

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='contacts_queue')

# Генерація фейкових контактів та запис до бази даних та черги
for _ in range(10):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email()
    )
    contact.save()

    message = {
        'contact_id': str(contact.id)
    }

    channel.basic_publish(exchange='', routing_key='contacts_queue', body=json.dumps(message))

    print(f" [x] Sent {message}")

connection.close()
