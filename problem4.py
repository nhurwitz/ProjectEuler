def isPalindrome(n):
	s = str(n)
	for x in xrange(0, (len(s)+1)/2):
		rev = len(s) - x
		if(s[x] != s[len(s)-x-1]):
			return False

	return True

def findPalindrome():
	largest = 0
	for x in xrange(999, 100, -1):
		for y in xrange(999, 100, -1):
			z = x*y
			if isPalindrome(z):
			 largest = z if z > largest else largest

	return largest

print findPalindrome()