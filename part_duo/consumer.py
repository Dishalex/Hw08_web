import pika
import json
import time

from models import Contact
import connect

# Підключення до RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='contacts_queue')


# Функція для імітації надсилання email
def send_email(contact):
    print(f"Simulating sending email to {contact.email}")
    time.sleep(2)
    print(f"Email sent to Contact {contact.id}")
    contact.is_message_sent = True
    contact.save()


# Функція-колбек для обробки повідомлень з черги
def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.is_message_sent:
        send_email(contact)

# обробник для черги
channel.basic_consume(queue='contacts_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press Ctrl+C')
channel.start_consuming()
