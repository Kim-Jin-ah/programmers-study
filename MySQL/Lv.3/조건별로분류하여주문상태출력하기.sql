SELECT ORDER_ID, PRODUCT_ID, OUT_DATE,
    CASE 
        WHEN OUT_DATE <= '2022-05-01' THEN "출고완료"
        WHEN OUT_DATE > '2022-05-01' THEN "출고대기"
        ELSE "출고미정"
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;

-- 풀이전략, 핵심 아이디어
-- CASE 사용하여 날짜를 기준으로 조건을 나누고, 조건에 따라 새로운 값 출력
