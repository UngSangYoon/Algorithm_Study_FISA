"""
백준 로또 실버2
문제
독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.

로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

"""

def generate_combinations(S, index, chosen):
    # 선택한 숫자가 6개가 되면 출력
    if len(chosen) == 6:

        #리스트 chosen의 원소를 공백으로 구분된 문자열로 변환하여 출력함
        print(" ".join(map(str, chosen)))
        return

    # 조합 생성 (현재 인덱스부터 끝까지)
    for i in range(index, len(S)):
        chosen.append(S[i])  # 현재 숫자 선택
        generate_combinations(S, i + 1, chosen)  # 다음 숫자 선택
        chosen.pop()  # 선택한 숫자 제거 (백트래킹)

while True:
    # 입력받기
    lst = list(map(int, input().split()))
    k = lst[0]

    # 종료 조건
    if k == 0:
        break

    # lst에서 k를 뺀, 집합 S 추출
    S = lst[1:]

    # 조합 생성 함수 호출
    generate_combinations(S, 0, [])

    # 각 테스트 케이스 사이 빈 줄 출력
    print()
