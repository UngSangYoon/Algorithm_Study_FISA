'''
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
'''

s = int(input())
total = 0
count = 0

while True:
    count += 1
    total += count
    if total > s:
        break

print(count-1)