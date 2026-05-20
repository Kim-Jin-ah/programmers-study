def solution(numbers, direction):
    answer = []
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]

  ## 풀이전략, 핵심 아이디어
  # 리스트 순서 뒤로 미는 방법 : 인덱스 활용하기 기억!
