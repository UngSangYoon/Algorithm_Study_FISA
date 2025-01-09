ans = ""
a = int(input())
while a!=0:
	a -= 1
	if ans == "":
		ans = input()
	else:
		b = input()
		for i in range(0,len(ans)):
			if ans[i] != b[i]:
				ans = list(ans)
				ans[i] = "?"
				ans = (''.join(ans))
				
print(ans)