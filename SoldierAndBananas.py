k, n, w = list(map(int, input().split()))
totalAmount = 0
result = sum([totalAmount + (i*k) for i in range(1, w+1)])
if result <= n:
	print(0)
else:
	print(result-n)
