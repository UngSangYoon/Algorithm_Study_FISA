def func(S, current, start, k, result):
    if len(current) == k:
        result.append(current[:])


    for i in range(start, k):
        current.append(S[i])
        func(S, current, i + 1, k, result)
        current.pop()


import sys

# k는 배열에 있는 총 가짓수
N=int(input())
results=[]
arr = [i for i in range(1,N+1)]

func(arr,[],0,N,results)

print(results)


# input = sys.stdin.read
#
# data = input().strip().split('\n')
# results = []
#
# for line in data:
#     if line == "0":
#         break
#
#     nums = list(map(int, line.split()))
#     k = nums[0]
#     S = nums[1:]
#
#     result = []
#     func(S, [], 0, k, result)
#
#
#     case_result = "\n".join(" ".join(map(str, comb)) for comb in result)
#     results.append(case_result)
#
#
# print("\n\n".join(results))