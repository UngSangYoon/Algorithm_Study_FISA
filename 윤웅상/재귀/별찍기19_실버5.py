'''
예제 입력 1 
1
예제 출력 1 
*

예제 입력 2 
2
예제 출력 2 
*****
*   *
* * *
*   *
*****
'''
input_num = int(input())
star_box = [[' ']*(1+(input_num-1)*4) for _ in range(1+(input_num-1)*4)]
middle = (1+(input_num-1)*4)//2
star_box[middle][middle] = '*'
for i in range(1, input_num):
    for j in range(middle-(i*2), middle+(i*2) +1):
        star_box[middle-(i*2)][j] = '*'
        star_box[middle+(i*2)][j] = '*'
        star_box[j][middle-(i*2)] = '*'
        star_box[j][middle+(i*2)] = '*'

for i in star_box:
    print(''.join(i))
