SELECT *
FROM PLACES
WHERE HOST_ID IN(SELECT HOST_ID
                FROM PLACES
                GROUP BY HOST_ID
                HAVING COUNT(*) >= 2)
ORDER BY ID;

-- 풀이전략, 핵심 아이디어
-- 그룹화해서 필터링 한 조건을 WHERE에 넣어 조건에 맞는 것만 필터링하도록 in 사용
