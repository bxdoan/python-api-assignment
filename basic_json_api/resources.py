# -*- coding: utf-8 -*-
# Author: Doan Bui (bxdoan93@gmail.com)
# htttps://github.com/bxdoan/python-api-assignment
from run import db
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jsonpify import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, class_mapper
from datetime import datetime
from dateutil.parser import parse
from models import Users, Customers, serialize

parserU = reqparse.RequestParser()
parserU.add_argument('username', help = 'This field cannot be blank', required = True)
parserU.add_argument('password', help = 'This field cannot be blank', required = True)
parserU.add_argument('dob', help = 'This field cannot be blank')

parserC = reqparse.RequestParser()
parserC.add_argument('name')
parserC.add_argument('dob')
parserC.add_argument('id')

def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class UserRegistration(Resource):
    def post(self):
        try:
            data = parserU.parse_args()
            if data['dob'] == None:
                return {
                    'message': 'dob field cannot be blank'
                }, 400
            age = calculate_age(parse(data['dob']))
            if age < 18:
                return {
                    'message': 'User {} should be greater 18'.format(data['username'])
                }, 400
            new_user = Users(
                username = data['username'],
                password = Users.generate_hash(data['password']),
                dob = data['dob']
            )
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(data['username'])
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = parserU.parse_args()
        current_user = Users.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 400
        if Users.verify_hash(data['password'], current_user.password):
            return {'message': 'Logged in as {}'.format(current_user.username)}
        else:
            return {'message': 'Wrong credentials'}, 400

class CustomersResource(Resource):
    def get(self, id=None):
        try:
            if not id:
                customers = Customers.return_all()
                return jsonify({'customers': customers})
            else:
                customer = Customers.return_id(id)
                return jsonify({'customer': serialize(customer)})
        except:
            return {'message': 'Something went wrong'}, 500

    def post(self):
        data = parserC.parse_args()
        new_customer = Customers(
            name = data['name'],
            dob = data['dob'],
            updated_at = datetime.now()
        )
        try:
            new_customer.save_to_db()
            return {
                'message': 'Customer {} was created'.format(data['name']),
                'customer_id': new_customer.id
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500

    def put(self):
        try:
            data = parserC.parse_args()
            if data['id'] == None:
                return {'message': 'customer_id field cannot be blank'}, 400
            customer = Customers.return_id(data['id'])
            if data['name'] != None:
                customer.name = data['name']
            if data['dob'] != None:
                customer.dob = data['dob']
            customer.updated_at = datetime.now()
            db.session.commit()
            return {'message': 'Customer {} was updated'.format(data['name']),
                    'customer_id': data['id']
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500

    def delete(self):
        data = parserC.parse_args()
        try:
            if data['id'] == None:
                return 400
            Customers.delete_id(data['id'])
            return {'message': 'Customer {} was deleted'.format(data['name']),
                    'customer_id': data['id']
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500
