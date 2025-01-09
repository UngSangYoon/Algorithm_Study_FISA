#최대공약수와 최소공배수
a,b = map(int, input().split())

#입력된 값 중 큰 값을 x자리에 넣기
if a >= b:
  x = a
  y = b
else:
  x = b #24
  y = a #18

#최대공약수 반환
def div(x, y):
  
  divisor = []

  for i in range(1, x+1):
    if (x % i == 0) and (y % i == 0):
      divisor.append(i)

  return max(divisor)

#최소공배수 반환
def mul(x, y):
    return (x * y) // div(x, y)

print(div(a, b))
print(mul(a, b))
