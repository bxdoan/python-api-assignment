# python-api-assignment

To start assignment we need some software:

  * Install pyenv `brew install pyenv`
  * Install Python version 3.6.8 by using  `pyenv install 3.6.8` & `pyenv global 3.6.8 `
  * Install sqlalchemy and dependencies with `pip install sqlalchemy` & `pip install psycopg2-binary`

Customers data model

1. create table customers using SqlAlchemy:
    `python /customer_data_model/customer_data.py`

2. Write a query in PostgresSQL syntax to get names of the youngest customers:
    see /customer_data_model/youngest_customers.sql
