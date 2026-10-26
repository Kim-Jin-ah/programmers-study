SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "Dog"
ORDER BY NAME,ANIMAL_ID;

## 풀이전략, 핵심 아이디어
# %의 자리 신경쓰기, 두 개 공통인 조건을 찾을 때 AND 사용하기
