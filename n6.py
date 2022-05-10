def even(list):
	i=0
	sum=[]
	while i<len(list):
		if list[i]%2==0:
			sum.append(list[i])
		i+=1
	print(sum)
even([1,2,3,4,7,5,6,7,8,9])