SELECT ID, CASE
            WHEN RANKING=1 THEN 'CRITICAL'
            WHEN RANKING=2 THEN 'HIGH'
            WHEN RANKING=3 THEN 'MEDIUM'
            WHEN RANKING=4 THEN 'LOW'
            END AS COLONY_NAME
FROM (SELECT ID, NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS RANKING
        FROM ECOLI_DATA) A
ORDER BY ID;

-- 풀이전략, 핵심 아이디어
-- 윈도우 함수 NTILE() 사용 => 정렬된 데이터를 4개의 그룹으로 균등하게 나눔
-- CASE 를 사용하여 등급 지정해주기
