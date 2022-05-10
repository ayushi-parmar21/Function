def number(limit):
	i=0
	while i<=limit:
		if i%2==0:
			print(i,"EVEN",end=",")
		else:
			print(i,"ODD",end=",")
		i+=1
number(7)