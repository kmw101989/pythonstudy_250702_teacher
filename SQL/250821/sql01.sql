# 1. category 테이블에서 Comedy, Sports, Family 카테고리의
# category_id와 카테고리명을 출력해주세요.

SELECT
	category_id,
    name
FROM category
WHERE
	name = "Comedy" OR
    name = "Sports" OR
    name = "Family";
    
SELECT
	category_id, name
FROM category
WHERE
	name IN("Comedy", "Sports", "Family");
    
    
# 문제2. film_category 테이블에서 카테고리 ID별 영화 갯수 확인 및 출력
SELECT
	category_id, COUNT(*)
FROM film_category
GROUP BY category_id;

# 문제3. 카테고리가 Comedy인 영화 갯수 확인 및 출력 (*JOIN으로 작성해주세요)

SELECT
	COUNT(*)
FROM category C
JOIN film_category F USING(category_id)
WHERE C.name = "Comedy";

# 문제4. 카테고리가 Comedy인 영화 갯수 확인 및 출력 (*Subquery으로 작성해주세요)

SELECT COUNT(*) FROM film_category
WHERE category_id IN (
	SELECT category_id FROM category
    WHERE name = "Comedy"
);

# 문제5. Comedy, Sports, Family 각각의 카테고리별 영화 수 확인하기 (JOIN사용)

SELECT
	C.name, COUNT(*)
FROM category C
JOIN film_category USING(category_id)
WHERE C.name IN ("Comedy", "Sports", "Family")
GROUP BY C.category_id;

# 문제6. 각 카테고리를 기준으로 영화 수가 70이상인 카테고리명을 출력해주세요.

SELECT
	C.name, COUNT(*) AS category_count
FROM category C
JOIN film_category F USING(category_id)
GROUP BY C.category_id
HAVING COUNT(*) >= 70 ;

# 문제 7. 각 카테고리에 포함된 영화들의 렌탈 횟수 구하기

# 렌탈횟수 -> 현재 우리가 가지고 있는 DVD 전체 총 아이템을 기준으로
# 각 아이템들이 몇 번씩 렌탈이 되었는가?

# 렌탈정보 : rental -> inventory_id
# inventory -> inventory_id, film_id
# film_category -> category_id, film_id
# category -> category_id

SELECT
	C.name, COUNT(*)
FROM category C
JOIN film_category USING(category_id)
JOIN inventory USING(film_id)
JOIN rental USING(inventory_id)
GROUP BY C.category_id;

# 문제 8. Comedy, Sports, Family 카테고리에 포함되는 영화들의 렌탈 횟수 구하기

SELECT
	C.name, COUNT(*)
FROM category C
JOIN film_category USING(category_id)
JOIN inventory USING(film_id)
JOIN rental USING(inventory_id)
WHERE C.name IN ("Comedy", "Sports", "Family")
GROUP BY C.category_id;

SELECT
	C.name, COUNT(*)
FROM category C
JOIN film_category USING(category_id)
JOIN inventory USING(film_id)
JOIN rental USING(inventory_id)
WHERE C.name IN ("Comedy")
GROUP BY C.category_id;

# 문제 9. 카테고리가 Comedy인 데이터의 렌탈 횟수 출력 (*서브쿼리 문법으로 작성)

SELECT
	COUNT(*)
FROM rental
WHERE inventory_id IN (
	SELECT inventory_id FROM inventory WHERE film_id IN (
		SELECT film_id FROM film_category WHERE category_id IN (
			SELECT category_id FROM category
            WHERE name = "Comedy"
        )
    )
);

SELECT
  /* 카테고리명도 서브쿼리로 가져오기 */
  (SELECT c.name
   FROM category c
   WHERE c.name = 'Comedy') AS category_name,
  /* 해당 카테고리의 대여 건수 */
  (SELECT COUNT(*)
   FROM rental r
   WHERE r.inventory_id IN (
     SELECT i.inventory_id
     FROM inventory i
     WHERE i.film_id IN (
       SELECT fc.film_id
       FROM film_category fc
       WHERE fc.category_id IN (
         SELECT c2.category_id
         FROM category c2
         WHERE c2.name = 'Comedy'
       )
     )
   )) AS rental_count;

# 문제10. address 테이블에는 address_id가 있지만, customer 테이블에는
# 없는 데이터의 갯수 출력!!!! (*INNER JOIN // RIGHT JOIN)

SELECT * FROM address; # 603
SELECT * FROM customer; # 599

SELECT
	COUNT(A.address_id)
FROM address A
JOIN customer C USING(address_id);

SELECT
	(SELECT COUNT(*) FROM address) -
	(SELECT
		COUNT(A.address_id)
	FROM address A
	JOIN customer C USING(address_id))
    AS no_customer_address;

# 1 + 2 = 3

SELECT COUNT(*) no_customer_address
FROM customer C
RIGHT JOIN address A
ON A.address_id = C.address_id
WHERE customer_id IS NULL;

# 문제 11. 캐나다 고객에게 이메일 마케팅 캠페인을 진행하고자 합니다.
# 캐나다 고객의 이름과 이메일 주소 리스트를 출력해주세요. 

# customer => address_id
# address => address_id & city_id
# city => city_id & country_id
# country => country_id

SELECT
	first_name, last_name, email
FROM customer CU
JOIN address AD USING(address_id)
JOIN city CI USING(city_id)
JOIN country CO USING(country_id)
WHERE CO.country = "Canada";

# 문제 12. 신혼부부 타겟고객들의 매출이 최근 저조해져서 가족영화를 홍보대상으로
# 삼고자 합니다. 가족 영화로 분류된 모든 영화 리스트(*영화제목)를 출력해주세요.

SELECT F.title
FROM film F
JOIN film_category FC USING(film_id)
JOIN category CA USING(category_id)
WHERE CA.name = "Family";

# 문제 13. 가장 자주 대여하는 영화 리스트를 참고로 보고 싶습니다.
# 가장 자주 대여하는 영화 순으로 100개만 뽑아주세요.
# 뽑아달라는 것의 의미는 "영화제목"과 "렌탈횟수"

# film -> title // film_id
# inventory -> film_id & inventory_id
# rental -> inventory_id

SELECT F.title, COUNT(*) AS Rentals
FROM film F
JOIN inventory I USING(film_id)
JOIN rental R USING(inventory_id)
GROUP BY F.film_id
ORDER BY Rentals DESC
LIMIT 100;

# 문제 14. 각 스토어별로 매출을 확인하고 싶습니다. 관련 데이터를 출력해주세요.
# 관련 데이터는 다음과 같습니다.
# "도시, 국가" // 스토어ID // 스토어별 총 매출

# payment -> amount // staff_id
# staff -> staff_id & store_id
# store -> store_id & address_id
# address -> address_id & city_id
# city -> city_id & country_id
# country -> country_id // Countrty

SELECT
	CONCAT(CI.city, ", ", CO.country) AS Store,
    STO.store_id AS Store_ID,
	SUM(P.amount) AS Total_Sales
FROM payment P
JOIN staff STA ON STA.staff_id = P.staff_id
JOIN store STO ON STO.store_id = STA.store_id
JOIN address A ON A.address_id = STO.address_id
JOIN city CI ON CI.city_id = A.city_id
JOIN country CO ON CO.country_id = CI.country_id
GROUP BY STO.store_id;

# 문제 15. 가장 렌탈비용을 많이 지불한 상위 10명의 VIP 고객에게 선물을 배송하고자
# 합니다. 해당 VIP 고객들의 이름과 주소, 이메일, 그리고 각 고객별 그동안 총 지불
# 비용을 출력해주세요.

SELECT
	C.first_name, C.last_name,
    A.address, C.email,
	SUM(P.amount) AS total_amount
FROM payment P
JOIN customer C USING(customer_id)
JOIN address A USING(address_id)
GROUP BY P.customer_id
ORDER BY total_amount DESC
LIMIT 10;

# 문제 16. actor 테이블의 배우 이름을 first_name과 last_name의 조합으로
# 출력해주세요. 단, 소문자로 출력해주세요. Actor_Name이라는 필드명으로 출력!!!

SELECT
	LOWER(CONCAT(first_name, " ", last_name)) Actor_Name
FROM actor;

SELECT
	CONCAT(
		UPPER(LEFT(first_name, 1)),
        LOWER(SUBSTRING(first_name, 2)),
        " ",
        UPPER(LEFT(last_name, 1)),
        LOWER(SUBSTRING(last_name, 2))
        ) AS Actor_Name
FROM actor;

# 문제 17. 언어가 영어인 영화 중 영화 타이틀이 K와 Q로 시작하는 영화의 타이틀만 출력!!!
# 서브쿼리로 가져오세요!!!

SELECT
	title
FROM film
WHERE language_id IN (
	SELECT language_id FROM language
    WHERE name = "English"
) AND (title LIKE "K%" OR title LIKE "Q%");

# 문제 18. Alone Trip에 나오는 배우 이름을 모두 출력하세요. -> 하나의 문장으로 출력!!!
# 단, 배우이름은 actor_name 이라는 필드명으로 출력해주세요.
# 서브쿼리를 사용해주세요.

SELECT
	CONCAT(first_name, " ", last_name) actor_name
FROM actor
WHERE actor_id IN (
	SELECT actor_id FROM film_actor WHERE film_id IN (
		SELECT film_id FROM film WHERE title = "Alone Trip"
    )
);

# 문제 19. 2005년 8월에 각 스태프 멤버가 올린 매출을 출력해주세요.
# 스태프 멤버 필드명은 Staff_Member로,
# 매출 필드명은 Total_Amount로 출력해주세요!

SELECT
	CONCAT(S.first_name, " ", last_name) Staff_Member,
    SUM(P.amount) Total_Amount
FROM staff S
JOIN payment P USING(staff_id)
WHERE payment_date LIKE "2005-08%"
GROUP BY P.staff_id;

SELECT
	CONCAT(S.first_name, " ", last_name) Staff_Member,
    SUM(P.amount) Total_Amount
FROM staff S
JOIN payment P USING(staff_id)
WHERE
	EXTRACT(YEAR FROM payment_date) = 2005 AND
    EXTRACT(MONTH FROM payment_date) = 8
GROUP BY P.staff_id;

SELECT
	CONCAT(S.first_name, " ", last_name) Staff_Member,
    SUM(P.amount) Total_Amount
FROM staff S
JOIN payment P USING(staff_id)
WHERE
	YEAR(payment_date) = 2005 AND
    MONTH(payment_date) = 8
GROUP BY P.staff_id;

# 문제 20. 각 카테고리의 평균 영화 러닝타임이 전체 평균 러닝타임보다 큰
# 카테고리들의 카테고리명과 해당 카테고리의 평균 러닝 타임을 출력하세요.

SELECT
	C.name,
	AVG(F.length) film_length
FROM film F
JOIN film_category FC USING(film_id)
JOIN category C USING(category_id)
GROUP BY C.name
HAVING AVG(F.length) > (
	SELECT AVG(length) FROM film
);

# 문제 21. 각 카테고리별 평균 영화 대여 시간과 해당 카테고리명을 출력하세요.
# 영화 대여 시간 => 영화 대여 및 반납 시간의 차이, hour를 단위로 사용하세요!

# 대여시간 : rental => inventory_id
# inventory : inventory_id & film_id
# film_category : film_id & category_id
# category : category_id

SELECT
	C.name,
    AVG(TIMESTAMPDIFF(HOUR, R.rental_date, R.return_date)) AS diff_time
FROM rental R
JOIN inventory I USING(inventory_id)
JOIN film_category F USING(film_id)
JOIN category C USING(category_id)
GROUP BY C.name;

# 문제 22. 새로운 임원이 부임했습니다.
# 총 매출액 상위 5개 장르(*카테고리)의 매출액을 수시로 확인하고자 합니다.
# 각 장르별 총 매출액(Total Sales), 각 장르 이름(Genre)으로 해당 데이터를 수시로
# 확인 할 수 있는 "VIEW"를 생성해주세요.
# VIEW의 이름은 top5_genres로 만들어주시고, 총 매출액 상위 5개 장르의 매출액이
# 출력될 수 있도록 해주세요.


CREATE OR REPLACE VIEW top5_genres AS
	SELECT
		C.name AS Genre,
		SUM(P.amount) AS Total_Sales
	FROM payment P # rental_id
    JOIN rental R USING(rental_id) # inventory_id
    JOIN inventory I USING(inventory_id) # film_id
    JOIN film_category F USING(film_id) # category_id
    JOIN category C USING(category_id)
    GROUP BY C.name
    ORDER BY SUM(P.amount) DESC
    LIMIT 5;

DROP VIEW top5_genres;

# 문제 23. 2005년 5월에 가장 많이 대여된 영화 3개를 찾아주세요. 영화제목과 대여횟수를 출력하면 됩니다!

SELECT
	F.title,
	COUNT(*) AS rental_count
FROM rental R
JOIN inventory I USING(inventory_id)
JOIN film F USING(film_id)
WHERE
	MONTH(R.rental_date) = 5 AND
    YEAR(R.rental_date) = 2005
GROUP BY F.film_id
ORDER BY rental_count DESC
LIMIT 3;

# 문제 24. 대여된 적이 없는 영화를 찾으세요.

# rental => inventory_id
# inventory => inventory_id & film_id
# film => film_id

SELECT
	title
FROM film
WHERE film_id NOT IN (
	SELECT film_id FROM inventory I
    JOIN rental R USING(inventory_id)
);

# 문제 25. 각 고객의 총 지출 금액의 평균 보다 총 지출 금액이 더 큰 고객 리스트를
# 찾으세요. 그들의 이름과 그들이 지출한 총 금액을 보여주세요.

# 고객 A 5번 렌트, 총 100달러
# 고객 B 3번 렌트, 총 80달러
# 고객당 평균 지출금액 90달러

SELECT
	C.first_name, C.last_name,
    SUM(P.amount)
FROM payment P
JOIN customer C USING(customer_id)
GROUP BY C.customer_id
HAVING SUM(P.amount) > (
	SELECT
		AVG(sum_amount)
	FROM (
		SELECT SUM(amount) AS sum_amount
		FROM payment
		GROUP BY customer_id
	) AS sub_query
);

# 문제 26. 가장 많은 결제건을 처리한 직원이 누구인지 찾아주세요.

SELECT
	S.staff_id, S.first_name, S.last_name,
    COUNT(*) AS count_many
FROM staff S
JOIN payment P USING(staff_id)
GROUP BY S.staff_id
ORDER BY COUNT(*) DESC
LIMIT 1;

# 문제 27. "액션" 카테고리에서 높은 영화 영상 등급을 받은 순으로, 상위 5개의의 영화를
# 보여주세요. (*높은 영화 영상 등급 순으로의 정렬은 ORDER BY rating DESC 을 기준으로 하세요!)


SELECT
	F.title, F.rating
FROM film F
JOIN film_category FC USING(film_id)
JOIN category C USING(category_id)
WHERE C.name = "Action"
ORDER BY rating DESC
LIMIT 5;

SELECT
	DISTINCT rating
FROM film;

DESC film;

# 문제 28. 각 영화 영상등급을 기준으로 영화별 대여기간의 평균을 찾아주세요.

SELECT rating, AVG(rental_duration)
FROM film
GROUP BY rating;

# 문제 29. 매장 ID별 총 매출을 보여주는 VIEW를 생성하세요.

CREATE OR REPLACE VIEW total_sales_by_store AS
	SELECT
		S.store_id,
        SUM(P.amount)
	FROM store S
    JOIN staff ST USING(store_id)
    JOIN payment P USING(staff_id)
    GROUP BY S.store_id;

SELECT * FROM total_sales_by_store;
DROP VIEW total_sales_by_store;

# 문제 30. 가장 많은 고객이 있는 상위 5개 국가를 보여주세요.

SELECT
	CO.country,
    COUNT(*) customer_count
FROM country CO
JOIN city CI USING(country_id)
JOIN address A USING(city_id)
JOIN customer C USING(address_id)
GROUP BY CO.country
ORDER BY customer_count DESC
LIMIT 5;



