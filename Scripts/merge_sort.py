def merge_sort(lst_main):
	if len(lst_main) <= 1:
		return lst_main
	else:
		mid = len(lst_main) // 2

		l = merge_sort(lst_main[:mid])
		r = merge_sort(lst_main[mid:])

		return merge(l, r)



def merge(lst_left, lst_right):
	lst_ord = []
	p_left = 0
	p_right = 0

	while p_left < len(lst_left) and p_right < len(lst_right):
		if lst_left[p_left] > lst_right[p_right]:
			lst_ord.append(lst_right[p_right])
			p_right += 1
		else:
			lst_ord.append(lst_left[p_left])
			p_left += 1

	for i in range(p_left, len(lst_left)):
		lst_ord.append(lst_left[i])

	for i in range(p_right, len(lst_right)):
		lst_ord.append(lst_right[i])

	return lst_ord

import random

def main():
	lst = []

	for i in range(100):
		lst.append(random.randrange(9))

	print(merge_sort(lst))
	
	return 0

if __name__ == '__main__':
	main()