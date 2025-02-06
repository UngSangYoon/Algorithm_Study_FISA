'''
소프트웨어융합대학 학생회에서 주최한 소융체전에서 청기 백기 뒤집기 게임이 한창이다. 
소프트웨어학부, ICT융합학부가 번갈아가면서 게임을 진행하는 중이다. 게임의 규칙은 간단하다. 
게임을 진행할 차례인 학부에서 출전한 선수들 N명이 존재한다. 
학생들의 앞 탁자에는 N개의 깃발이 청색이 위로 백색이 아래로 보이도록 놓여있다. 
이때 출전한 선수 중 첫 번째 선수는 N개의 깃발 중 1의 배수에 해당하는 번호의 깃발을 뒤집어 놓는다. 
다음 두 번째 선수는 N개의 깃발 중 2의 배수에 해당하는 번호의 깃발을 뒤집어 놓는다. 
i 번째 선수는 i의 배수에 해당하는 번호의 깃발을 뒤집고, N 번째 선수까지 진행하면 끝이 난다. 
그렇다면 이 게임에서 N 명의 선수가 참가하고 N개의 깃발이 존재할 때, N 번째 선수까지 진행하여 완료된 상태에서 백색이 위로 놓여있는 깃발의 수가 몇 개인지 알아보자.
'''

# n = int(input())

# list_ = [False]*(n)

# tmp = 1
# while (tmp<=n):
#     for i in range(1,n+1):
#         if(i%tmp)==0:
#             list_[i-1] = not list_[i-1]
#     tmp+=1

# print(list_.count(True))

# for i in range(1, n+1):
#     flag= False
#     for j in range(1, i+1):
#         if i%j==0:
#              flag = not flag
    
#     if flag == True:
#         cnt +=1


# def divisor(number): # number : 16
#     result = []
#     for i in range(1, int(number**(1/2))+1):
#         if number%i==0:
#             result.append(i)
#             if i < number//i:
#                 result.append(number//i)
#         		# [1, 16, 2, 8, 4]
#     return result 

# n = int(input())
# cnt = 0

# for i in range(1, n+1):
#     if (len(divisor(i))%2)!=0 :
#         cnt +=1
    
# print(cnt)

n = int(input())
cnt = 0
tmp = 0

while True:
    tmp +=1

    if (tmp**2)<=n:
        cnt+=1
        
    else : break
    
print(cnt)