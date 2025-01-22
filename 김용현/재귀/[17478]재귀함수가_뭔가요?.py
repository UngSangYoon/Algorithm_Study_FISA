def func(N,str1,str2,str3,str4,str5,str6):
    if N==0:

        print(str1)
        print(str5)
        print(str6)
        return


    print(str1)
    print(str2)
    print(str3)
    print(str4)
    func(N - 1, '____' + str1, '____' + str2, '____' + str3, '____' + str4,'____'+str5,'____'+str6)
    print(str6)


N=int(input())


str1 = '"재귀함수가 뭔가요?"'
str2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
str3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
str4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
str5 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
str6 = '라고 답변하였지.'
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
func(N,str1, str2, str3, str4,str5,str6)

