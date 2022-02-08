#가장 높은 숫자가 쓰인 카드 한 장 뽑는 게임

#게임 룰
#1. 카드는 N행 X M열의 형태로 놓여 있다.
#2. 뽑으려는 카드가 포함된 행 선택
#3. 그다음 선택된 행에 포함된 카드 중 가장 작은 수가 적힌 카드 뽑기
#4. 따라서 처음에 카드를 골라낼 행을 고를 때, 이후 해당 행에서 가장 숫자가 낮은 카드를
#   뽑을 것을 고려해 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

from random import randint

#입력 조건
#첫째 줄에 N은 1이상, M은 100이하, 공백 기준으로 주어짐
#둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 수는 1 ~ 10,000 까지의 자연수
#첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자 출력

#입력 예시              #출력 예시
#3 3                      #2
#3 1 2
#4 1 4
#2 2 2

#행을 하나씩 골라 가장 작은 수가 적힌 카드부터 뽑아내야 함
#N = 행, M = 열

N, M = map(int, input().split())

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    #입력하는 행의 숫자 중 가장 작은 수를 min함수로 구함
    min_num = min(data)
    #가장 작은 수 중 가장 큰 수 찾기
    result = max(result, min_num)

print(result)