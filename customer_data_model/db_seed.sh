#!/bin/bash
psqluser="postgres"   # Database username
psqlpass="postgres"   # Database password
psqldb="postgres"     # Database name

if psql -lqt | cut -d \| -f 1 | grep -qw $psqluser; then
    # database exists
    echo "The database postgres exist. Droped it!"
    dropdb $psqldb
fi

# Create database postgres
echo "Create database postgres"
createdb $psqldb

# create the customers table
echo "Create the customers table"
psql -d $psqldb -U $psqluser -c "DROP TABLE IF EXISTS customers;
                                  CREATE TABLE customers(id serial PRIMARY KEY,
                                           name text,
                                           dob date,
                                           updated_at timestamp);"

# insert some seeding data
echo "insert some seeding data"
psql -d $psqldb -c "INSERT INTO customers VALUES
    (1, 'Ronaldo', '1/8/1991', '2019-08-22 04:05:01'),
		(2, 'Messi', '3/4/1992', '2019-08-22 04:05:02'),
		(3, 'Modric', '3/28/1993', '2019-08-22 04:05:03'),
		(4, 'Salah', '4/25/1994', '2019-08-22 04:05:04'),
		(5, 'Pogba', '1/8/1995', '2019-08-22 04:05:05'),
		(6, 'Kante', '1/22/1996', '2019-08-22 04:05:06'),
		(7, 'Neymar', '1/23/1997', '2019-08-22 04:05:07'),
		(8, 'Mbappe', '1/13/1998', '2019-08-22 04:05:08'),
		(9, 'Kroos', '1/11/1999', '2019-08-22 04:05:09'),
		(10, 'Oezil', '1/10/1990', '2019-08-22 04:05:010');"

# show customers table
psql -d $psqldb -c "SELECT * FROM customers;"
