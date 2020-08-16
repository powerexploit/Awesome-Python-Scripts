#to separate the positive and negative numbers of the list

def Pos_Neg(L,n):
	List_Pos=[]
	List_Neg=[]
	for i in range(0,n):
		if(L[i]>=0):
			List_Pos.append(L[i])
		else:
			List_Neg.append(L[i])

	return List_Pos,List_Neg

def main():
	L=[]
	n=int(input("ENTER SIZE OF LIST"))
	print("Enter elements in list")
	for i in range(0,n):
		element=int(input())
		L.append(element)
	Positive_list,Negative_list=Pos_Neg(L,n)
	print("The list of positive Numbers",Positive_list)
	print("The list of negative Numbers",Negative_list)

if __name__=="__main__":
	main()

