USE sakila;

CREATE VIEW ActorInfo AS
SELECT first_name, last_name
FROM actor
WHERE actor_id < 100;

SELECT * FROM ActorInfo;

CREATE OR REPLACE VIEW ActorInfo AS
SELECT first_name, last_name
FROM actor
WHERE actor_id < 100;

DROP VIEW ActorInfo;

CREATE OR REPLACE VIEW myview AS
SELECT * FROM customer
WHERE customer_id = 1;

SELECT * FROM myview;

UPDATE customer
SET first_name = 'DAVE'
WHERE customer_id = 1;

SELECT * FROM customer;
SELECT * FROM myview;

UPDATE myview
SET first_name = 'HAPPY'
WHERE customer_id = 1;

SELECT * FROM myview;

SELECT * FROM customer;