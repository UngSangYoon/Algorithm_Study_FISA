def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt +1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

num = int(input())
while num !=0:
   
    str_ = input()
    result, cnt = isPalindrome(str_)
    print('{} {}'.format(result, cnt))    
    num -= 1
