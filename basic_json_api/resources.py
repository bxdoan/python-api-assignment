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

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        new_user = Users(
            username = data['username'],
            password = data['password']
        )
        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format( data['username'])
            }
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = Users.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}, 400

        if data['password'] == current_user.password:
            return {'message': 'Logged in as {}'.format(current_user.username)}
        else:
            return {'message': 'Wrong credentials'}, 400

class AllCustomers(Resource):
    def get(self):
        try:
            customers = Customers.return_all()
            return jsonify({'customers': customers})
        except:
            return {'message': 'Something went wrong'}, 500

    def post(self):
        try:
            customer = Customers.return_id(request.args.get('id'))
            return jsonify({'customers': serialize(customer)})
        except:
            return {'message': 'Something went wrong'}, 500

    def delete(self):
        try:
            Customers.delete_id(request.args.get('id'))
            return {'message': 'OK'}
        except:
            return {'message': 'Something went wrong'}, 500

class CreateCustomers(Resource):
    def post(self):
        new_customer = Customers(
            name = request.args.get('name'),
            dob = request.args.get('dob'),
            updated_at = datetime.now()
        )
        try:
            new_customer.save_to_db()
            return {
                'message': 'Customer {} was created'.format( new_customer.name)
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500

class UpdateCustomers(Resource):
    def post(self):
        if request.args.get('id') == None:
            return 400
        customer = Customers.return_id(request.args.get('id'))
        if request.args.get('name') != None:
            customer.name = request.args.get('name')
        if request.args.get('dob') != None:
            age = calculate_age(parse(request.args.get('dob')))
            if age < 18:
                return {'message': 'Customer should be greater 18'}, 400
            customer.dob = request.args.get('dob'),
        customer.updated_at = datetime.now()
        db.session.commit()
        return {'message': 'OK'}, 200
