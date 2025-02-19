'''
문제
타슈는 대전시에서 제공하는 공용자전거 서비스이다. 시민들은 각 무인대여소에 배치된 자전거를 대여해 이용할 수 있고, 이용이 끝난 후에는 다시 무인대여소에 반납해야 한다. 자전거를 대여한 대여소에 다시 반납할 필요 없이 아무 대여소에 반납하면 된다.

대전시는 
$N$개의 대여소를 설치한 후, 자전거의 수요를 고려해서 각 대여소에 
$a_1,a_2,\cdots ,a_N$개의 자전거를 배치하고 서비스를 시작했다. 그리고 얼마 뒤에 서비스의 품질 개선을 위해 잠시 타슈 서비스를 중단하고 모든 자전거를 대여소에 반납하게 했다. 다행히도 유실된 자전거는 없었지만, 각 대여소에 위치한 자전거의 개수가 
$b_1,b_2,\cdots ,b_N$이 되었다.

대전시에서 일하는 영우는 타슈 서비스를 재개하기 전에 각 대여소에 위치한 자전거의 개수를 다시 
$a_1,a_2,\cdots ,a_N$으로 만들려고 한다. 영우는 직접 발로 뛰면서 
$i$번째 대여소에 위치한 자전거 한 대를 들어다가 
$j$번째 대여소로 옮길 수 있다. 영우는 자전거를 최소 몇 번 옮겨야 하는지 구해보자.

입력
첫째 줄에 정수 
$N(2\le N\le 100)$이 주어진다.

둘째 줄에 정수 
$a_1,a_2,\cdots ,a_N(1\le a_i\le 100)$이 공백으로 구분되어 주어진다.

셋째 줄에 정수 
$b_1,b_2,\cdots ,b_N(1\le b_i\le 100)$이 공백으로 구분되어 주어진다.

 
$a_1+a_2+\cdots +a_N$은 
$b_1+b_2+\cdots +b_N$과 같다.

출력
각 대여소에 위치한 자전거의 개수를 
$a_1,a_2,\cdots ,a_N$으로 만들기 위해서 자전거를 최소 몇 번 옮겨야 하는지 출력한다.

예제 입력 1 
4
3 1 4 2
2 2 3 3
예제 출력 1 
2
'''

n = int(input())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))

diff = []
for i in range(n):
    diff.append(alst[i] - blst[i])

cnt = 0
for i in range(n):
    if diff[i] > 0:
        cnt += diff[i]

print(cnt)
