import os, django, pika, json, time      
from dotenv import load_dotenv
load_dotenv()

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskynotification.settings")

# Configure Django settings
django.setup()

from notifications.models import Notification

connection_params = pika.ConnectionParameters(
    host='docker-taskyflow-microservice-rabbitmq-container-1',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials(username='taskyapp', password='1345'),
    heartbeat=600,
)

def establish_connection():
    while True:
        try:
            connection = pika.BlockingConnection(connection_params)
            return connection
        except pika.exceptions.AMQPConnectionError:
            time.sleep(5)

connection = establish_connection()
channel = connection.channel()

# Declare the first queue
channel.queue_declare(queue='notification', durable=True)

# # Declare the second queue
channel.queue_declare(queue='task', durable=True)

def callback(ch, method, properties, body):
    try:
        queue_name = method.routing_key
        data = json.loads(body)
        
        if properties.content_type == 'application/json':
            common_parameter = dict(
                content=data['content'],
                type=data['type'],
                workspace=data['workspace'],
            )
        
            if 'category' in data and data['category'] == 'personal':
                common_parameter['category'] = data['category']
            if 'userMail' in data:
                common_parameter['userMail'] = data['userMail']
            try:
                notification = Notification.objects.create(**common_parameter)
                notification.category_set()
            except Exception as e:
                print(f'Error: {e}')
                
    except Exception as e:
        print(f"Error processing message: {e}")
    finally:
        # Acknowledge the message after processing
        ch.basic_ack(delivery_tag=method.delivery_tag)

# Set up the callback for the first queue
channel.basic_consume(queue='notification', on_message_callback=callback, auto_ack=False)

# # Set up the callback for the second queue
channel.basic_consume(queue='task', on_message_callback=callback, auto_ack=False)

print('Started consuming')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
finally:
    connection.close()


