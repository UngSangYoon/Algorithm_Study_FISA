# 1978번

'''문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.'''

num = int(input())

num_li = map(int, input().split())

# 소수는 1과 자기자신만을 약수로 가지는 수이다.
def get_division(n):
    li_ = set()
    for i in range(1, n+1):
        if n % i == 0:
            li_.add(i)
    return li_

count = 0

for j in num_li:
    j_set = get_division(j)
    if len(j_set) == 2:
        count += 1
print(count)