#백준 10430

#세 수를 입력
a, b, c = map(int,input().split())

#(A+B)%C
print((a+b)%c)

#((A%C)+(B%C))%C
print(((a%c)+(b%c))%c)

#(AxB)%C
print((a*b)%c)

#((A%C)x(B%C))%C

print(((a%c)*(b%c))%c)

