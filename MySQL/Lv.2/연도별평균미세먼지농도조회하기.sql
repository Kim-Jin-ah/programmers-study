SELECT YEAR(YM) AS YEAR, ROUND(AVG(PM_VAL1),2) AS 'PM10', ROUND(AVG(PM_VAL2),2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR
ORDER BY YEAR;

-- 측정 날짜에서 연도만 추출하고, 연도별 미세먼지와 초미세먼지 평균 농도 구하기
-- ROUND(숫자,자릿수)를 사용하여 소수점 둘째자리까지 반올림
