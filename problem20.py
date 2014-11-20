facMap = dict()
facMap[1] = 1

def fac(n):
	if n in facMap.keys():
		return facMap[n]

	facMap[n] = n * facMap[n-1]
	return facMap[n]

for i in range(1,100):
	fac(i)

print(sum(map(int,str(fac(100)))))

