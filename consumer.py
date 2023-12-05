import os
import django
import pika
import json


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskynotification.settings")

# Configure Django settings
django.setup()

# from user.models import Product
from notifications.models import Notification

params = pika.URLParameters('amqps://tamelmkg:bAGQhUGeH658A5vM9E5wFA6wzQNaAkPc@puffin.rmq2.cloudamqp.com/tamelmkg')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='notification', durable=True)

def callback(ch, method, properties, body):
    try:
        print("Received in main")
        data = json.loads(body)
        
        print(data)
        print(type(data))

        if properties.content_type == 'application/json':
            Notification.objects.create(content = data['content'], type='Registration', workspace = data['workspace'])
            print('Done')
    except Exception as e:
        print(f"Error processing message: {e}")
    finally:
        # Acknowledge the message after processing
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
   

channel.basic_consume(queue='notification', on_message_callback=callback, auto_ack=False)

print('Started consuming')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C) gracefully
    pass
finally:
    connection.close()
