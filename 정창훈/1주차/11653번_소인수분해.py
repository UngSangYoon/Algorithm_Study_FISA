N = int(input("소인수분해할 숫자를 입력하세요: "))

if N > 1:
    factor = 2
    while N > 1: # 이부분을 잘 모르겠음, 1이 반복될때 까지 진행을 목적인데 왜 N > 1 인지?
        if N % factor == 0:
            print(factor)
            N = N // factor
        else:
            factor += 1
