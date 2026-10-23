def solution(price, money, count):
    result = 0
    for i in range(1,count+1):
        result += price * i
        
    if result <= money:
        return 0
    else:
        return result - money

  ## 풀이전략, 핵심 아이디어
  # 등차수열의 합을 반복문으로 풀어낸 문제
  # 값을 누적해서 합계를 구하는 방식 익히기
