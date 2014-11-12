sum = 0

for i in range(0, 1000):
	sum = (sum + i) if (i%3==0 or i%5==0) else sum

print sum
