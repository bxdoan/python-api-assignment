# -*- coding: utf-8 -*-
# Author: Doan Bui (bxdoan93@gmail.com)
# htttps://github.com/bxdoan/python-api-assignment

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, class_mapper
from json import dumps
from flask_jsonpify import jsonify
from datetime import datetime

app = Flask(__name__)
api = Api(app)

db_connect = create_engine('postgres://postgres:postgres@localhost/postgres')
base = declarative_base()
Session = sessionmaker(db_connect)
session = Session()

def serialize(model):
  """Transforms a model into a dictionary which can be dumped to JSON."""
  columns = [c.key for c in class_mapper(model.__class__).columns]
  return dict((c, getattr(model, c)) for c in columns)

class Customers(base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dob = Column(String)
    updated_at = Column(String)

#read
class Customers_all(Resource):
    def get(self):
        query = session.query(Customers)
        customers = [serialize(label) for label in query]
        result = {'data': customers}
        return jsonify(result)

#read with id
class Customers_id(Resource):
    def get(self, id):
        query = session.query(Customers).filter(Customers.id == id).one()
        customers = serialize(query)
        result = {'data': customers}
        return jsonify(result)

#create
class Create(Resource):
    def post(self):
        customer = Customers(name = request.args.get('name'),
                             dob = request.args.get('dob'),
                             updated_at = datetime.now(tz=None))
        session.add(customer)
        session.commit()
        return 200

#update
class Update(Resource):
    def post(self):
        if request.args.get('id') == None:
            return 400
        customer = session.query(Customers).filter(Customers.id == request.args.get('id')).one()
        if request.args.get('name') != None:
            customer.name = request.args.get('name')
        if request.args.get('dob') != None:
            customer.dob = request.args.get('dob'),
        customer.updated_at = datetime.now(tz=None)
        session.commit()
        return 200

#delete
class Delete(Resource):
    def delete(self):
        customer = session.query(Customers).filter(Customers.id == request.args.get('id')).one()
        session.delete(customer)
        session.commit()
        return 200

api.add_resource(Customers_all, '/', '/customers')
api.add_resource(Customers_id, '/customers/<id>')
api.add_resource(Create, '/create')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')

if __name__ == '__main__':
     app.run(debug=True)
