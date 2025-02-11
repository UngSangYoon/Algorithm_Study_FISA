num = int(input())
list_ = []

for _ in range(num):
    list_.append(tuple(input().split()))

list_ = [(entry[0], int(entry[1]), int(entry[2])) for entry in list_]

def count_possible_numbers_bruteforce(conditions):
    count = 0

    for i in range(1, 1000):
        num_str = f"{i:03d}"  
        valid = True

        for cond_num, strikes, balls in conditions:
            if strikes == 0 and balls == 0:
                if any(c in num_str for c in cond_num):  
                    valid = False
                    break 
            
            else:
                strike_count = sum(num_str[j] == cond_num[j] for j in range(3))
                ball_count = sum((c in num_str) for c in cond_num) - strike_count

                if strike_count != strikes or ball_count != balls:
                    valid = False
                    break 

        if valid:
            if any(strikes == 3 for _, strikes, _ in conditions):
                return 1 
            count += 1

    return count

print(count_possible_numbers_bruteforce(list_))
