SELECT Left(PRODUCT_CODE,2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY Left(PRODUCT_CODE,2)
ORDER BY CATEGORY ASC;

## 풀이전략, 핵심 아이디어
# 상품 코드의 앞 두 글자를 추출하여 그룹화 후
# 그것의 상품 개수를 구하고 카테고리별 오름차순 정렬
