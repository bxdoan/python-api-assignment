# Author: Doan Bui (bxdoan93@gmail.com)
# htttps://github.com/bxdoan/python-api-assignment
from run import db
from flask_jsonpify import jsonify
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from json import dumps
import datetime

base = declarative_base()

def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)

class Users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement=True)
    username = Column(String(120), unique = True, nullable = False)
    password = Column(String(120), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return db.session.query(Users).filter_by(username = username).first()

class Customers(base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dob = Column(String)
    updated_at = Column(String)

    def return_all():
        customers = [serialize(o) for o in db.session.query(Customers)]
        return customers

    def return_id(cls):
        customer = db.session.query(Customers).filter(Customers.id == cls).one()
        return customer

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_id(cls):
        customer = db.session.query(Customers).filter(Customers.id == cls).one()
        db.session.delete(customer)
        db.session.commit()
