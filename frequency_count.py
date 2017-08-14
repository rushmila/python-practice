my_string = "My name is Moon"
res = {}

for i in my_string.lower():
#	res[i] = res.get(i, 0) + 1
	if res.get(i):
		res[i] += 1
	else:
		res[i] = 1
print(res)
