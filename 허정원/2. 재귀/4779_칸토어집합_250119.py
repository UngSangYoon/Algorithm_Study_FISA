'''
ans = ['' for _ in range(13)]
ans[0] = '-'

for i in range(1, 13):
    ans[i] = ans[i-1] + (' '*(3**(i-1))) + ans[i-1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break
'''

def func(k):
    if k == 0:
        return '-'

    # recursive
    return func(k-1) + (' ' * (3**(k-1))) + func(k-1)

while True:
    try:
        N = int(input())
        print(func(N))
    except:
        break
