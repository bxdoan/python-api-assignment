# Author: Doan Bui (bxdoan93@gmail.com)
# htttps://github.com/bxdoan/python-api-assignment

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:postgres@localhost/postgres"

db = create_engine(db_string)
base = declarative_base()

class Customers(base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dob = Column(String)
    updated_at = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
customer = Customers(name="Ronaldo'", dob='1/8/1991', updated_at='2019-08-22 04:05:01')
session.add(customer)
session.commit()

# Read
customers = session.query(Customers)
for customer in customers:
    print(customer.id, customer.name, customer.dob)

# Delete
session.delete(customer)
session.commit()
