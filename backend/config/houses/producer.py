import pika, json 
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

params = pika.URLParameters(os.getenv("AQMP_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='core',body=json.dumps(body))
