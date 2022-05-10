def unique(list):
	i=0
	sum=[]
	while i<len(list):
		if list[i] not in sum:
			sum.append(list[i])
		i+=1
	print(sum)
unique([1,2,3,3,3,4,5])