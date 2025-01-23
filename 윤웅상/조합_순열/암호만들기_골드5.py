L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
pw = []
vowel_count = 0

def password(index, level):
    global vowel_count
    if level == L:
        vowel_count = 0
        for vowel in "aeiou":
            c = pw.count(vowel)
            vowel_count += c
        if vowel_count and (L - vowel_count) >= 2:
            print(''.join(pw))

    for i in range(index, C):
        pw.append(lst[i])
        password(i+1, level + 1)
        pw.pop()

password(0, 0)
