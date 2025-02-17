import time

# 예제 데이터
results = [[i for i in range(100)] for _ in range(1000)]  # 1000x100 리스트

# 첫 번째 방식
start_time = time.time()
for i in range(len(results)):
    for j in range(len(results[i])):
        print(results[i][j], "", end="")
    print()
print("첫 번째 방식 소요 시간:", time.time() - start_time)

# 두 번째 방식
start_time = time.time()
for result in results:
    print(" ".join(map(str, result)))
print("두 번째 방식 소요 시간:", time.time() - start_time)