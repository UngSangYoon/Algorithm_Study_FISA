# a, b, c = map(int, input().split())

# for i in range(1,b+1):
#     if (a**i)<c

a, b, c = map(int, input().split())
print(((a%c)**(b%c)%c))

if (b%2)==0:
    print(((a%c)**(b%c)%c))
else:
    print(((a%c)**(b%c)%c))