def square(i):
	return i*i

solution = square(sum(xrange(1,101))) - sum(map(square,xrange(1,101)))

print str(solution)