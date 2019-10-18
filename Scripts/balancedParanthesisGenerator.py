def parenthesis(oBrack , clBrack,n,s=[]):
	
	if(clBrack == n):
		print(" ".join(s))

	else:
		if(oBrack > clBrack):
			s.append(")")
			parenthesis(oBrack,clBrack+1,n)
			s.pop()
		if(oBrack<n):
			s.append("(")
			parenthesis(oBrack+1, clBrack , n)
			s.pop()
	return
n = int(input())
parenthesis(0, 0, n)
