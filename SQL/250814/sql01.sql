USE sakila;

SHOW TABLES;

SELECT
	P.customer_id, P.amount, P.payment_date
FROM payment P
WHERE P.amount > (
	SELECT AVG(amount)
    FROM payment
    WHERE customer_id = P.customer_id
);


# 중고급 서브쿼리 시작!!!

SELECT
	first_name,
    last_name
FROM customer
WHERE customer_id IN (
	SELECT customer_id
    FROM payment
    WHERE amount > (SELECT AVG(amount) FROM payment)
);

SELECT
	first_name,
    last_name
FROM customer
WHERE customer_id IN (
	SELECT customer_id
    FROM payment
    WHERE amount > 3
);


SELECT
	first_name,
    last_name
FROM customer
WHERE customer_id IN (
	SELECT customer_id
    FROM payment
    GROUP BY customer_id
    HAVING COUNT(*) > (
		SELECT
			AVG(payment_count)
        FROM (
			SELECT COUNT(*) AS payment_count
            FROM payment
            GROUP BY customer_id
        ) AS payment_counts
    )
);


SELECT
	first_name,
    last_name
FROM customer
WHERE customer_id = (
	SELECT customer_id
    FROM (
		SELECT customer_id, COUNT(*) AS payment_count
        FROM payment
        GROUP BY customer_id
    ) AS payment_counts
    ORDER BY payment_count DESC
    LIMIT 1
);

# 상관 서브쿼리

SELECT
	P.customer_id,
    P.amount,
    P.payment_date
FROM payment P
WHERE P.amount > (
	SELECT
		AVG(amount)
    FROM payment
    WHERE customer_id = P.customer_id
);

# film 테이블에서 평균 영화길이(length)보다 긴 영화들의
# 제목을 찾아주세요!!! -> 서브쿼리를 통해서 문제 해결!!!

SELECT title FROM film
WHERE length > (SELECT AVG(length) FROM film);

# rental 테이블에서 고객별 평균 대여 횟수보다 많은 대여를 한
# 고객들의 이름(first, last)을 찾아주세요.


SHOW TABLES;

SELECT
	*
FROM customer
LIMIT 5;

SELECT
	*
FROM rental
LIMIT 5;

SELECT
	first_name, last_name
FROM customer
WHERE customer_id IN (
	SELECT customer_id
    FROM rental
    GROUP BY customer_id
    HAVING COUNT(*) > (
		SELECT AVG(rental_count)
		FROM (
			SELECT COUNT(*) AS rental_count 
			FROM rental
			GROUP BY customer_id
		) AS rental_counts
    )
);

# 가장 많은 영화를 대여한 고객의 이름(first, last)을 찾아주세요!
SELECT
	first_name,
    last_name
FROM customer
WHERE customer_id = (
	SELECT customer_id
    FROM (
		SELECT customer_id, COUNT(*) AS rental_count
		FROM rental
		GROUP BY customer_id
    ) AS rental_counts
    ORDER BY rental_count DESC
    LIMIT 1
);

# 각 고객에 대해 자신이 대여한 평균 영화 길이보다 긴 영화들들의 제목을
# 찾아주세요!!!

SELECT
	*
FROM film
LIMIT 3; # film_id

SELECT
	*
FROM customer
LIMIT 3; # customer_id

SELECT
	*
FROM rental
LIMIT 3; # customer_id & inventory_id

SELECT
	*
FROM inventory
LIMIT 3; # inventory_id & film_id

SELECT
	C.first_name, C.last_name, F.title
FROM customer C
JOIN rental R ON R.customer_id = C.customer_id
JOIN inventory I ON I.inventory_id = R.inventory_id
JOIN film F ON F.film_id = I.film_id
WHERE F.length > (
	SELECT AVG(FIL.length)
    FROM film FIL
    JOIN inventory INV ON INV.film_id = FIL.film_id
    JOIN rental REN ON REN.inventory_id = INV.inventory_id
    WHERE REN.customer_id = C.customer_id
);






