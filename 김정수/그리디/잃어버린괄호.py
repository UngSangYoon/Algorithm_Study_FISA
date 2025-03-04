'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''


exp = input().split('-')

num = []

for i in exp:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0]

for i in range(1,len(num)):
    n -= num[i]


print(n)