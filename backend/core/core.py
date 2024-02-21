from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify, abort
import requests

from producer import publish
core = Flask(__name__)

CORS(core)

core.config["SQLALCHEMY_DATABASE_URL"]= "mysql://microservice:microservice@db/core"
db=SQLAlchemy(core)

from dataclasses import dataclass
@dataclass
class House(db.Model):
  id:int 
  name: str 
  image: str 
  description: str

  id=db.Column(db.Integer, primary_key=True, autoincrement=False)
  name=db.Column(db.String(150))
  image=  db.Column(db.String(150))
  description= db.Column(db.String(150))

from sqlalchemy import UniqueConstraint

@dataclass
class HouseChecker(db.Model):
 id = db.Column(db.Integer,primary_key= True) 
 checker_id = db.Column(db.Integer)
 house_id = db.Column(db.Integer)

 UniqueConstraint('checker_id','house_id',name="checker_house_unique")



@core.route('/')
def index():
	return '<h1>Hello World!</h1>'

@core.route('/api/houses')
def index():
    return jsonify(House.query.all())

@core.route('/api/houses/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get("http:localhost/api/checker")
    json = req.json()
    publish('house_liked',id)
    
    try:
        houseChecker = HouseChecker(checker_id=json['id'], house_id=id)
        db.session.add(houseChecker)
        db.session.commit()

    except:
        abort(400, 'You have liked this house.')

    return jsonify({
        'message': 'success'
    })
    
    
@core.route('/api/houses/<int:id>/check', methods=['POST'])
def check(id):
    req = requests.get("http:localhost/api/checker")
    json = req.json()
    publish('house_checked',id)
    try:
        houseChecker = HouseChecker(checker_id=json['id'], house_id=id)
        db.session.add(houseChecker)
        db.session.commit()

    except:
        abort(400, 'You have checked this house.')

    return jsonify({
        'message': 'success'
    })
if __name__ == '__main__':
    core.run(host='0.0.0.0', port=5000, debug=True)
