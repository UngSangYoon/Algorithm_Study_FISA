"""
문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.
"""

import itertools

n = int(input())
n_list = list(range(1, n+1))

# 원래 생각했던 방법... 근데 틀렸어요.
# for i in list(itertools.permutations(n_list)):
#     c_result = ' '.join(str(i))
#     print(c_result)

"""
위 코드의 출력 결과
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
"""

# 아마 출력이 튜플 형식으로 되어서 그런듯 함
# map() 함수로 각 요소를 str로 변환 → 정답입니다.
for i in list(itertools.permutations(n_list)):
    c_result = ' '.join(map(str, i))
    print(c_result)