'''
문제
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

입력
첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

출력
첫째 줄에 게임의 상금을 출력 한다.

예제 입력 1 
3 3 6
예제 출력 1 
1300
'''

#주사위 값 입력
a = input().split()
#형 변환
for i in range(3):
  a[i] = int(a[i])

#상금 초기값 설정
money = 0

#셋 다 같은 경우
if a[0] == a[1] == a[2]:
    money = 10000 + a[0] * 1000

#두 개만 같은 경우
elif (a[0] == a[1]) and (a[0] != a[2]):
  money = 1000 + a[0] * 100
elif (a[0] == a[2]) and (a[0] != a[1]):
  money = 1000 + a[0] * 100
elif (a[1] == a[2]) and (a[1] != a[0]):
  money = 1000 + a[1] * 100

#셋 다 다른 경우
else:
  money = max(a) * 100

#상금 출력
print(money)

