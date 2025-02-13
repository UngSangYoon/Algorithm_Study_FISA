'''
문제
정휘는 후배들이 재귀 함수를 잘 다루는 재귀의 귀재인지 알아보기 위해 재귀 함수와 관련된 문제를 출제하기로 했다.

팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 팰린드롬의 예시로 AAA, ABBA, ABABA 등이 있고, 팰린드롬이 아닌 문자열의 예시로 ABCA, PALINDROME 등이 있다.

어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. 아래 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.
'''

# 문자열을 함수의 인자로 받아야함!
# 앞에서 읽고 뒤에서 읽었을 때 같은 문자열이라는게 무슨 말일까?
# 처음에는 입력받은 문자열의 첫 인덱스와 마지막 인덱스를 비교한다.
def recursion(str_, front_idx, end_idx, num_ = 1):
    # 계속 돌고 돌아 끝까지 오면 팰린드롬
    if front_idx >= end_idx:
        return 1, num_
    # 다르면 팰린드롬이 아님.
    elif str_[front_idx] != str_[end_idx]:
        return 0, num_
    else:
        # 문자열 처음과 끝이 같으면
        # return을 하자 -> 근데 return 할 때 인덱스를 앞은 1을 추가를 해야하고 뒤의 인덱스는 1을 뺴야겠지?
        return recursion(str_, front_idx = front_idx + 1, end_idx = end_idx - 1, num_ = num_ + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

int_ = int(input())
for _ in range(int_):
    string = input()
    print(isPalindrome(string)[0], isPalindrome(string)[1])