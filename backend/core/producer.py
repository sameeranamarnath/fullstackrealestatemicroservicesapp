import pika, json,os
import dotenv


dotenv.load_dotenv()
params = pika.URLParameters(os.environ.get('AQMP_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='config', body=json.dumps(body), properties=properties)