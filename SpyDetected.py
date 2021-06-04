t = int(input())
occurrences = dict();
for i in range(t):
	n = int(input())
	data = list(map(int, input().split()))
	for i in data:
		if i in occurrences:
			occurrences[i] += 1
		else:
			occurrences[i] = 1
	for i in occurrences:
		if(occurrences[i] == 1):
			print(data.index(i)+1)
	data = []
	occurrences = dict()
