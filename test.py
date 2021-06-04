def sumofdiv(number):
    divisors = [1]
    for i in range(2, number+1):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)

t = int(input())
for i in range(t):
	c = int(input())
	for i in range(1,c):
		if c == sumofdiv(i):
			print(i)
		else:
			print(-1)


print('hello, World')
print('testing git commits')
