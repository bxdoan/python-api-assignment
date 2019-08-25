# Author: Doan Bui (bxdoan93@gmail.com)
# htttps://github.com/bxdoan/python-api-assignment
from app import db
from flask_jsonpify import jsonify
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from passlib.hash import pbkdf2_sha256 as sha256
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
    dob = Column(String)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return db.session.query(Users).filter_by(username = username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

class Customers(base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dob = Column(String)
    updated_at = Column(String)

    def return_all():
        customers = [serialize(o) for o in db.session.query(Customers)]
        return customers

    def return_one(cls):
        customer = db.session.query(Customers).filter(Customers.id == cls).one()
        return customer

    def add(self):
        db.session.add(self)
        db.session.commit()

    def commit():
        db.session.commit()

    def delete(cls):
        customer = db.session.query(Customers).filter(Customers.id == cls).one()
        db.session.delete(customer)
        db.session.commit()

class RevokedTokenModel(base):
    __tablename__ = 'revoked_tokens'
    id = Column(Integer, primary_key = True, autoincrement=True)
    jti = Column(String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = db.session.query(RevokedTokenModel).filter(RevokedTokenModel.jti == jti).first()
        return bool(query)
