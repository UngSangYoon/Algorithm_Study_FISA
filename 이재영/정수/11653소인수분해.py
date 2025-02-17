N = int(input(""))
out = []
i = 2
while 1:
    if N % i == 0:
        out.append(i)
        N = N // i
    else:
        i += 1
        if i > N:
            break
for i in out:
    print(i)
