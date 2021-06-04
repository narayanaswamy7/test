import functools
n = int(input())
testcases = []
for i in range(n):
	numbers = [float(n) for n in input().split()]
	testcases.append(numbers)
for i in testcases:
	print('Yes' if round(100/(functools.reduce(lambda x,y : x*y, i)),2)<9.58 else 'No')
