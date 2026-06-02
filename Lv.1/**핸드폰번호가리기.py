def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]

## 풀이전략, 핵심 아이디어
# 뒷자리 4개를 뺀 만큼을 *로 곱해 *로 표시되도록 하고
# -4번째부터 끝까지는 그대로 가져와서
# 합치기

# 이런 생각이 잘 떠올라지도록 다시 복습 필요
