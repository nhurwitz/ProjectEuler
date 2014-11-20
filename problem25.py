fibMap = dict()
fibMap[1] = 1
fibMap[2] = 1

def fib(n):
	if(n in fibMap.keys()):
		return fibMap[n]

	fibMap[n] = fibMap[n-1] + fibMap[n-2]
	return fibMap[n]

num = 1
while(len(str(fib(num))) < 1000):
	num += 1

print num