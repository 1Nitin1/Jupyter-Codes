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

### Task:1
- create a table employee and use not null, default, primary key, Date, unique and serial.
- Setting serial curval: select setval('emp_id_seq',2);


## Clauses
1. WHERE
2. IN and NOT IN
3. BETWEEN
4. DISTINCT
5. ORDER BY
6. LIMIT
7. LIKE and ILIKE

## Aggregate Functions
1. MAX
2. MIN
3. COUNT
4. AVG
5. SUM

## OTHER KEYWORD
1. GROUP BY

## STRING FUNCTIONS
1. CONCAT(str1,str2,...)
2. CONCAT_WS('-',str1,str2,...)
3. SUBSTR(str,start,end)
4. REPLACE(str,from,to)
5. LENGTH(str)
6. REVERSE(str)
7. UPPER(str)
8. LOWER(str)
9. LEFT(str, n)
10. RIGHT(str, n)
11. TRIM(str)
12. POSITION(x in y)

## Altering Tables
1. Adding column: alter table tab_name add column ________;
2. Remove column: alter table tab_name drop column col_name;
3. Rename column: alter table tab_name rename column col_name to new_col_name;
4. Rename table: alter table tab_name rename to table_name;
   - OR
   - rename table tab_name to table_name;

## CHECK and CONSTRAINT
1. CHECK is used for making custom checks like mobile no. length >=10.
   - create table xyz(
   - id int,
   - mob varchar(20) unique check (length(mob)>=10)
   - );
2. We can also name it ourselves using CONSTRAINT:
   - create table xyz(
   - id int,
   - mob varchar(20) unique,
   - constraint my_check check (length(mob)>=10)
   - );
3. Adding constraint: alter table tab_name add constraint c_name check _____;
4. Removing constraint: alter table tab_name drop constarint c_name;

## CASE:
1. used like if elif else:
   -  select fname , salary,
   -  case
   -  when salary>=55000 then 'high'
   -  when salary >=50000 then 'mid'
   -  else 'low'
   -  end as sal_cat
   -  from employee;

## FOREIGN KEY
- Syntax:
- foreign key (c_id) reference c_table(c_id);

## JOINS
- CROSS JOIN : select * from tab1_name cross join tab2_name;
- INNER JOIN, LEFT JOIN, RIGHT JOIN: select * from tab1_name a inner join tab2_name b on a.id=b.id;

## VIEWS
- can save a query as a view: create view v_name as --QUERY--

## Having and Rollup
- Having is used with group by.
- Rollup is used to create another total tuple. The null can be overridden using coalesce.

## Stored Routine
1. Stored procedure:
   - CREATE OR REPLACE PROCEDURE pr_name (parameters)
   - LANGUAGE pgplsql
   - AS $$
   - BEGIN
   - - your query...
   - END;
   - $$;
2. Stored function:
   - CREATE OR REPLACE FUNCTION fn_name (parameters)
   - RETURNS return_type AS $$
   - BEGIN
   - - your funtion...
     - RETURN data;
   - END;
   - $$ LANGUAGE pgplsql;

## CTE
- Common Table Expression
- Used to simplify queries
- WITH t_name AS (
- ...QUERY...
- )

## TRIGGER:
- Used to automatically do some action if a particular thing happens.

- CREATE OR REPLACE TRIGGER tri_name
- {BEFORE | AFTER }