N = int(input())
out = {}
yes = []
for i in range(N):
    inn = input()
    if inn in out:
        out[inn] += 1
    else:
        out[inn] = 1
count = max(out.values())

for word in out:
    if out[word] == count:
        yes.append(word)


result = sorted(yes)[0]
print(result)
