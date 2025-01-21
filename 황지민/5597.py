#5597 
x = range(1, 31)
x = list(x)
b = []
c =[]

for i in range(28):
    a = int(input())
    b.append(a)
    
result = [i for i in x if i not in b]

print(min(result))
result.remove(min(result))
print(min(result))