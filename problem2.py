def fib(n):
	if(n <= 2): return 1;
	return fib(n-1) + fib(n-2)

i=1
sum = 0
while(fib(i) < 4000000):
	if(fib(i)%2 == 0):
		sum += fib(i)
	i+=1

print sum
