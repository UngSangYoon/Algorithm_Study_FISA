'''
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
1
예제 출력 1 
9
예제 입력 2 
2
예제 출력 2 
17
'''
# 정답
N = int(input())

# dp 테이블 0 ~ 9
dp = [[0]*10 for _ in range(N)]

# 초기화
for i in range(1, 10):
    dp[0][i] = 1

# n : 자리수, K 마지막 숫자
for n in range(1, N):
    dp[n][0] = dp[n-1][1]
    dp[n][9] = dp[n-1][8]
    
    for k in range(1, 9):
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]

print(sum(dp[N-1])%1000000000)


# 시간 초과
class TreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    @staticmethod
    def build_tree(value, depth, max_depth, memo):
        if depth > max_depth: # 트리 생성 X
            return None
    
        if(value, depth) in memo:
            return memo[(value, depth)]
        
        node = TreeNode(value)

        if value == 9:
            node.left = TreeNode.build_tree(8, depth+1, max_depth, memo)

        elif value == 0:
            node.right = TreeNode.build_tree(1, depth+1, max_depth, memo)
            
        else: 
            node.left = TreeNode.build_tree(value-1, depth+1, max_depth, memo)
            node.right = TreeNode.build_tree(value+1, depth+1, max_depth, memo)
        
        memo[(value, depth)] = node
        return node
    

def count_leaf_nodes(node):
    if not node:
        return 0
    
    if not node.left and not node.right:
        return 1
    
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

max_depth = int(input())
total_num = 0
memo = {}

for i in range(1, 10):
    root = TreeNode.build_tree(i, 1, max_depth, memo)
    leaf_count = count_leaf_nodes(root)
    total_num += leaf_count


print(total_num)
