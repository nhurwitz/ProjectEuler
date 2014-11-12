def getLargestPrimeFactor(n):
	lf = 1
	while n%2==0:
		lf = 2
		n = n/2

	f = 3
	while n!= 1:
		while n%f == 0:
			lf = f
			n = n/f
		f += 2
	return lf

print getLargestPrimeFactor(600851475143)