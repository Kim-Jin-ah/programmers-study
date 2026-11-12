SELECT ID, CASE
                WHEN SIZE_OF_COLONY <= 100 THEN "LOW"
                WHEN SIZE_OF_COLONY <= 1000 THEN "MEDIUM"
                ELSE "HIGH"
            END AS SIZE 
FROM ECOLI_DATA
ORDER BY ID;

-- 풀이전략, 핵심 아이디어
-- 조건문 CASE WHEN 활용
