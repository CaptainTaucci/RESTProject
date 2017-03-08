
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import init_database as i_db

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'BarDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/'

mongo = PyMongo(app)

@app.route('/bars', methods=['GET'])
def get_all_bars():
  bars = mongo.db.bars
  output = []
  for s in bars.find():
    output.append(s)
  return jsonify({'result' : output})

@app.route('/bars/', methods=['GET'])
def get_one_bar(name):
  bars = mongo.db.bars
  s = bars.find_one({'name' : name})
  if s:
    output = s
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/bar', methods=['POST'])
def add_bar():
  bar = mongo.db.bars
  name = request.json['name']
  lon = request.json['lon']
  lat = request.json['lat']
  beerprize = request.json['beerprize']
  jagermaister = request.json['jagermaister']
  openhours = request.json['openhours']
  bar_id = bar.insert_one({"name" : name, "lon":lon, "lat":lat, "beerprize":beerprize, "jagermaister":jagermaister, "openhours":openhours})
  new_bar = bar.find_one({'_id': bar_id })
  return jsonify({'result' : new_bar})

@app.route('/bar/count', methods=['GET'])
def get_count():
    bar = mongo.db.bars
    return bar.count()

@app.route('/bar/update', methods=['POST'])
def update_one():
    bars = mongo.db.bars
    name = request.json['name']
    key = request.json['key']
    val = request.json['val']
    bar_id = bars.update_one({'name':name}, {"$set": {key:val}}, upsert=False)
    new_bar = bars.find_one({'_id': bar_id })
    if(new_bar['key']==val):
        return True
    else:
        return False
       
@app.route('/bar/delete', methods=['GET'])
def get_count(name):
    bars = mongo.db.bars
    bars.delete_one({"name":name})
    if("No such" not in get_one_bar(name)):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)