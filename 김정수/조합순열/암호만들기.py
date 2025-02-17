'''
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
'''


from itertools import combinations


n , k = map(int, input().split())
list_ = list(map(str, input().split()))
list_a = []
list_b = []


for i in list_ :
    if i in ["a","e","i","o","u"]:
        list_a.append(i)
    else:
        list_b.append(i)


combinations_a = []


for r in range(1, len(list_a) + 1):
    combinations_a.extend(combinations(list_a, r))


combinations_b = []


for r in range(2, len(list_b) + 1):
    combinations_b.extend(combinations(list_b, r))


result_set = set()


for a in combinations_a:
    for b in combinations_b:
        if len(a + b) == n:
            result_set.add("".join(sorted(a + b)))


sorted_results = sorted(result_set)


for i in sorted_results:
    print(i)


'''
1. 주어진 문자들을 모음(list_a)와 자음(list_b)으로 나눔
2. 모음 조합 생성(최소 1개 이상의 모음 조합 생성)
3. 자음 조합 생성(최소 2개 이상의 자음 조합 생성)
4. 최종 조합 만들기 - 각 모음 조합과 자음 조합을 합쳐서 총 글자 수가 n이 되는 경우에 한해
   알파벳 순으로 정렬한 문자열을 결과 집합에 추가
'''