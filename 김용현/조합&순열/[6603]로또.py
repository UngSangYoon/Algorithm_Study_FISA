choose =[]
K=0
arr=[]

def combination(index,level):
    global choose,K,arr
    if level == 6:
        for i in choose:
            print(i,end=' ')
        print()
        return


    for i in range(index,K):
        choose.append(arr[i])
        combination(i+1,level+1)
        choose.pop()






while 1:
    I=  list (map(  int,  input().split() ) )

    K=I[0] # 첫번째 값이 K 값이기에

    arr= I[1:]

    if K==0:
        break
    choose = []
    combination(0,0)
    print()




    """
    
    input은 문자열로 값을 받아옴
    
    input.split()을 하게 된다면 
    ()안에 있는 문자를 기본으로하여 
    input에 있는 문자열을 리스트로 바꿔준다.
    ()이면 디폴트로 ' ' 즉 공백을 의미한다.
    
    난 지금 list에 저장된 문자들을 다 정수로 바꿔주고 싶다.
    map을 사용해서 int로 모든 것을 바꿔준다.
    
    map을 사용하게 된다면 포인터 값만 돌려주기에 list를 써서 확실하게 만들어 줘야한다.
    
    """