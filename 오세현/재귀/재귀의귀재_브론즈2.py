"""
백준 25501번 재귀의 귀재 브론즈2

문제
정휘는 후배들이 재귀 함수를 잘 다루는 재귀의 귀재인지 알아보기 위해 재귀 함수와 관련된 문제를 출제하기로 했다.

팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 팰린드롬의 예시로 AAA, ABBA, ABABA 등이 있고, 팰린드롬이 아닌 문자열의 예시로 ABCA, PALINDROME 등이 있다.

어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. 아래 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.

def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))

정휘는 위에 작성된 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다.

구체적으로는, 문자열 
$S$를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다. 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.

정휘를 따라 여러분도 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.

입력
첫째 줄에 테스트케이스의 개수 
$T$가 주어진다. (
$1 \leq T \leq 1\,000$)

둘째 줄부터 
$T$개의 줄에 알파벳 대문자로 구성된 문자열 
$S$가 주어진다. (
$1 \leq \vert S\vert \leq 1\,000$)

출력
각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력한다.
"""


#처음에 생각했던 코드 재귀부분 (틀림)
def recursion(s, l, r):
    count_num = 0
    if l >= r:  #문자열 중간까지 판단했는데 처음과 끝이 같으면 1을 반환
        print(1, count_num)
    elif s[l] != s[r]: 
        return 0         #문자열의 처음과 끝이 다르면 0을 반환
    else: 
        count_num += 1
        return recursion(s, l+1, r-1)     #더 재귀해야 되면 다시 재귀함수 호출

#최종 제출한 코드
def recursion(s, l, r):
    if l >= r:  #문자열 중간까지 판단했는데 처음과 끝이 같으면 1을 반환
        return 1, l+1  #재귀 호출 횟수 = l + 1

    elif s[l] != s[r]: 
        return 0, l+1         #문자열의 처음과 끝이 다르면 0을 반환

    else: 
        return recursion(s, l+1, r-1)     #더 재귀해야 되면 다시 재귀함수 호출

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
            #문자열, 초기값 0, 문자 길이 - 1

test_num = int(input())

while test_num > 0:
    s = input()
    li1 = isPalindrome(s)
    print(li1[0], li1[1])
    test_num -= 1


#재귀 함수 호출 횟수 어떻게 count? -> 재귀함수 인자인 l로 해결
#반환값이 두 개라 리스트에 받아서 인덱스 번호로 출력함