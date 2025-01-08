a,b =map(int,input("").split())
c,d = set(),set()
for i in range(1,a+1):
    if a % i == 0:
        c.add(i)
for i in range(1,b+1):
    if b % i == 0:
        d.add(i)
gcd = max(c&d)
print(gcd)
print(int((a*b)/gcd))
