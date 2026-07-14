def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)


a = 192
b = 162
print(gcd(a,b) == gcd(b,a), gcd(a,b))
