SELECT I.ID, N.FISH_NAME, I.LENGTH
FROM FISH_INFO I
INNER JOIN FISH_NAME_INFO N
ON I.FISH_TYPE = N.FISH_TYPE
WHERE (I.FISH_TYPE,I.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH)
                                FROM FISH_INFO
                                GROUP BY FISH_TYPE)
ORDER BY I.ID;

-- 풀이전략, 핵심 아이디어
-- 종류별 최대 길이를 구한 후 원본 테이블과 JOIN
-- 서브쿼리가 여러 값을 반환할 때 =이 아닌 IN 사용 주의
