fibMap = dict()
fibMap[1] = 1
fibMap[2] = 1

def fib(n):
	if(n in fibMap.keys()):
		return fibMap[n]

	fibMap[n] = fibMap[n-1] + fibMap[n-2]
	return fibMap[n]

i=1
sum = 0
while(fib(i) < 4000000):
	if(fib(i)%2 == 0):
		sum += fib(i)
	i+=1

print sum
