SELECT ANIMAL_ID,NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE "Neutered%" THEN "O"
        WHEN SEX_UPON_INTAKE LIKE "Spayed%" THEN "O"
        ELSE "X"
    END AS "중성화"
FROM ANIMAL_INS;

# CASE를 사용하여 조건에 따라 결과를 다르게 출력하기
# 두 조건을 하나로 합친다면
SELECT
    ANIMAL_ID,
    NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE 'Neutered%'
          OR SEX_UPON_INTAKE LIKE 'Spayed%'
        THEN 'O'
        ELSE 'X'
    END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
