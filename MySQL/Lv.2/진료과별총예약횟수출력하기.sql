SELECT MCDP_CD AS 진료과코드, COUNT(*) AS 5월예약건수
FROM APPOINTMENT
WHERE APNT_YMD LIKE "2022-05%" 
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC, 진료과코드 ASC;

# 날짜 조건으로 데이터를 먼저 필터링하고, GROUP BY로 그룹을 나눈 다음, COUNT(*)로 개수 세기
# WHERE -> GROUP BY -> SELECT -> ORDER BY 흐름 이해하기
