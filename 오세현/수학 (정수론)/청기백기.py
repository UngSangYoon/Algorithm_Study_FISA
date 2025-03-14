'''
문제
소프트웨어융합대학 학생회에서 주최한 소융체전에서 청기 백기 뒤집기 게임이 한창이다.
소프트웨어학부, ICT융합학부가 번갈아가면서 게임을 진행하는 중이다.
게임의 규칙은 간단하다. 게임을 진행할 차례인 학부에서 출전한 선수들 N명이 존재한다.
학생들의 앞 탁자에는 N개의 깃발이 청색이 위로 백색이 아래로 보이도록 놓여있다.
이때 출전한 선수 중 첫 번째 선수는 N개의 깃발 중 1의 배수에 해당하는 번호의 깃발을 뒤집어 놓는다.
다음 두 번째 선수는 N개의 깃발 중 2의 배수에 해당하는 번호의 깃발을 뒤집어 놓는다.
i 번째 선수는 i의 배수에 해당하는 번호의 깃발을 뒤집고, N 번째 선수까지 진행하면 끝이 난다.
그렇다면 이 게임에서 N 명의 선수가 참가하고 N개의 깃발이 존재할 때, N 번째 선수까지 진행하여 완료된 상태에서 백색이 위로 놓여있는 깃발의 수가 몇 개인지 알아보자.

입력
첫 번째 줄에 출전한 학생의 수이자, 깃발의 개수인 N(1 ≤ N ≤ 2,100,000,000)이 주어진다.

출력
첫 번째 줄에 N 번째 선수까지 진행한 후의 상태의 깃발 중 백색이 위로 놓여있는 깃발의 수를 출력한다.
'''

#각 깃발의 색은 뒤집은 횟수 = 약수 개수에 따라 결정됨
#현재 깃발이 청기이므로, 약수의 개수가 홀수면 백기, 짝수면 청기
#ex) n=3, 1의 약수는 1개->백기, 2의 약수는 2개->청기, 3의 약수는 2개-> 청기

#약수가 홀수인 경우->약수 중 제곱근이 있음

#입력 받기
n = int(input())


i = 1		#깃발 번호
count = 0		#백기 count

while i * i <= n:		#깃발 번호가 제곱수면, 백기임
	count += 1		#백기 개수 +1
	i += 1

print(count)

