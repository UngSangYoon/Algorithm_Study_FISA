def recursion(s, l, r):
    global count
    if l >= r: 
        count += 1
        return 1 
    elif s[l] != s[r]:
        count += 1 
        return 0
    else: 
        count += 1
        return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)
n = int(input())
out = []
for i in range(n):
    out.append(input(""))
for i in out:
    count = 0
    print(isPalindrome(i), count)
