'''
입력
입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

출력
각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.

예제 입력 1 
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
예제 출력 1 
0
10
5
'''
# 미래에 언젠가 오른다면 무조건 사야함 / 떨어지기만 한다면 무조건 팔아야함
# 전체 리스트에서 오르는 부분의 서브리스트 구성
# ex) [1, 1, 3, 1, 2] -> [[1, 1, 3], [1, 2]]
#   ) [10, 7, 6] -> [[10] , [7], [6]] -- 만약 감소만 한다면 감소부분까지 len이 1인 서브리스트가 구성될 것 
def find_increasing_subsequences(arr):
    subsequences = []
    temp_subsequence = []
    
    for i in range(len(arr)):
        if not temp_subsequence:
            temp_subsequence.append(arr[i])
        elif arr[i] >= arr[i - 1]:
            temp_subsequence.append(arr[i])
        else:
            subsequences.append(temp_subsequence)
            temp_subsequence = [arr[i]]
    
    if temp_subsequence:
        subsequences.append(temp_subsequence)
    
    return subsequences


T = int(input())

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    li = find_increasing_subsequences(li)
    ans = 0
    decrease = False
    for i in li:
        if len(i) == 1 and decrease == False:
            decrease = True
            ans += i[0]

        elif len(i) > 1:
            decrease = False
            for j in range(len(i)-1):
                ans += i[-1] - i[j]
    print(ans)