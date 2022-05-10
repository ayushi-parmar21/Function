def fun(a):
	i=0
	count=0
	coun=0
	while i<len(a):
		if a[i]>=0:
			count+=1
		else:
			coun+=1
		i+=1
	print("positive number in list: ",count)
	print("negative number in list: ",coun)
fun([2,-7,5,-64,-14])