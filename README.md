# python-api-assignment

## To start assignment we need some software:

  * Install some softwares and dependencies:
    ```
    pip3 install -r requirements.txt
    ```

  * Install PostgresSQL and run it:
    ```
    apt-get install postgresql
    pg_ctl -D /usr/local/var/postgres start
    ```

  * Please remember create PostgresSQL `username=postgres` and `password=postgres`.

## Customers data model

1. Create table customers using SqlAlchemy, please read [customer_data.py](https://github.com/bxdoan/python-api-assignment/blob/master/customer_data_model/customer_data.py):
    ```
    python /customer_data_model/customer_data.py
    ```
    ![customer_data](img/customer_data.png)

2. A query in PostgresSQL syntax to get names of the youngest customers:
  [youngest_customers.sql](https://github.com/bxdoan/python-api-assignment/blob/master/customer_data_model/youngest_customers.sql) - sql query
  ![youngest_customers](img/youngest_customers.png)
3.  Write a shell script, preferred as .sh bash script as [db-seed.sh](github.com/bxdoan/python-api-assignment/blob/master/customer_data_model/db-seed.sh), that will a) drop the database if exist, b) create the database, c) create the :customers table, d) insert some seeding data. Use command below to see the result:
    ```
    chmod +x customer_data_model/db_seed.sh && ./customer_data_model/db_seed.sh
    ```
    ![db_seed](img/db-seed.png)

## Basic JSON API App
4.  Create RESTful API endpoints returning JSON so that we can make CRUD actions:
    Please see [run.py](github.com/bxdoan/python-api-assignment/blob/master/basic_json_api/run.py) and run command to run the server locally:
    ```
    cd basic_json_api/
    FLASK_APP=run.py FLASK_DEBUG=1 flask run
    ```
    * Read: `method = GET`

      [api.bxdoan.com/customers](http://api.bxdoan.com/customers) - show all customers

      [api.bxdoan.com/customers/id](http://api.bxdoan.com/customers/1) - show **only** 1 customer by **id**
    * Create: `method = POST`

      [api.bxdoan.com/customers](http://api.bxdoan.com/customers) - create customer with pair `name=<name>` and `dob=<datetime>` in json type
    * Update: `method = PUT`

      [api.bxdoan.com/customers](http://api.bxdoan.com/customers) - update **only** 1 customer by **id** `id=<id>` with `name=<name>` or `dob=<datetime>` in json type
    * Delete: `method = DELETE`

      [api.bxdoan.com/delete?id=1](http://api.bxdoan.com/customers) - delete **only** 1 customer by **id** `id=<id>` in json type
5.  Share Postman collection where we can use to make calls to these endpoints.

## Deployment and Auth
6.  Deploy on Google Cloud Platform with domain [api.bxdoan.com](http://api.bxdoan.com/) or IP **35.198.220.248**

7.  The POST endpoint only allow to create user with age greater than 18.

    **Create** with age lower than 18 with receive
    ```
    {'message': 'User should be greater 18'}
    ```
8.  Authentication should be using JWT token.
