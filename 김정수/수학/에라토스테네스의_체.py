'''
백준[2960] 에라토스테네스의 체

에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

이 알고리즘은 다음과 같다.

2부터 N까지 모든 정수를 적는다.
아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
'''

N, K = map(int, input().split())

cnt = 0
remove_list = [False] * (N+1)

for i in range(2, N+1):
    if not remove_list[i]:
        remove_list[i] = True
        cnt += 1
        if cnt == K:
            print(i)
        for mul_num in range(i, N+1, i):
            if not remove_list[mul_num]:
                remove_list[mul_num] = True
                cnt += 1
                if cnt == K:
                    print(mul_num)



'''
remove_list를 N+1 크기만큼 만들어준 이유는 편의상 인덱스를 알아보기 쉽게(~번째와 같도록) 하기 위함입니다.

이 문제의 핵심은 remove_list의 인덱스가 곧 숫자라는 것과
이중 for문을 돌며 range안에 i부터 시작해 i씩 더해주는 방식으로
해당 배수를 지워주는 것입니다.


'''