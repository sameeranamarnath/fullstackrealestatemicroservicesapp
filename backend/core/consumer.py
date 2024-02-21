import pika,json
from core import House,db
import dotenv 

import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()


params = pika.URLParameters(os.environ.get("AQMP_URL"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='core')

def callback(ch,method,properties,body):
 print("Received in core")
 data = json.loads(body)
 print(data)
 
 if properties.content_type == 'house_created':
  house = House(id=data["id"],name=data["name"],image=data["image"],description=data["description"])
  db.session.add(house)
  db.session.commit()
  print("House created")
 elif properties.content_type == 'house_updated':
  house = House.query.get(data['id'])
  house.name= data['name']
  house.image= data["image"]
  house.description =data["description"]
  db.session.commit()
  print("House updated")
 elif properties.content_type == 'house_deleted':
  house= House.query.get(data['id'])



