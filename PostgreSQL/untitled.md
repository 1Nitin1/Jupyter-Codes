# DATABASE USING POSTGRESQL

## CLI METHODS
1. \list - for getting the list of databases
2. \q - to quit
3. \password postgres - to change the password
4. \! cls - to clear

## QUERIES
1. SeLECT datname from pg_database; : for gettinng all databases.
2. CREATE DATABASE Abcd; : for creating a new database.
3. \c Abcd; : for changing database.
4. DROP DATABASE Abcd; : for deleting a database.

## CRUD
1. Creating table:
   -  Create table Person(id int, name varchar(10), city varchar(20));
2. To display the data inside a DB or Table:
   - \d or for table specific, \d table_name;
3. To insert tuples:
   -  INSERT INTO person(id,name,city) Values (101,'Nitin','Delhi'),(102,'Manya','U.P.');
4. Reading data:
   - SELECT * FROM Person;
5. Updating data:
   - UPDATE table_name SET col_name='xyz' WHERE col_name='abc';
6. Deleting a tuple:
   -  DELETE FROM Person WHERE id=101;

## Datatypes
- INT
- BIGINT
- FLOAT
- DOUBLE
- NUMERIC
- VARCHAR
- DECIMAL(precision)
- DECIMAL(precision,dec_limit)
- SERIAL : for auto_increment
- etc

## Constraints
1. Primary key
2. Not NULL
3. LIKE
4. ILIKE
5. DEFAULT