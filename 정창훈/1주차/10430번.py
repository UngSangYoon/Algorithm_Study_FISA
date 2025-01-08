'''
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

[출력]
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
'''

A, B, C = map(int, input('A, B, C 값을 입력해주시오.').split())
if 2 > A:
    print('A의 값은 반드시 2 이상 이여야합니다.')
elif C > 10000:
    print('C의 값은 반드시 10000 이하 이여야합니다.')
else:

    answer1 = (A + B) % C
    answer2 = ((A % C) + (B % C)) % C
    answer3 = (A * B) % C
    answer4 = ((A % C) * (B % C)) % C

print(answer1)
print(answer2)
print(answer3)
print(answer4)