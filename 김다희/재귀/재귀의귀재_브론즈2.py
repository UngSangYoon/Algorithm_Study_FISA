# 25501
# 아이디어: l을 호출 횟수로 사용하자~~

t = int(input())

def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)

def recursion(s, l, r):
    if l >= r:
        return 1, l+1
    elif s[l] != s[r]:
        return 0, l+1
    else:
        return recursion(s, l + 1, r - 1)

for _ in range(t):
    ss = input()
    print(is_palindrome(ss)[0], is_palindrome(ss)[1])