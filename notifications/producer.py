# import pika, json

# params = pika.URLParameters('amqps://tamelmkg:bAGQhUGeH658A5vM9E5wFA6wzQNaAkPc@puffin.rmq2.cloudamqp.com/tamelmkg')
# try:
#     connection = pika.BlockingConnection(params)
#     channel = connection.channel()
#     channel.queue_declare(queue='admin')
# except pika.exceptions.AMQPConnectionError as connection_error:
#     print(f"AMQP Connection Error: {connection_error}")

# def publish(method, body):
    
#     try:
#         properties = pika.BasicProperties(method)
#         channel.basic_publish(
#         exchange='',
#         routing_key='main',
#         body=json.dumps(body),
       
#         properties=properties   # Make the message persistent
        
#     )
#     except pika.exceptions.AMQPChannelError as channel_error:
#         print(f"AMQP Channel Error: {channel_error}")
    
