def is_palindrome(n):
	for x in xrange(0, (len(n)+1)/2):
		rev = len(n) - x
		if(n[x] != n[len(n)-x-1]):
			return False

	return True

sum = 0
for i in range(0, 1000000):
	 sum = sum + i if (is_palindrome(str(bin(i)[2:])) and is_palindrome(str(i))) else sum

print sum
