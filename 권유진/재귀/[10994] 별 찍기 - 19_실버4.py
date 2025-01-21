'''
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 차례대로 별을 출력한다.

예제 입력 1 
1
예제 출력 1 
*

예제 입력 2
2
예제 출력 2 
*****
*   *
* * *
*   *
*****

예제 입력 3 
3
예제 출력 3 
*********
*       *
* ***** *
* *   * *
* * * * *
* *   * *
* ***** *
*       *
*********
'''

N=int(input())
shape = [[' ' for _ in range(4*N-3)]for _ in range(4*N-3)]

def star(n,x,y):
    if n==1 :
      shape[x][y]='*'
      return 
    
    tmp=4*n - 3

    for i in range(tmp):
      shape[x][y+i]='*' # 좌
      shape[x+i][y]='*' # 상
      shape[x+tmp-1][y+i]='*' # 우
      shape[x+i][y+tmp-1]='*' # 하
    
    star(n-1,x+2,y+2) # 밖에 찍고 계속 안쪽으로로


star(N,0,0)
for s in shape :
   print(''.join(s)) 