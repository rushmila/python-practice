numbers = [11, 10, 9, 6, 11, 5, 7, 8, 8, 10]
remove_duplicates = []
duplicates = []
data = {}


for item in numbers:
	if not data.get(item):
		data[item] = "x"
		print(data)
		remove_duplicates.append(item)
	else:
		duplicates.append(item)
print(remove_duplicates)
print(duplicates)
