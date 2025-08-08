USE bestproducts;

SELECT * FROM items LIMIT 1;
SELECT * FROM ranking LIMIT 1;

# 1.메인카테고리와 서브카테고리별 평균할인가격과 평균할인률을 출력해주세요.
SELECT R.main_category, R.sub_category, AVG(dis_price), AVG(discount_percent)
FROM items I
JOIN ranking R
ON I.item_code = R.item_code
GROUP BY R.main_category, R.sub_category
ORDER BY AVG(discount_percent) DESC;

# 2.판매자별 베스트상품 갯수, 평균할인가격, 평균할인률을 출력해주세요.
# - 베스트상품 갯수 순으로 내림차순 정렬해주세요.

SELECT
	provider,
    COUNT(*) count,
	AVG(dis_price) dis_price,
    AVG(discount_percent) dis_percent
FROM items
WHERE provider IS NOT NULL AND provider != ''
GROUP BY provider
ORDER BY count DESC;

# 3.메인카테고리별 베스트 상품 갯수가 20개 이상인 판매자의 판매자별 평균할인가격,
# 평균할인률, 베스트 상품 갯수를 출력해주세요.

SELECT
	R.main_category,
	I.provider,
    COUNT(*) count,
	AVG(dis_price) dis_price,
    AVG(discount_percent) discount_percent
FROM items I
JOIN ranking R ON I.item_code = R.item_code
WHERE provider IS NOT NULL AND provider != ''
GROUP BY I.provider, R.main_category
ORDER BY count DESC;

# 4.items 테이블에서 dis_price가 5만원 이상인 상품들 중
# main_category별 평균 dis_price와 discount_percent 출력하세요!!

SELECT
	main_category,
	AVG(dis_price) dis_price,
    AVG(discount_percent) discount_percent
FROM items I
JOIN ranking R ON I.item_code = R.item_code
WHERE dis_price >= 50000
GROUP BY main_category;

