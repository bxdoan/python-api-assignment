# python-api-assignment

## To start assignment we need some software:

  * Install pyenv `brew install pyenv`
  * Install Python version 3.6.8 by using  `pyenv install 3.6.8` & `pyenv global 3.6.8 `
  * Install sqlalchemy and dependencies with `pip install sqlalchemy` & `pip install psycopg2-binary`

## Customers data model

1. Create table customers using SqlAlchemy, please read [customer_data.py](https://github.com/bxdoan/python-api-assignment/blob/master/customer_data_model/customer_data.py):
    ```
    python /customer_data_model/customer_data.py
    ```

2. A query in PostgresSQL syntax to get names of the youngest customers:
  [youngest_customers.sql](https://github.com/bxdoan/python-api-assignment/blob/master/customer_data_model/youngest_customers.sql)

3.  Write a shell script, preferred as .sh bash script as [db-seed.sh](github.com/bxdoan/python-api-assignment/blob/master/customer_data_model/db-seed.sh), that will a) drop the database if exist, b) create the database, c) create the :customers table, d) insert some seeding data. Use command below to see the result:
    ```
    chmod +x customer_data_model/db_seed.sh && ./customer_data_model/db_seed.sh
    ```
    ![db seed](img/db-seed.png)
    
## Basic JSON API App
