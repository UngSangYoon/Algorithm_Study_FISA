def make_prime_list(n):

    """
    bool 리스트 arr[n+1]을 생성하여
    소수인 인덱스엔 True
    아닌 수들에겐 False 넣고
    리스트 arr 반환
    """
    arr =[True for _ in range(n+1)]
    arr[0] = False
    arr[1] = False



    for i in range(2,int(n**0.5+1)):
        if arr[i]:
            for j in range(i*i, n+1, i):
                """
                i x 2 부터 시작해도 괜찮긴 하지만
                i x i 부터 시작하는게 시간복잡도 측면에서 미세하마 유리할수도
                i x 2 부터 하면 이미 지워진 수를 다시 검산하는 일이 발생
                예를들어 i가 5라고 가정하면
                i가 2,3 일때 이미 제거가 됨
                5 x 2, 5 x 3 등이 이미 제거되는 것
                따라서 소수 i가 한번 더 있는 i x i 부터 시작하는 것이 유리?
                """
                arr[j]=False
    return arr





# 배열의 장점 위치를 알때 시간 복잡도: O(1)

def gold_bach(n,prime_list):
    """
    :param n: 짝수 n
    :param prime_list:소수 정보를 담고있는 리스트
    :return: 골드바흐 파티션의 수
    """
    cnt=0

    for i in range(2,n//2+1):   # n//2까지만 반복문을 돌려도 됨
        if prime_list[i]:       # 배열의 인덱스 조회 O(1)로 간결하게 처리
            if prime_list[n-i]:
                cnt+=1

    return cnt



T=int(input())

case_list = [int(input()) for _ in range(T) ]

prime_list=make_prime_list(max(case_list))

for case in case_list:
    print(gold_bach(case,prime_list))