def recur(idx, n):
    global arr

    if n == 1:
        return
    for i in range(idx + n//3, idx + 2*n//3):
        arr[i] = ' '
    
    recur(idx, n//3)
    recur(idx + 2*n//3, n//3)


while True:
    try:
        n = int(input())
        arr = ['-'] * (3**n)
        recur(0, len(arr))
        print(''.join(arr))
    except:
        break
